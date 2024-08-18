import os
import colorama
from colorama import Fore, Style
from languages import set_language, get_translation
from scanner import check_link
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

def get_malicious_links_path():
    if is_termux():
        return "/data/data/com.termux/files/home/malicious.json"
    elif is_kali():
        return "/home/kali/malicious.json"
    else:
        return "malicious.json"

def load_malicious_links():
    try:
        with open(get_malicious_links_path(), 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + """
:::::::::       :::::::::       ::::::::   :::::::::::       ::::::::::       ::::::::   :::::::::::                          :::    :::       :::::::::::   :::::::::::  
 :+:    :+:      :+:    :+:     :+:    :+:      :+:           :+:             :+:    :+:      :+:                              :+:   :+:            :+:           :+:       
+:+    +:+      +:+    +:+     +:+    +:+      +:+           +:+             +:+             +:+                              +:+  +:+             +:+           +:+        
+#++:++#+       +#++:++#:      +#+    +:+      +#+           +#++:++#        +#+             +#+           +#++:++#++:++      +#++:++              +#+           +#+         
+#+             +#+    +#+     +#+    +#+      +#+           +#+             +#+             +#+                              +#+  +#+             +#+           +#+          
#+#             #+#    #+#     #+#    #+#      #+#           #+#             #+#    #+#      #+#                              #+#   #+#            #+#           #+#           
###             ###    ###      ########       ###           ##########       ########       ###                              ###    ###       ###########       ###
    """ + Style.RESET_ALL)
    print(Fore.YELLOW + get_translation("welcome_message") + Style.RESET_ALL)
    print(Fore.BLUE + "1. " + get_translation("scan_url") + Style.RESET_ALL)
    print(Fore.YELLOW + "2. " + get_translation("info") + Style.RESET_ALL)
    print(Fore.GREEN + "3. " + get_translation("change_language") + Style.RESET_ALL)
    print(Fore.RED + "4. " + get_translation("exit") + Style.RESET_ALL)
    print(Fore.MAGENTA + "5. " + get_translation("update_script") + Style.RESET_ALL)

def show_info():
    print(Fore.YELLOW + "DEDSEC-PROTECT-KIT v1.0" + Style.RESET_ALL)
    print(Fore.YELLOW + get_translation("developed_by") + Style.RESET_ALL)
    print(Fore.YELLOW + get_translation("contact") + Style.RESET_ALL)
    print(Fore.YELLOW + get_translation("thanks_for_using") + Style.RESET_ALL) 
    print(Fore.RED + get_translation("send_malicious_links") + Style.RESET_ALL)

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

def main():
    install_dependencies()
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
            show_info()
        elif choice == '3':
            lang = input(Fore.GREEN + get_translation("enter_language") + Style.RESET_ALL)
            set_language(lang)
        elif choice == '4':
            print(Fore.YELLOW + get_translation("goodbye_message") + Style.RESET_ALL)
            break
        elif choice == '5':
            update_script()
        else:
            print(Fore.RED + get_translation("invalid_option") + Style.RESET_ALL)

if __name__ == "__main__":
    main()
