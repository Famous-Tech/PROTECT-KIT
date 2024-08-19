import subprocess
import os
import re
import json
from colorama import Fore, Style
from main import get_malware_signatures_path

API_KEY = '54c7eeb1cfba5e921b7d375077f42880d383c7238479e63405ad3321c6478c34'  # Remplacez par votre API Key
API_URL = 'https://www.virustotal.com/vtapi/v2/url/report'
API_FILE_URL = 'https://www.virustotal.com/vtapi/v2/file/report'
API_SCAN_URL = 'https://www.virustotal.com/vtapi/v2/file/scan'

def load_malware_signatures():
    try:
        with open(get_malware_signatures_path(), 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

MALWARE_SIGNATURES = load_malware_signatures()

def analyze_apk(apk_path):
    temp_dir = "temp_apk_analysis"
    os.makedirs(temp_dir, exist_ok=True)
    
    # Décompiler l'APK
    subprocess.call(["apktool", "d", apk_path, "-o", temp_dir])
    
    # Analyser les fichiers décompilés pour voir s’il y a des trucs malveillants 
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            if file.endswith(".smali"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    for signature in MALWARE_SIGNATURES:
                        if re.search(signature, content):
                            return Fore.RED + f"Malicious pattern detected: {signature}" + Style.RESET_ALL
    
    # Nettoyer le répertoire temporaire
    subprocess.call(["rm", "-rf", temp_dir])
    
    return Fore.GREEN + "No malicious patterns detected." + Style.RESET_ALL

def check_apk(apk_path):
    # Vérifier avec VirusTotal
    vt_result = check_file(apk_path)
    if "Safe file" not in vt_result:
        return vt_result
    
    # Analyser l'APK
    return analyze_apk(apk_path)

def check_file(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    params = {'apikey': API_KEY, 'resource': file_hash}
    response = requests.get(API_FILE_URL, params=params)
    if response.status_code == 200:
        json_response = response.json()
        if json_response['response_code'] == 1:
            positives = json_response['positives']
            if positives > 0:
                return Fore.RED + f"Malicious file detected! ({positives} engines flagged this file)" + Style.RESET_ALL
            else:
                return Fore.GREEN + "Safe file." + Style.RESET_ALL
        else:
            return Fore.YELLOW + "File not found in VirusTotal database." + Style.RESET_ALL
    else:
        return Fore.RED + "Error connecting to VirusTotal." + Style.RESET_ALL
