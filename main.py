import os
import colorama
from colorama import Fore, Style
from languages import set_language, get_translation
from utils import get_malware_signatures_path, get_malicious_links_path
from scanner import check_link, check_apk, check_file
import json
import requests
import subprocess
import sys

# Initialisation de colorama
colorama.init()

def install_dependencies():
    dependencies = ["requests", "colorama"]
    for dep in dependencies:
        try:
            __import__(dep)
        except ImportError:
            print(f"{dep} not found. Installing...")
            subprocess.call([sys.executable, "-m", "pip", "install", dep])

def is_termux():
    return 'TERMUX_VERSION' in os.environ

def is_kali():
    return 'KALI_VERSION' in os.environ

def load_malicious_links():
    try:
        with open(get_malicious_links_path(), 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def load_malware_signatures():
    try:
        with open(get_malware_signatures_path(), 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + """
     ____   ____    ___   _____  _____   ____  _____         _  __ ___  _____  
|  _ \ |  _ \  / _ \ |_   _|| ____| / ___||_   _|       | |/ /|_ _||_   _| 
| |_) || |_) || | | |  | |  |  _|  | |      | |   _____ | ' /  | |   | |   
|  __/ |  _ < | |_| |  | |  | |___ | |___   | |  |_____|| . \  | |   | |   
|_|    |_| \_\ \___/   |_|  |_____| \____|  |_|         |_|\_\|___|  |_|   
                                                                           

    """ + Style.RESET_ALL)
    print(Fore.YELLOW + get_translation("welcome_message") + Style.RESET_ALL)
    print(Fore.BLUE + "1. " + get_translation("scan_url") + Style.RESET_ALL)
    print(Fore.GREEN + "2. " + get_translation("scan_apk") + Style.RESET_ALL)
    print(Fore.MAGENTA + "3. " + get_translation("scan_file") + Style.RESET_ALL)
    print(Fore.YELLOW + "4. " + get_translation("info") + Style.RESET_ALL)
    print(Fore.GREEN + "5. " + get_translation("change_language") + Style.RESET_ALL)
    print(Fore.RED + "6. " + get_translation("exit") + Style.RESET_ALL)
    print(Fore.MAGENTA + "7. " + get_translation("update_script") + Style.RESET_ALL)

def show_info():
    print(Fore.YELLOW + "DEDSEC-PROTECT-KIT v1.0" + Style.RESET_ALL)
    print(Fore.YELLOW + get_translation("developed_by") + Style.RESET_ALL)
    print(Fore.YELLOW + get_translation("contact") + Style.RESET_ALL)
    print(Fore.YELLOW + get_translation("thanks_for_using") + Style.RESET_ALL) 
    print(Fore.RED + get_translation("send_malicious_links") + Style.RESET_ALL)
    input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)  # Ajout de la pause

def update_script():
    repo_url = "https://api.github.com/repos/Famous-Tech/PROTECT-KIT/commits"
    try:
        response = requests.get(repo_url)
        if response.status_code == 200:
            latest_commit = response.json()[0]['sha']
            local_commit = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
            if latest_commit != local_commit:
                print(Fore.MAGENTA + "Update available! Downloading..." + Style.RESET_ALL)
                subprocess.call(["git", "pull"])
                print(Fore.MAGENTA + "Update completed successfully!" + Style.RESET_ALL)
            else:
                print(Fore.MAGENTA + "No updates available." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Error checking for updates." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error updating script: {e}" + Style.RESET_ALL)
    input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)  # Ajout de la pause

def install_apktool():
    if is_termux():
        subprocess.call(["pkg", "install", "apktool"])
    elif is_kali():
        subprocess.call(["sudo", "apt-get", "install", "apktool"])

def main():
    install_dependencies()
    install_apktool()
    malicious_links = load_malicious_links()
    while True:
        display_menu()
        choice = input(Fore.BLUE + get_translation("choose_option") + Style.RESET_ALL)
        if choice == '1':
            url = input(Fore.GREEN + get_translation("enter_link") + Style.RESET_ALL)
            result = check_link(url, malicious_links)
            print(result)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)  # Ajout de la pause
        elif choice == '2':
            apk_path = input(Fore.GREEN + get_translation("enter_apk_path") + Style.RESET_ALL)
            result = check_apk(apk_path)
            print(result)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)  # Ajout de la pause
        elif choice == '3':
            file_path = input(Fore.GREEN + get_translation("enter_file_path") + Style.RESET_ALL)
            result = check_file(file_path)
            print(result)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)  # Ajout de la pause
        elif choice == '4':
            show_info()
        elif choice == '5':
            lang = input(Fore.GREEN + get_translation("enter_language") + Style.RESET_ALL)
            set_language(lang)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)  # Ajout de la pause
        elif choice == '6':
            print(Fore.YELLOW + get_translation("goodbye_message") + Style.RESET_ALL)
            break
        elif choice == '7':
            update_script()
        else:
            print(Fore.RED + get_translation("invalid_option") + Style.RESET_ALL)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)  # Ajout de la pause

if __name__ == "__main__":
    main()
