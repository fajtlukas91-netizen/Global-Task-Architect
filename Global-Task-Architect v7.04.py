import csv
import os
import shutil
import time
import sys
import json
import subprocess # NOVÉ: Pro spouštění externích aplikací
from datetime import datetime

# --- MATRIX COLOR SCHEME ---
G_BRIGHT = "\033[92m"
G_DARK = "\033[32m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RED = "\033[91m"
Y = "\033[93m"
END = "\033[0m"

# --- CONFIG ---
USER_DATA_DIR = "architect_users"
PLANS_DIR = "plans"

for folder in [USER_DATA_DIR, PLANS_DIR]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# --- SYSTEM FUNCTIONS ---

def matrix_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def open_with_pro_editor(file_path):
    """
    v7.04 FEATURE: Pokusí se otevřít plán v lepším editoru.
    Pořadí: 1. Notepad++, 2. WordPad, 3. Default System Editor
    """
    # Cesty k editorům (standardní umístění)
    npp_path = r"C:\Program Files\Notepad++\notepad++.exe"
    wordpad_path = r"C:\Program Files\Windows NT\Accessories\wordpad.exe"
    
    abs_path = os.path.abspath(file_path)
    
    try:
        if os.path.exists(npp_path):
            matrix_print(f"{G_DARK}>>> LAUNCHING_NOTEPAD++...", 0.01)
            subprocess.Popen([npp_path, abs_path])
        elif os.path.exists(wordpad_path):
            matrix_print(f"{G_DARK}>>> LAUNCHING_WORDPAD (Notepad++ not found)...", 0.01)
            subprocess.Popen([wordpad_path, abs_path])
        else:
            matrix_print(f"{G_DARK}>>> LAUNCHING_DEFAULT_SYSTEM_EDITOR...", 0.01)
            os.startfile(abs_path)
    except Exception as e:
        print(f"{RED}!! EXECUTION_ERROR: {e} !!{END}")

def get_user_profile(name):
    file_path = os.path.join(USER_DATA_DIR, f"{name.lower()}.json")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        new_profile = {
            "name": name,
            "created_at": str(datetime.now().date()),
            "total_plans": 0,
            "last_session": str(datetime.now().strftime("%H:%M:%S"))
        }
        save_user_profile(name, new_profile)
        return new_profile

def save_user_profile(name, data):
    file_path = os.path.join(USER_DATA_DIR, f"{name.lower()}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def create_action_plan(user_data, main_goal, steps, deadline):
    current_time = datetime.now()
    file_timestamp = current_time.strftime("%H%M%S")
    name = user_data['name']
    
    txt_file = os.path.join(PLANS_DIR, f"plan_{name.lower()}_{file_timestamp}.txt")

    # Export to TXT se stylovým ohraničením
    with open(txt_file, "w", encoding="utf-8") as file:
        file.write("╔" + "═"*58 + "╗\n")
        file.write(f"║ ARCHITECT_ACTION_PLAN v7.04{' ':>28}║\n")
        file.write("╠" + "═"*58 + "╣\n")
        file.write(f"║ OPERATOR: {name.upper():<47}║\n")
        file.write(f"║ CREATED:  {current_time.strftime('%Y-%m-%d %H:%M'):<47}║\n")
        file.write(f"║ DEADLINE: {deadline:<47}║\n")
        file.write("╠" + "═"*58 + "╣\n")
        file.write(f"║ GOAL: {main_goal.upper():<52}║\n")
        file.write("╟" + "─"*58 + "╢\n")
        for i, step in enumerate(steps, 1):
            file.write(f"║ [{i}] [ ] {step:<49}║\n")
        file.write("╚" + "═"*58 + "╝\n")

    abs_path = os.path.abspath(txt_file)
    user_data["total_plans"] += 1
    user_data["last_session"] = current_time.strftime("%Y-%m-%d %H:%M:%S")
    save_user_profile(name, user_data)

    print(f"\n{G_BRIGHT}{BOLD}✅ ARCHIVE_SUCCESS: Plan generated successfully.{END}")
    print(f"{G_DARK}📍 LOCATION: {Y}{abs_path}{END}")
    
    # OTEVŘENÍ V LEPŠÍM EDITORU
    open_with_pro_editor(txt_file)
    
    return txt_file

# --- HLAVNÍ CYKLUS ---
clear()
print(f"{G_BRIGHT}--- ARCHITECT_v7.04_PRO_EDITOR_READY ---{END}")
u_name = input(f"{G_DARK}IDENTIFY OPERATOR: {END}").strip()
if not u_name: u_name = "User"
user_data = get_user_profile(u_name)

while True:
    clear()
    print(f"{G_BRIGHT}{BOLD}[ GLOBAL_TASK_ARCHITECT_v7.04 ]{END}")
    print(f"{G_DARK}ACTIVE_OPERATOR: {user_data['name'].upper()} | LOGS: {user_data['total_plans']}{END}\n")
    
    cmd = input(f"{G_DARK}1. NEW | 2. EXIT > {END}").strip().lower()

    if cmd == '2' or cmd == 'exit':
        break
    elif cmd == '1' or cmd == 'new':
        u_goal = input(f"{G_DARK}PRIMARY_GOAL: {END}").strip()
        u_date = input(f"{G_DARK}DEADLINE: {END}").strip()
        u_steps = input(f"{G_DARK}TASKS (comma separated): {END}").strip()
        
        list_of_steps = [s.strip() for s in u_steps.split(",") if s.strip()]
        if list_of_steps:
            create_action_plan(user_data, u_goal, list_of_steps, u_date)
            input(f"\n{G_DARK}Press Enter to return to Command Prompt...{END}")
