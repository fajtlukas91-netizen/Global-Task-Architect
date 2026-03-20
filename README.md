# 🏗️ ARCHITECT | Terminal Management System (v9.05)

**ARCHITECT** je výkonný, minimalistický nástroj pro správu projektů a sledování deadlinů běžící přímo v terminálu. Je navržen pro uživatele, kteří vyžadují **čistý kód**, **industriální estetiku** a **maximální přehlednost** bez zbytečného vizuálního šumu.

![Version](https://img.shields.io/badge/Version-9.05_Ultra-ffcc00?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge)
![UI](https://img.shields.io/badge/UI-Deep_Amber-333333?style=for-the-badge)

---

## 💎 Filozofie projektu
ARCHITECT byl vytvořen s cílem eliminovat rozptylování běžných grafických aplikací. Zaměřuje se na čistotu výstupu, rychlost zápisu a okamžitou vizuální odezvu. Všechny procesy jsou optimalizovány pro lineární plynulost bez rušivého problikávání obrazovky.

## 🔥 Klíčové vlastnosti

### 🎨 High-Contrast Alert System
Unikátní barevné schéma postavené na **Deep Amber** (jantarové) paletě, doplněné o agresivní signalizaci kritických stavů:
* 🟧 **Jantarová:** Standardní operační režim a systémové výpisy.
* 🟪 **Magenta (Fialová):** Kritické varování (Termín vyprší do 3 dnů). Navrženo pro maximální barevný kontrast k základnímu schématu.
* 🟥 **Bold Red (Tučná červená):** Expirované záznamy vyžadující okamžitou pozornost operátora.

### 🛡️ Persistent Security & Profiles
* **Decentralizovaná data:** Každý operátor spravuje vlastní izolovanou databázi v zabezpečeném formátu JSON.
* **Access Key Protection:** Přístup je chráněn algoritmem zpětné verifikace klíče (Reverse-Key Logic).
* **Fault Tolerance:** Robustní ošetření vstupů (try-except shield) zabraňující pádu aplikace při zadání nevalidních datových formátů.

### ⚡ Stationary UI Logic
Na rozdíl od běžných terminálových skriptů ARCHITECT využívá **Single-Header Logic**. Logo zůstává staticky na vrcholu relace, zatímco historie akcí a analýzy plynule přibývají pod ním. To zajišťuje přirozenou čitelnost a stabilitu zobrazení.

---

## 🚀 Instalace

1. **Klonování repozitáře:**
   ```bash
   git clone [https://github.com/](https://github.com/)[TVOJE-UZIVATELSKE-JMENO]/architect-system.git
   cd architect-system
Spuštění:

Bash
python architect.py
🛠️ Ovládací protokoly
[1] NOVÝ: Inicializace nového záznamu. Vyžaduje název projektu a termín ve formátu DD.MM.YYYY.

[2] DATABÁZE: Interaktivní prohlížeč všech záznamů s funkcí okamžité terminace (smazání) úkolu zadáním jeho ID.

[Q] ODHLÁSIT: Bezpečné ukončení relace, finalizace zápisu do JSON a odpojení od systému.

📂 Datová architektura
/architect_users: Úložiště uživatelských profilů a jejich specifických úkolů.

/plans: Vyhrazený prostor pro exporty a systémové reporty.

👨‍💻 Vývojový tým
Lead Developer: [Lukáš Fajt - Netizen]
Core Engine: ARCHITECT Ultra Framework v10.0

SYSTEM_STATUS: > "Data v pohybu. Termíny pod kontrolou. Systém ARCHITECT."
