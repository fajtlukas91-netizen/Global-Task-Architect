import csv
import os
import shutil
import time
import sys
from datetime import datetime

# --- MATRIX COLOR SCHEME ---
G_BRIGHT = "\033[92m"
G_DARK = "\033[32m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RED = "\033[91m"
END = "\033[0m"

def matrix_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_boot_sequence():
    os.system('cls' if os.name == 'nt' else 'clear')
    # ASCII Art Header pro v7.02
    print(f"{G_BRIGHT}")
    print(r"  _    ____   ____ _   _ ___ _____ _____ ____ _____ ")
    print(r" / \  |  _ \ / ___| | | |_ _|_   _| ____/ ___|_   _|")
    print(r"/ _ \ | |_) | |   | |_| || |  | | |  _|| |     | |  ")
    print(r"/ ___ \|  _ <| |___|  _  || |  | | | |__| |___  | |  ")
    print(r"/_/   \_\_| \_\\____|_| |_|___| |_| |_____\____| |_|  ")
    print(f"{END}")
    matrix_print(f"{G_BRIGHT}>>> INITIALIZING ARCHITECT_CORE_v7.02_USER_FRIENDLY...", 0.05)
    matrix_print(f"{G_DARK}>>> DIRECTORY_CHECK: [BACKUPS, PLANS] OK.", 0.02)
    time.sleep(0.5)

def show_guide():
    print(f"\n{BOLD}{UNDERLINE}--- ARCHITECT_MANUAL ---{END}")
    print(f"{G_DARK}1. USER_NAME: Identifikátor pro název souboru.")
    print(f"2. PRIMARY_GOAL: Hlavní cíl vašeho plánu.")
    print(f"3. TASK_SEQUENCE: Úkoly oddělujte ČÁRKOU (např.: Úkol1, Úkol2).")
    print(f"4. HISTORY: Všechny cesty k souborům najdete v 'architect_history.log'.{END}")
    print(f"{BOLD}------------------------{END}\n")

def create_backup():
    if not os.path.exists('backups'):
        os.makedirs('backups')
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    backup_filename = f"backups/tasks_backup_{timestamp}.csv"
    if os.path.exists('tasks.csv'):
        shutil.copy('tasks.csv', backup_filename)
        print(f"{G_BRIGHT}✅ SYSTEM_BACKUP_CREATED: {backup_filename}{END}")

def create_action_plan(name, main_goal, steps, deadline):
    # Vytvoření složky pro plány
    if not os.path.exists('plans'):
        os.makedirs('plans')

    current_time = datetime.now()
    file_timestamp = current_time.strftime("%H%M%S")
    
    txt_file = f"plans/plan_{name.lower()}_{file_timestamp}.txt"
    csv_file = f"plans/plan_{name.lower()}_{file_timestamp}.csv"

    # Export do TXT
    with open(txt_file, "w", encoding="utf-8") as file:
        file.write(f"ACTION PLAN: {main_goal.upper()}\n")
        file.write(f"Created: {current_time.strftime('%d.%m.%Y %H:%M')} | Deadline: {deadline}\n")
        file.write("-" * 30 + "\n")
        for i, step in enumerate(steps, 1):
            file.write(f"{i}. [ ] {step}\n")

    # Export do CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Goal", "Step", "Deadline"])
        for step in steps:
            writer.writerow([main_goal, step, deadline])

    # --- NOVINKA v7.02: LOGOVÁNÍ CESTY PRO UŽIVATELE ---
    log_file = "architect_history.log"
    abs_txt_path = os.path.abspath(txt_file) # Zjistí úplnou adresu na disku
    
    with open(log_file, "a", encoding="utf-8") as log:
        timestamp = current_time.strftime("%d.%m.%Y %H:%M")
        log.write(f"[{timestamp}] CÍL: {main_goal} | CESTA: {abs_txt_path}\n")

    print(f"\n{G_BRIGHT}{BOLD}✅ ARCHIVE_SUCCESS: Plán byl vygenerován.{END}")
    print(f"{G_DARK}📍 PŘESNÁ LOKACE: {abs_txt_path}{END}")
    print(f"{G_DARK}📖 HISTORIE: Seznam všech vašich souborů najdete v: {os.path.abspath(log_file)}{END}")
    
    return txt_file

# --- HLAVNÍ CYKLUS ---
show_boot_sequence()
create_backup()

while True:
    print(f"\n{G_BRIGHT}{BOLD}[ GLOBAL_TASK_ARCHITECT_v7.02 ]{END}")
    u_input = input(f"{G_DARK}USER_NAME (or 'help'/'exit'): {END}").strip()
    
    if u_input.lower() == 'exit':
        print(f"{G_BRIGHT}SYSTEM_SHUTDOWN...{END}")
        break
    if u_input.lower() == 'help':
        show_guide()
        continue
    
    if not u_input:
        print(f"{RED}!! ERROR: NAME_REQUIRED !!{END}")
        continue

    u_goal = input(f"{G_DARK}PRIMARY_GOAL: {END}").strip()
    u_date = input(f"{G_DARK}DEADLINE: {END}").strip()
    u_steps = input(f"{G_DARK}TASKS (comma separated): {END}").strip()

    list_of_steps = [s.strip() for s in u_steps.split(",") if s.strip()]

    if not list_of_steps:
        print(f"{RED}!! ERROR: SEQUENCE_EMPTY !!{END}")
    else:
        created_file = create_action_plan(u_input, u_goal, list_of_steps, u_date)
        
        # Okamžité otevření pro kontrolu
        try:
            os.startfile(created_file)
        except:
            pass

    cont = input(f"\n{G_DARK}CREATE ANOTHER PLAN? (y/n): {END}").lower()
    if cont != 'y':
        print(f"{G_BRIGHT}TERMINATING_SESSION...{END}")
        break
