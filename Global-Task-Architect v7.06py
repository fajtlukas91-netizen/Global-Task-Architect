import csv
import os
import shutil
import time
import sys
import json
import subprocess
import random
from datetime import datetime

# =================================================================
# --- MOTIV: AMBER (Jantarová) - STABLE v7.06 ---
# =================================================================
P = "\033[33m"       # Jantarová (Základní text)
A = "\033[93m"       # Jasně žlutá (Důležité info)
S = "\033[90m"       # Šedá (Rámečky a linky)
BOLD = "\033[1m"
END = "\033[0m"

# --- CONFIG ---
USER_DATA_DIR = "architect_users"
PLANS_DIR = "plans"
VERSION = "7.06_AMBER_REALTIME"

for folder in [USER_DATA_DIR, PLANS_DIR]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# --- VISUAL FUNCTIONS ---

def show_loading_bar(task_name):
    print(f"{S}{task_name:<25}", end="")
    for i in range(21):
        percent = i * 5
        bar = "█" * i + "░" * (20 - i)
        sys.stdout.write(f"\r{S}{task_name:<25} [{P}{bar}{S}] {percent}%")
        sys.stdout.flush()
        time.sleep(random.uniform(0.01, 0.03))
    print(f" {A}[ OK ]{END}")

def show_hacker_boot():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{P}")
    print(r"  █████╗ ██████╗  ██████╗██╗  ██╗██╗████████╗███████╗ ██████╗████████╗")
    print(r" ██╔══██╗██╔══██╗██╔════╝██║  ██║██║╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝")
    print(r" ███████║██████╔╝██║     ███████║██║   ██║   █████╗  ██║        ██║   ")
    print(r" ██╔══██║██╔══██╗██║     ██╔══██║██║   ██║   ██╔══╝  ██║        ██║   ")
    print(r" ██║  ██║██║  ██║╚██████╗██║  ██║██║   ██║   ███████╗╚██████╗   ██║   ")
    print(r" ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   ")
    print(f"{END}")
    time.sleep(0.3)
    show_loading_bar("LOAD_SYSTEM_KERNEL")
    show_loading_bar("SYNC_OPERATOR_JSON")
    show_loading_bar("NOTEPAD_LINK_CHECK")

def show_status_bar(user_data):
    """Aktualizuje čas při každém zobrazení menu."""
    now = datetime.now().strftime("%H:%M:%S")
    border = f"{S}║{END}"
    
    # Obsah lišty - nyní s aktuálním časem systému
    content = f" {BOLD}OP:{END} {A}{user_data['name'].upper():<10}{END} {S}|{END} {BOLD}STATS:{END} {P}{user_data['total_plans']:<4}{END} {S}|{END} {BOLD}SYSTEM_TIME:{END} {A}{now:<8}{END} "
    
    print(f"{S}╔" + "═"*(len(content)-20) + "╗")
    print(f"{border}{content}{border}")
    print(f"{S}╚" + "═"*(len(content)-20) + "╝{END}")

def open_with_pro_editor(file_path):
    npp_path = r"C:\Program Files\Notepad++\notepad++.exe"
    abs_p = os.path.abspath(file_path)
    if os.path.exists(npp_path):
        subprocess.Popen([npp_path, abs_p])
    else:
        os.startfile(abs_p)

# --- LOGIC ---

def get_user_profile(name):
    file_path = os.path.join(USER_DATA_DIR, f"{name.lower()}.json")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"name": name, "total_plans": 0}

def save_user_profile(name, data):
    file_path = os.path.join(USER_DATA_DIR, f"{name.lower()}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def create_action_plan(user_data, goal, steps, date):
    current_time = datetime.now()
    file_timestamp = current_time.strftime("%H%M%S")
    txt_file = os.path.join(PLANS_DIR, f"plan_{user_data['name'].lower()}_{file_timestamp}.txt")

    with open(txt_file, "w", encoding="utf-8") as f:
        f.write("╔" + "═"*60 + "╗\n")
        f.write(f"║ ARCHITECT REPORT - AMBER EDITION{' ':>26}║\n")
        f.write("╠" + "═"*60 + "╣\n")
        f.write(f"║ OP: {user_data['name'].upper():<54}║\n")
        f.write(f"║ DATE: {current_time.strftime('%Y-%m-%d %H:%M'):<48}║\n")
        f.write(f"║ DEADLINE: {date:<48}║\n")
        f.write("╠" + "═"*60 + "╣\n")
        f.write(f"║ GOAL: {goal.upper():<52}║\n")
        f.write("╟" + "─"*60 + "╢\n")
        for i, s in enumerate(steps, 1):
            f.write(f"║ [{i:02}] [ ] {s:<47}║\n")
        f.write("╚" + "═"*60 + "╝\n")

    user_data["total_plans"] += 1
    save_user_profile(user_data["name"], user_data)
    print(f"\n{A}>>> DATA_ARCHIVED_SUCCESSFULLY{END}")
    open_with_pro_editor(txt_file)

# --- START ---
show_hacker_boot()
name = input(f"\n{S}IDENTIFY_OPERATOR > {END}{BOLD}{P}")
user_data = get_user_profile(name)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    show_status_bar(user_data) # Tady se čas pokaždé obnoví
    
    print(f"\n{P}COMMAND_MENU:{END}")
    print(f"[{A}1{END}] NEW_PROJECT")
    print(f"[{A}2{END}] LOG_OFF")
    
    # Tento input sice zastaví čas, ale hned po akci se čas v liště "skočí" na aktuální
    cmd = input(f"\n{S}SYSTEM@CONSOLE > {END}").strip()

    if cmd == '2': break
    elif cmd == '1':
        g = input(f"{P}GOAL: {END}")
        d = input(f"{P}DATE: {END}")
        steps = []
        print(f"{P}TASKS (Empty to end):{END}")
        while True:
            s = input(f"{S}  > {END}")
            if not s: break
            steps.append(s)
        if steps:
            create_action_plan(user_data, g, steps, d)
            input(f"\n{S}Press Enter to sync and return...{END}")
