translations = {
    "en": {
        "welcome_message": "Welcome to DEDSEC-PROTECT-KIT",
        "scan_url": "Scan an URL",
        "info": "INFO",
        "change_language": "Change language",
        "exit": "Exit",
        "update_script": "Update the script",
        "choose_option": "Choose an option: ",
        "enter_link": "Enter the link to check: ",
        "enter_language": "Enter the language (en/fr/ht): ",
        "goodbye_message": "Goodbye!",
        "invalid_option": "Invalid option, please try again.",
        "developed_by": "Developed by: FAMOUS-TECH | ʜᴀᴄᴋᴇʀ₁₆₀₉",
        "contact": "Contact: +1 (409) 995-3525 whattsapp only",
        "thanks_for_using": "THANKS FOR USING THIS SCRIPT",
        "send_malicious_links": "send me all malicious link you know pls i need to create a big database. bye!",
        "malicious_link_detected": "Malicious link detected!",
        "safe_link": "Safe link.",
        "link_not_found": "Link not found in VirusTotal database.",
        "error_connecting": "Error connecting to VirusTotal.",
        "suspicious_domain_detected": "Suspicious domain detected! Similar to {}",
        "known_malicious_link": "Malicious link detected! (Known malicious link)"
    },
    "fr": {
        "welcome_message": "Bienvenue dans DEDSEC-PROTECT-KIT",
        "scan_url": "Scanner une URL",
        "info": "INFO",
        "change_language": "Changer la langue",
        "exit": "Quitter",
        "update_script": "Mettre à jour le script",
        "choose_option": "Choisissez une option: ",
        "enter_link": "Entrez le lien à vérifier: ",
        "enter_language": "Entrez la langue (en/fr/ht): ",
        "goodbye_message": "Au revoir!",
        "invalid_option": "Option invalide, veuillez réessayer.",
        "developed_by": "Développé par: FAMOUS-TECH | ʜᴀᴄᴋᴇʀ₁₆₀₉",
        "contact": "Contact: +1 (409) 995-3525 whattsapp only",
        "thanks_for_using": "MERCI D'UTILISER CE SCRIPT",
        "send_malicious_links": "envoyez-moi tous les liens malveillants que vous connaissez s'il vous plaît, j'ai besoin de créer une grande base de données. au revoir!",
        "malicious_link_detected": "Lien malveillant détecté!",
        "safe_link": "Lien sûr.",
        "link_not_found": "Lien non trouvé dans la base de données VirusTotal.",
        "error_connecting": "Erreur de connexion à VirusTotal.",
        "suspicious_domain_detected": "Domaine suspect détecté! Similaire à {}",
        "known_malicious_link": "Lien malveillant détecté! (Lien malveillant connu)"
    },
    "ht": {
        "welcome_message": "Byenveni nan DEDSEC-PROTECT-KIT",
        "scan_url": "Tcheke yon URL",
        "info": "INFO",
        "change_language": "Chanje lang (en,fr,)",
        "exit": "Sòti",
        "update_script": "Mete  script la ajou",
        "choose_option": "Chwazi yon opsyon: ",
        "enter_link": "Antre lyen wap tcheke an la: ",
        "enter_language": "Antre lang (en/fr/ht): ",
        "goodbye_message": "babay ",
        "invalid_option": "Opsyon invalid, tanpri eseye ankò.",
        "developed_by": "Devlope pa: FAMOUS-TECH | ʜᴀᴄᴋᴇʀ₁₆₀₉",
        "contact": "Kontak: +1 (409) 995-3525 whattsapp sèlman",
        "thanks_for_using": "Mèsi dèske w itilize script sa",
        "send_malicious_links": "zanmi m voye  tout lyen danje(fake) ou konnen tanpri mwen bezwen kreye yon gwo baz done pou script sa ka pi pwisan. bye!",
        "malicious_link_detected": "Lyen malizyè detekte!",
        "safe_link": "Lyen sekirize.",
        "link_not_found": "Lyen pa jwenn nan baz done VirusTotal.",
        "error_connecting": "Erè nan koneksyon ak VirusTotal la.",
        "suspicious_domain_detected": "fek sit yo chanje non an pou n ka pran ladan l ! Menm jan ak {}",
        "known_malicious_link": "Lyen malizyè detekte! (Lyen malizyè konnen)"
    }
}

current_language = "en"

def set_language(lang):
    global current_language
    if lang in translations:
        current_language = lang

def get_translation(key):
    return translations[current_language].get(key, "Translation not found")
