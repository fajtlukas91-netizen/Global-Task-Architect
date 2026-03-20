# 🏗️ ARCHITECT | Terminal Management System (v10.0)

**ARCHITECT** is a high-performance, minimalist project management and deadline tracking engine designed for modern terminal environments. It merges 80s industrial aesthetics with robust data processing logic.

![Version](https://img.shields.io/badge/Version-10.0_Ultra-ffcc00?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge)
![UI](https://img.shields.io/badge/UI-Deep_Amber-333333?style=for-the-badge)

---

## 💎 Project Philosophy
ARCHITECT was engineered to eliminate the distractions of modern GUIs. It prioritizes clean output, rapid data entry, and immediate visual feedback. All processes are optimized for linear flow, ensuring a stable display without flickering or unnecessary screen clearing.

## 🔥 Key Features

### 🎨 High-Contrast Alert System
A unique color-coded notification system built on a **Deep Amber** foundation, featuring aggressive signaling for critical tasks:
* 🟧 **Amber:** Standard operational mode and system logs.
* 🟪 **Magenta:** Critical Warning (Deadline within 3 days). Designed for maximum visual contrast against the amber base.
* 🟥 **Bold Red:** Expired records requiring immediate operator intervention.

### 🛡️ Persistent Security & Profiles
* **Decentralized Data:** Each operator manages an isolated database stored in a secure JSON structure.
* **Access Key Protection:** Authentication secured via a Reverse-Key logic verification.
* **Fault Tolerance:** Robust exception handling (Try-Except Shield) prevents system crashes during invalid date inputs.

### ⚡ Stationary UI Logic
Unlike standard scripts, ARCHITECT utilizes **Single-Header Logic**. The ASCII logo remains static at the top of the session, while action history and analysis flow naturally below it, ensuring professional readability.

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)[YOUR-USERNAME]/architect-system.git
   cd architect-system
Launch System:

Bash
python architect.py
🛠️ Operational Protocols
[1] NEW PROJECT: Initialize a new record. Requires a project name and a deadline (DD.MM.YYYY). Leaving the deadline empty defaults to NONE.

[2] DATABASE: Interactive project browser. Allows for immediate record termination (deletion) by entering the specific ID.

[Q] LOGOUT: Securely disconnects the session, finalizes the JSON write-cycle, and terminates the process.

📂 Data Architecture
/architect_users: Local storage for operator profiles and task encrypted-ready structures.

/plans: Reserved directory for future export modules and system reports.

👨‍💻 Development
Lead Developer: Lukas Fajt - Netizen

Core Engine: ARCHITECT Ultra Framework v10.0

SYSTEM_STATUS: > "Data in motion. Deadlines under control. System ARCHITECT."
