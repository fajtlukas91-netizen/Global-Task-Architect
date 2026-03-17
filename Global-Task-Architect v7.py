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

# --- 1. & 2. UI: EFEKT NAČÍTÁNÍ ---
def matrix_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_boot_sequence():
    os.system('cls' if os.name == 'nt' else 'clear')
    matrix_print(f"{G_BRIGHT}>>> INITIALIZING ARCHITECT_CORE_v7.0...", 0.05)
    matrix_print(f"{G_DARK}>>> LOADING MODULES: [BACKUP_SYSTEM, EXPORT_ENGINE, UI_CONTROLLER]...", 0.02)
    time.sleep(0.5)
    print(f"{G_BRIGHT}>>> SYSTEM_READY.{END}\n")

# --- 3. NÁPOVĚDA / GUIDE ---
def show_guide():
    print(f"\n{BOLD}{UNDERLINE}--- ARCHITECT_MANUAL ---{END}")
    print(f"{G_DARK}1. USER_NAME: Your identifier for file naming.")
    print(f"2. PRIMARY_GOAL: The main objective of your plan.")
    print(f"3. TASK_SEQUENCE: Separate tasks with a COMMA (e.g.: Task1, Task2).")
    print(f"4. DEADLINE: Use any format (e.g.: 24.12.2026).{END}")
    print(f"{BOLD}------------------------{END}\n")

# --- ZÁLOHA (ZŮSTÁVÁ) ---
def create_backup():
    if not os.path.exists('backups'):
        os.makedirs('backups')
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    backup_filename = f"backups/tasks_backup_{timestamp}.csv"
    if os.path.exists('tasks.csv'):
        shutil.copy('tasks.csv', backup_filename)
        print(f"{G_BRIGHT}✅ SYSTEM_BACKUP_CREATED: {backup_filename}{END}")

def create_action_plan(name, main_goal, steps, deadline):
    current_time = datetime.now()
    created_at = current_time.strftime("%d.%m.%Y %H:%M")
    file_timestamp = current_time.strftime("%H%M%S")
    
    txt_file = f"plan_{name.lower()}_{file_timestamp}.txt"
    csv_file = f"plan_{name.lower()}_{file_timestamp}.csv"

    # Exporty zůstávají stejné jako ve v6...
    with open(txt_file, "w", encoding="utf-8") as file:
        file.write(f"ACTION PLAN: {main_goal.upper()}\n")
        file.write(f"Created: {created_at} | Deadline: {deadline}\n")
        file.write("-" * 30 + "\n")
        for i, step in enumerate(steps, 1):
            file.write(f"{i}. [ ] {step}\n")

    print(f"\n{G_BRIGHT}{BOLD}SYSTEM_REPORT: FILES_GENERATED{END}")
    return txt_file

# --- HLAVNÍ CYKLUS ---
show_boot_sequence()
create_backup()

while True:
    print(f"\n{G_BRIGHT}{BOLD}[ GLOBAL_TASK_ARCHITECT_v7 ]{END}")
    print(f"{G_DARK}Type 'help' for manual or 'exit' to quit.{END}")
    
    u_input = input(f"{G_DARK}USER_NAME (or command): {END}").strip()
    
    if u_input.lower() == 'help':
        show_guide() # Tady vypíše nápovědu
        continue     #<--- Toto je klíč! Vrátí program zpět na USER_NAME

    if u_input.lower() == 'exit':
        print(f"{G_BRIGHT} TERMINATING_SYSTEM . . .{END}")
        break               # Ukončí program
    
    # --- 4. LOGIKA: VALIDACE JMÉNA ---
    if not u_input:
        print(f"{RED}!! ERROR: NAME_REQUIRED !!{END}")
        continue

    u_goal = input(f"{G_DARK}PRIMARY_GOAL: {END}").strip()
    u_date = input(f"{G_DARK}DEADLINE_STAMP: {END}").strip()
    u_steps = input(f"{G_DARK}TASK_SEQUENCE (split by comma): {END}").strip()

    # --- VALIDACE KROKŮ ---
    list_of_steps = [s.strip() for s in u_steps.split(",") if s.strip()]

    if not list_of_steps:
        print(f"{RED}{BOLD}!! ERROR: SEQUENCE_EMPTY - MISSION_ABORTED !!{END}")
    else:
        created = create_action_plan(u_input, u_goal, list_of_steps, u_date)
        try:
            os.startfile(created)
        except:
            print(f"{G_DARK}Plan created: {created}{END}")

    # Dotaz na pokračování (aby se to netočilo zběsile)
    cont = input(f"\n{G_DARK}NEW_ENTRY? (y/n): {END}").lower()
    if cont != 'y':
        break
