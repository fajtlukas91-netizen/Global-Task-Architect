# 🏗️ ARCHITECT - Task Management System v7.06

![Theme: Amber](https://img.shields.io/badge/UI_Theme-Amber_Industrial-orange)
![Python: 3.x](https://img.shields.io/badge/Python-3.x-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

**ARCHITECT** je terminálový nástroj pro precizní plánování úkolů a projektů. Vytvořen s důrazem na vizuální estetiku retro terminálů (Amber Edition) a efektivní workflow.

## 🚀 Klíčové vlastnosti (v7.06)

* **Amber Industrial UI:** Přehledné rozhraní v jantarových tónech, které šetří zrak.
* **Real-time Status Bar:** Horní lišta s dynamickou aktualizací času, jména operátora a statistik.
* **Sequential Task Entry:** Intuitivní zadávání úkolů jeden po druhém místo složitého psaní čárek.
* **Profi Export:** Automatické generování `.txt` plánů s ASCII ohraničením.
* **Smart Editor Link:** Program automaticky detekuje **Notepad++** pro nejlepší zobrazení, jinak použije systémový WordPad.
* **User Persistence:** Každý operátor má svůj vlastní profil uložený v `JSON` formátu.

## 🛠️ Instalace a spuštění

1.  Ujistěte se, že máte nainstalovaný **Python 3.x**.
2.  Stáhněte si tento repozitář.
3.  Pro nejlepší vizuální zážitek doporučujeme nainstalovat [Notepad++](https://notepad-plus-plus.org/).
4.  Spusťte program příkazem:
    ```bash
    python architect.py
    ```

## 📂 Struktura složek

Program si automaticky vytváří následující hierarchii:
* `/plans`: Zde naleznete vygenerované akční plány.
* `/architect_users`: Databáze uživatelských profilů a statistik.

## 📜 Verze 7.06 Changelog
- Implementováno jantarové barevné schéma (Amber Edition).
- Přidána sekvenční smyčka pro zadávání úkolů.
- Opraveno přetékání textu v ASCII tabulkách.
- Přidána dynamická synchronizace času v menu.

---
*Developed by [Tvé Jméno/Přezdívka] - 2024*
