# 🏗️ ARCHITECT - Task Management System v8.0 [SECURITY]

![Architect Demo](github%20demo.png)

**Advanced Task Management System with Retro Amber UI, Secure Access Control, and Automated Reporting.**

ARCHITECT je terminálový nástroj pro precizní plánování úkolů, navržený s důrazem na estetiku 80. let (Amber Terminal) a efektivitu moderních vývojářských workflow. Od verze 8.0 obsahuje plnohodnotný systém správy uživatelů a zabezpečení.

---

### 🛡️ Novinky ve verzi 8.0:
* **Security Core:** Integrovaný přihlašovací systém pro více operátorů.
* **Encrypted Keys:** Hesla nejsou ukládána v čistém textu (Simple Masking v8).
* **Hidden Input:** Real-time maskování hesla v konzoli pomocí knihovny `getpass`.
* **User Profiles:** Individuální sledování statistik (počet vytvořených plánů) pro každého uživatele.
* **Hacker Boot Sequence:** Nová startovací sekvence s kontrolou integrity systému.

### 🚀 Hlavní funkce:
* **Retro UI:** Jantarové barevné schéma pro minimální únavu očí.
* **Automated Reporting:** Generování profesionálních `.txt` reportů s ASCII tabulkami.
* **Smart Integration:** Automatická detekce a otevírání reportů v **Notepad++** (nebo systémovém editoru).
* **Persistent Storage:** Data uživatelů a plány jsou bezpečně ukládány do JSON a TXT struktury.

---

### 🛠️ Jak začít:
1. Spusťte hlavní skript: `python architect_v8.py`
2. **Autorizace:** Zadejte své ID operátora (noví uživatelé si při prvním spuštění nastaví svůj přístupový klíč).
3. **Příkazy:**
    * `[1]` - Spustí průvodce vytvořením nového projektu.
    * `[2]` - Bezpečné odhlášení ze systému.

### 📁 Struktura složek:
* `/architect_users` - Šifrované profily operátorů (JSON).
* `/plans` - Archivované akční plány (TXT).

---

> **Status:** STABLE RELEASE v8.0_SECURITY  
> **Environment:** Python 3.x | Windows Terminal Recommended
