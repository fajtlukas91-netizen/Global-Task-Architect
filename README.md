# 🏗️ ARCHITECT - Task Management System [v8.0 SECURITY]

![Architect Demo](github%20demo.png)

### ⚙️ SYSTEM_CORE_SPECIFICATIONS
ARCHITECT je terminálový engine pro precizní plánování úkolů a správu projektů. Navržen pro maximální efektivitu v příkazové řádce (CLI) s důrazem na Amber Terminal estetiku a automatizovaný reporting.

---

### 🛡️ SECURITY_LAYER [NEW_IN_v8.0]
Verze 8.0 přináší kompletní přepracování přístupových práv a ochranu uživatelských dat:
* **AUTHORIZATION_GATE:** Systém vyžaduje validní OPERATOR ID pro přístup do hlavního menu.
* **ACCESS_KEY_ENCRYPTION:** Implementace Simple Masking algoritmu. Hesla nejsou v JSON databázi čitelná (v8.01_SEC).
* **HIDDEN_INPUT_PROTOCOL:** Využití knihovny `getpass` pro maskování vstupu hesla v reálném čase.
* **INDIVIDUAL_PROFILES:** Každý operátor má vlastní JSON profil se statistikami (Total Plans) a unikátním klíčem.

---

### 🎨 VISUAL_SPECIFICATIONS (AMBER_MONITOR)
Systém simuluje vzhled jantarových monitorů z 80. let pomocí ANSI kódování:
* `\033[33m` - **AMBER_PRIMARY** (Standardní text a UI prvky)
* `\033[93m` - **AMBER_HIGHLIGHT** (Důležité systémové stavy a potvrzení)
* `\033[90m` - **GRAY_FRAME** (Rámečky, linky a cesty k souborům)
* `\033[91m` - **SECURITY_ALERT** (Zamítnutí přístupu, kritické chyby)

---

### 🚀 CORE_LOGIC_&_INTEGRATION
* **AUTOMATED_REPORTING:** Generování `.txt` reportů s precizní ASCII hlavičkou a očíslovanými úkoly.
* **NOTEPAD++_LINK:** Automatická detekce cesty `C:\Program Files\Notepad++\notepad++.exe`. Okamžité otevření vygenerovaného plánu po archivaci.
* **BOOT_PROTOCOL:** Startovací sekvence s kontrolou integrity jádra a načítáním bezpečnostních modulů.
* **DATA_PERSISTENCE:** * `/plans/` - Úložiště akčních plánů (formát TXT).
    * `/architect_users/` - Zabezpečená databáze operátorů (formát JSON).

---

### 🛠️ OPERATION_GUIDE
1. **START:** Spusťte `architect_v8.py`.
2. **IDENT:** Zadejte své OPERATOR ID (pro nové uživatele se spustí REG_PROTOCOL).
3. **SECURE:** Definujte svůj Access Key (vstup je skrytý).
4. **EXECUTE:** V menu zvolte `[1]` pro zahájení NEW_PROJECT_WIZARD.

---

### 📂 DIRECTORY_TREE
```text
/
├── architect_v8.py          # Hlavní systémový skript
├── github demo.png          # Vizuální dokumentace
├── plans/                   # Výstupní složka reportů (.txt)
└── architect_users/         # Databáze profilů a hesel (.json)
