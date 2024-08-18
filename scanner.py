import requests
from colorama import Fore, Style
from urllib.parse import urlparse
from difflib import SequenceMatcher

API_KEY = '54c7eeb1cfba5e921b7d375077f42880d383c7238479e63405ad3321c6478c34'  # Remplacez par votre API Key si vous en avez un j’aime pas trop quand on utilise le mien 👀
API_URL = 'https://www.virustotal.com/vtapi/v2/url/report'

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def check_virus_total(url):
    params = {'apikey': API_KEY, 'resource': url}
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        json_response = response.json()
        if json_response['response_code'] == 1:
            positives = json_response['positives']
            if positives > 0:
                return Fore.RED + f"Malicious link detected! ({positives} engines flagged this URL)" + Style.RESET_ALL
            else:
                return Fore.GREEN + "Safe link." + Style.RESET_ALL
        else:
            return Fore.YELLOW + "Link not found in VirusTotal database." + Style.RESET_ALL
    else:
        return Fore.RED + "Error connecting to VirusTotal." + Style.RESET_ALL

def check_domain_similarity(url, known_domains):
    parsed_url = urlparse(url)
    url_domain = parsed_url.netloc
    for known_domain in known_domains:
        if similar(url_domain, known_domain) > 0.8:
            return Fore.RED + f"Suspicious domain detected! Similar to {known_domain}" + Style.RESET_ALL
    return None

def check_link(url, malicious_links):
    # Check VirusTotal
    vt_result = check_virus_total(url)
    if "Safe link" not in vt_result:
        return vt_result
    
    # Check malicious.json
    if url in malicious_links:
        return Fore.RED + "Malicious link detected! (Known malicious link)" + Style.RESET_ALL
    
    # Check domain similarity
    known_domains = ["whatsapp.com", "facebook.com", "google.com" , "https://chat.whatsapp.com/"]
    similarity_result = check_domain_similarity(url, known_domains)
    if similarity_result:
        return similarity_result
    
    return Fore.GREEN + "Safe link." + Style.RESET_ALL
