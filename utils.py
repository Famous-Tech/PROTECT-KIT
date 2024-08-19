import os

def get_malware_signatures_path():
    if 'TERMUX_VERSION' in os.environ:
        return "/data/data/com.termux/files/home/malware_signatures.json"
    elif 'KALI_VERSION' in os.environ:
        return "/home/kali/malware_signatures.json"
    else:
        return "malware_signatures.json"

def get_malicious_links_path():
    if 'TERMUX_VERSION' in os.environ:
        return "/data/data/com.termux/files/home/malicious.json"
    elif 'KALI_VERSION' in os.environ:
        return "/home/kali/malicious.json"
    else:
        return "malicious.json"
