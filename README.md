# 🌐 Global Task Architect v7.0 (The Architect Edition)

### 🚀 Evolution from v1.0 to v7.0
Tento projekt prošel brutální evolucí. Od jednoduchého generátoru úkolů jsme se dostali k robustnímu systému s ochranou dat, vizuální identitou a uživatelským manuálem.

---

## 🛠️ New Features in v7.0
* **Matrix Boot Sequence:** Implementováno dynamické načítání systému (`matrix_print`) pro autentický hackerský pocit.
* **Architect Manual:** Integrovaný systémový pomocník. Stačí napsat `help` v terminálu.
* **Data Validation:** Program je nyní neprůstřelný. Ošetřuje prázdné vstupy a náhodné mezery (`.strip()`).
* **System Commands:** Přidána podpora pro příkazy `help` a `exit` přímo v hlavní smyčce.
* **Automated Backup Engine:** Každé spuštění automaticky zálohuje stávající databázi úkolů do složky `/backups` s časovým razítkem.
* **Multi-Format Export:** Generuje přehledné `.txt` pro lidi a strukturované `.csv` pro stroje.

---

## 💻 Tech Stack
* **Language:** Python 3.x
* **Libraries:** `os`, `csv`, `shutil`, `datetime`, `time`, `sys`
* **UI:** ANSI Escape Sequences (Matrix Green Theme)

---

## 📖 How to Use (System Guide)
1. **Launch:** Spusťte `main.py` a sledujte bootovací sekvenci.
2. **Commands:**
    * `help` - Zobrazí manuál pro správné zadávání dat.
    * `exit` - Bezpečně ukončí systém.
3. **Input:** Zadejte jméno, cíl a sekvenci úkolů oddělenou čárkou.
4. **Result:** Systém okamžitě vygeneruje soubory a otevře ten hlavní pro kontrolu.

---

## 🛡️ Data Safety
Všechny plány jsou automaticky verzovány. Pokud omylem přepíšete důležitý soubor, najdete jeho kopii v adresáři `backups/`.

---

> **Developer Note:**
> *"Build. Secure. Automate. Repeat."*
> Aktuálně pracujeme na verzi **v7.01**, která přinese ještě inteligentnější zpracování dat.
