# Global Task Architect v7.02 🏗️

A professional Python-based CLI tool designed for structured task planning, automated data management, and activity logging.

## 🚀 Key Features
- **Multi-format Export:** Generates both `.txt` (human-readable) and `.csv` (data-ready) action plans.
- **Automated Backup System:** Creates safety backups of existing task data upon startup.
- **Activity Logging:** Maintains a detailed `architect_history.log` with absolute file paths for easy retrieval.
- **Matrix-style UI:** Enhanced command-line interface with boot sequences and color-coded feedback.
- **Cross-platform:** Compatible with Windows, Linux, and macOS.

## 🛠️ Technical Details
- **Language:** Python 3.x
- **Libraries used:** `os`, `csv`, `shutil`, `datetime`, `sys`, `time`
- **Architecture:** Modular function-based design with an infinite execution loop.

## 📖 How to use
1. Run the script: `python architect.py`
2. Follow the on-screen boot sequence.
3. Enter your **User Name**, **Primary Goal**, and **Tasks** (separated by commas).
4. Find your generated plans in the `/plans` directory and check your history in `architect_history.log`.

## 📝 Version History
- **v7.02:** Full English localization, absolute path logging, and UI optimization. (Current)
- **v7.01:** Added backup system and CSV export.
- **v1.00:** Initial release (basic task input).

---
*Developed as part of a self-taught Python journey.*
