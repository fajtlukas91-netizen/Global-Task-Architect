import csv
import os
import shutil
import time
import sys
import json
import subprocess
import random
import getpass
from datetime import datetime

# =================================================================
# --- MOTIV: AMBER (Jantarová) - STABLE v8.0 ---
# =================================================================
P = "\033[33m"       # Jantarová
A = "\033[93m"       # Jasně žlutá
S = "\033[90m"       # Šedá
BOLD = "\033[1m"
RED = "\033[91m"
END = "\033[0m"

USER_DATA_DIR = "architect_users"
PLANS_DIR = "plans"
VERSION = "8.0_SECURITY"

for folder in [USER_DATA_DIR, PLANS_DIR]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# --- SECURITY ENGINE ---

def simple_mask(password):
    masked = ""
    for char in password:
        masked += chr(ord(char) + 2)
    return masked

def get_user_profile(name):
    file_path = os.path.join(USER_DATA_DIR, f"{name.lower()}.json")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_user_profile(name, data):
    file_path = os.path.join(USER_DATA_DIR, f"{name.lower()}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# --- VISUALS ---

def matrix_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char); sys.stdout.flush(); time.sleep(delay)
    print()

def show_loading_bar(task_name):
    print(f"{S}{task_name:<25}", end="")
    for i in range(21):
        percent = i * 5
        bar = "█" * i + "░" * (20 - i)
        sys.stdout.write(f"\r{S}{task_name:<25} [{P}{bar}{S}] {percent}%")
        sys.stdout.flush(); time.sleep(random.uniform(0.01, 0.03))
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
    show_loading_bar("LOAD_SECURITY_MODULE")
    show_loading_bar("NOTEPAD_LINK_CHECK")

def show_status_bar(user_data):
    now = datetime.now().strftime("%H:%M:%S")
    border = f"{S}║{END}"
    content = f" {BOLD}OP:{END} {A}{user_data['name'].upper():<10}{END} {S}|{END} {BOLD}STATS:{END} {P}{user_data['total_plans']:<4}{END} {S}|{END} {BOLD}SYSTEM_TIME:{END} {A}{now:<8}{END} {S}| SECURED{END} "
    print(f"{S}╔" + "═"*(len(content)-29) + "╗")
    print(f"{border}{content}{border}")
    print(f"{S}╚" + "═"*(len(content)-29) + "╝{END}")

# --- ACCESS CONTROL ---

def security_access_control():
    show_hacker_boot()
    print(f"\n{S}AUTHORIZATION_REQUIRED{END}")
    name = input(f"{BOLD}OPERATOR ID > {END}{P}").strip()
    if not name: sys.exit()
    user_data = get_user_profile(name)

    if user_data is None:
        matrix_print(f"\n{A}>>> NEW_OPERATOR_DETECTED: {name.upper()}{END}")
        pw1 = getpass.getpass(f"{S}SET ACCESS KEY (hidden)    > {END}")
        pw2 = getpass.getpass(f"{S}CONFIRM ACCESS KEY (hidden) > {END}")
        if pw1 == pw2 and pw1 != "":
            user_data = {"name": name, "total_plans": 0, "access_key": simple_mask(pw1)}
            save_user_profile(name, user_data)
            matrix_print(f"\n{A}>>> SECURITY_PROFILE_CREATED_AND_SECURED{END}")
            time.sleep(1); return user_data
        else:
            print(f"\n{RED}### ERROR: KEYS_DO_NOT_MATCH ###{END}"); time.sleep(2); sys.exit()
    else:
        matrix_print(f"\n{P}>>> ACCESSING_PROFILE: {name.upper()}{END}")
        input_pass = getpass.getpass(f"{S}ENTER ACCESS KEY (hidden) > {END}")
        if simple_mask(input_pass) == user_data['access_key']:
            matrix_print(f"{A}>>> ACCESS_GRANTED_OPERATOR_{name.upper()}{END}"); time.sleep(1); return user_data
        else:
            print(f"\n{RED}### SECURITY_ALERT: ACCESS_DENIED ###{END}"); time.sleep(2); sys.exit()

# --- LOGIC ---

def open_with_pro_editor(file_path):
    npp_path = r"C:\Program Files\Notepad++\notepad++.exe"
    abs_p = os.path.abspath(file_path)
    if os.name == 'nt' and os.path.exists(npp_path):
        subprocess.Popen([npp_path, abs_p])
    else:
        if hasattr(os, 'startfile'): os.startfile(abs_p)

def create_action_plan(user_data):
    os.system('cls' if os.name == 'nt' else 'clear')
    show_status_bar(user_data)
    print(f"\n{BOLD}{A}--- [NEW_PROJECT_WIZARD] ---{END}\n")
    g = input(f"{P}ENTER PROJECT GOAL: {END}")
    d = input(f"{P}SET DEADLINE DATE: {END}")
    steps = []
    print(f"{P}DEFINE SEQUENTIAL TASKS (Leave empty to finalize):{END}")
    while True:
        s = input(f"{S}  > {END}")
        if not s: break
        steps.append(s)

    if steps:
        current_time = datetime.now()
        file_ts = current_time.strftime("%H%M%S")
        txt_filename = f"plan_{user_data['name'].lower()}_{file_ts}.txt"
        txt_file_path = os.path.join(PLANS_DIR, txt_filename)

        with open(txt_file_path, "w", encoding="utf-8") as f:
            f.write("╔" + "═"*60 + "╗\n")
            f.write(f"║ ARCHITECT REPORT - v{VERSION:<26} ║\n")
            f.write("╠" + "═"*60 + "╣\n")
            f.write(f"║ OP: {user_data['name'].upper():<54}║\n")
            f.write(f"║ GOAL: {g.upper():<52}║\n")
            f.write(f"║ DATE: {current_time.strftime('%Y-%m-%d'):<48}║\n")
            f.write("╠" + "═"*60 + "╣\n")
            for i, s in enumerate(steps, 1):
                f.write(f"║ [{i:02}] [ ] {s:<47}║\n")
            f.write("╚" + "═"*60 + "╝\n")

        user_data["total_plans"] += 1
        save_user_profile(user_data["name"], user_data)
        
        # --- TADY JE TO VRÁCENO ---
        print(f"\n{A}>>> DATA_ARCHIVED_SUCCESSFULLY{END}")
        print(f"{S}PATH: {os.path.abspath(txt_file_path)}{END}") # <--- Tahle řádka tam chyběla
        
        open_with_pro_editor(txt_file_path)
    else:
        print(f"\n{RED}>>> ABORTED: NO_TASKS_DEFINED{END}")
    
    input(f"\n{S}Press Enter to return to Command Menu...{END}")

# --- START ---
user_data = security_access_control()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    show_status_bar(user_data)
    print(f"\n{BOLD}{P}AVAILABLE_COMMANDS:{END}")
    print(f"[{A}1{END}] CREATE_NEW_PLAN")
    print(f"[{A}2{END}] SYSTEM_LOG_OFF")
    cmd = input(f"\n{BOLD}{S}SYSTEM@CONSOLE > {END}").strip()

    if cmd == '2': break
    elif cmd == '1': create_action_plan(user_data)
