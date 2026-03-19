import csv
import os
import shutil
import time
import sys
import json
from datetime import datetime

# --- MATRIX COLOR SCHEME ---
G_BRIGHT = "\033[92m"
G_DARK = "\033[32m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RED = "\033[91m"
Y = "\033[93m"  # Yellow pro zvýraznění cesty
END = "\033[0m"

# --- CONFIG & DIRECTORIES ---
USER_DATA_DIR = "architect_users"
PLANS_DIR = "plans"
BACKUP_DIR = "backups"

# Inicializace složek
for folder in [USER_DATA_DIR, PLANS_DIR, BACKUP_DIR]:
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

def get_user_profile(name):
    """Správa uživatelských profilů v JSON."""
    file_path = os.path.join(USER_DATA_DIR, f"{name.lower()}.json")
    
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        matrix_print(f"{G_DARK}>>> NEW_IDENTITY_DETECTED: Generating database for {name.upper()}...", 0.02)
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

def show_boot_sequence():
    clear()
    print(f"{G_BRIGHT}")
    print(r"  _    ____    ____ _   _ ___ _____ _____ ____ _____ ")
    print(r" / \  |  _ \ / ___| | | |_ _|_   _| ____/ ___|_   _|")
    print(r"/ _ \ | |_) | |   | |_| || |  | | |  _|| |     | |  ")
    print(r"/ ___ \|  _ <| |___|  _  || |  | | | |__| |___  | |  ")
    print(r"/_/   \_\_| \_\\____|_| |_|___| |_| |_____\____| |_|  ")
    print(f"{END}")
    matrix_print(f"{G_BRIGHT}>>> INITIALIZING ARCHITECT_CORE_v7.03_STABLE...", 0.05)
    matrix_print(f"{G_DARK}>>> DIRECTORY_CHECK: [BACKUPS, PLANS, USERS] OK.", 0.02)
    time.sleep(0.5)

def create_backup():
    """Zálohuje hlavní databázi úkolů, pokud existuje."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    backup_filename = os.path.join(BACKUP_DIR, f"tasks_backup_{timestamp}.csv")
    if os.path.exists('tasks.csv'):
        shutil.copy('tasks.csv', backup_filename)
        print(f"{G_BRIGHT}✅ SYSTEM_BACKUP_CREATED: {os.path.abspath(backup_filename)}{END}")

def create_action_plan(user_data, main_goal, steps, deadline):
    current_time = datetime.now()
    file_timestamp = current_time.strftime("%H%M%S")
    name = user_data['name']
    
    # Definice souborů uvnitř složky plans
    txt_file = os.path.join(PLANS_DIR, f"plan_{name.lower()}_{file_timestamp}.txt")
    csv_file = os.path.join(PLANS_DIR, f"plan_{name.lower()}_{file_timestamp}.csv")

    # Export to TXT
    with open(txt_file, "w", encoding="utf-8") as file:
        file.write(f"ACTION PLAN: {main_goal.upper()}\n")
        file.write(f"Created: {current_time.strftime('%Y-%m-%d %H:%M')} | Deadline: {deadline}\n")
        file.write(f"Operator: {name}\n")
        file.write("-" * 40 + "\n")
        for i, step in enumerate(steps, 1):
            file.write(f"{i}. [ ] {step}\n")

    # Export to CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Goal", "Step", "Deadline", "Operator"])
        for step in steps:
            writer.writerow([main_goal, step, deadline, name])

    # Získání absolutní cesty pro uživatele
    abs_txt_path = os.path.abspath(txt_file)

    # Aktualizace uživatelských statistik
    user_data["total_plans"] += 1
    user_data["last_session"] = current_time.strftime("%Y-%m-%d %H:%M:%S")
    save_user_profile(name, user_data)

    # LOGGING do historie
    with open("architect_history.log", "a", encoding="utf-8") as log:
        log.write(f"[{current_time.strftime('%Y-%m-%d %H:%M')}] GOAL: {main_goal} | PATH: {abs_txt_path}\n")

    # Finální výpis cesty
    print(f"\n{G_BRIGHT}{BOLD}✅ ARCHIVE_SUCCESS: Plan generated successfully.{END}")
    print(f"{G_DARK}------------------------------------------------------------{END}")
    print(f"{G_BRIGHT}📍 LOCATION:{END} {Y}{BOLD}{abs_txt_path}{END}")
    print(f"{G_DARK}📊 USER_STATS: Total plans for {name.upper()}: {user_data['total_plans']}{END}")
    print(f"{G_DARK}------------------------------------------------------------{END}")
    
    return txt_file

# --- MAIN EXECUTION LOOP ---
show_boot_sequence()
create_backup()

# Identifikace na začátku
matrix_print(f"\n{G_BRIGHT}>>> ACCESS_RESTRICTED: IDENTITY_CHECK_REQUIRED{END}", 0.03)
u_name = input(f"{G_DARK}ENTER_OPERATOR_NAME: {END}").strip()
if not u_name: u_name = "Anonymous"
user_data = get_user_profile(u_name)

while True:
    clear()
    print(f"{G_BRIGHT}{BOLD}[ GLOBAL_TASK_ARCHITECT_v7.02_STABLE ]{END}")
    print(f"{G_DARK}OPERATOR: {user_data['name'].upper()} | SESSION_LOGS: {user_data['total_plans']}{END}")
    print(f"{G_DARK}------------------------------------------------------------{END}")
    
    print(f"\n{BOLD}COMMAND_MENU:{END}")
    print(f"1. {G_BRIGHT}NEW{END} (Generate Project Plan)")
    print(f"2. {G_BRIGHT}EXIT{END}")
    
    cmd = input(f"\n{G_DARK}ARCHITECT_INPUT > {END}").strip().lower()

    if cmd == 'exit':
        matrix_print(f"{G_BRIGHT}TERMINATING_SESSION... GOODBYE, OPERATOR {user_data['name'].upper()}.{END}")
        time.sleep(1)
        break
    
    elif cmd == 'new':
        u_goal = input(f"{G_DARK}PRIMARY_GOAL: {END}").strip()
        u_date = input(f"{G_DARK}DEADLINE: {END}").strip()
        u_steps = input(f"{G_DARK}TASKS (comma separated): {END}").strip()

        list_of_steps = [s.strip() for s in u_steps.split(",") if s.strip()]

        if not list_of_steps:
            print(f"{RED}!! ERROR: SEQUENCE_EMPTY !!{END}")
            time.sleep(1)
        else:
            created_file = create_action_plan(user_data, u_goal, list_of_steps, u_date)
            # Automatické otevření souboru
            try:
                os.startfile(created_file)
            except:
                pass
            input(f"\n{G_DARK}PLAN_READY. Press Enter to return to main menu...{END}")

    else:
        print(f"{RED}!! INVALID_COMMAND !!{END}")
        time.sleep(1)
