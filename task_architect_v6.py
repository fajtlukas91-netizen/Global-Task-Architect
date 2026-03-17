import csv
import os
import shutil
from datetime import datetime

# --- MATRIX COLOR SCHEME ---
G_BRIGHT = "\033[92m"  # Jasně zelená
G_DARK = "\033[32m"    # Tmavší zelená (standard)
BOLD = "\033[1m"       # Tučné
UNDERLINE = "\033[4m"   # Podtržené
END = "\033[0m"        # Reset barev

def create_backup():
    if not os.path.exists('backups'):
        os.makedirs('backups')
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"backups/tasks_backup_{timestamp}.csv"
    if os.path.exists('tasks.csv'):
        shutil.copy('tasks.csv', backup_filename)
        print(f"✅ Záloha vytvořena: {backup_filename}")


def create_action_plan(name, main_goal, steps, deadline):
    current_time = datetime.now()
    created_at = current_time.strftime("%d.%m.%Y %H:%M")
    file_timestamp = current_time.strftime("%H%M%S")
    
    txt_file = f"plan_{name.lower()}_{file_timestamp}.txt"
    csv_file = f"plan_{name.lower()}_{file_timestamp}.csv"

    # Export do TXT
    with open(txt_file, "w", encoding="utf-8") as file:
        file.write(f"ACTION PLAN: {main_goal.upper()}\n")
        file.write(f"Created: {created_at} | Deadline: {deadline}\n")
        file.write("-" * 30 + "\n")
        for i, step in enumerate(steps, 1):
            file.write(f"{i}. [ ] {step}\n")

    # Export do CSV
    with open(csv_file, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Task Description", "Status", "Created At"])
        for i, step in enumerate(steps, 1):
            writer.writerow([i, step, "To Do", created_at])

    # --- MATRIX STYLE TERMINAL OUTPUT ---
    print(f"\n{G_BRIGHT}{BOLD}" + "v" * 50)
    print(f" SYSTEM_REPORT: DATA_GENERATED_SUCCESSFULLY")
    print(f"{END}{G_DARK} > FILE_01: {txt_file} (plain_text)")
    print(f" > FILE_02: {csv_file} (data_structure)")
    print(f"{G_BRIGHT}{BOLD}" + "ʌ" * 50 + f"{END}")
    
    return txt_file

# --- MAIN SYSTEM LOOP ---
# TADY ZAVOLAME ZALOHU HNED PŘI STARTU
create_backup()

while True:
    print(f"\n{G_BRIGHT}{BOLD}[ GLOBAL_TASK_ARCHITECT_v6 ]{END}")
    print(f"{G_DARK}Initialising interface...{END}")
    
    u_name = input(f"{G_DARK}USER_NAME: {END}")
    u_goal = input(f"{G_DARK}PRIMARY_GOAL: {END}")
    u_date = input(f"{G_DARK}DEADLINE_STAMP: {END}")
    u_steps = input(f"{G_DARK}TASK_SEQUENCE (split by comma): {END}")

    list_of_steps = [s.strip() for s in u_steps.split(",") if s.strip()]

    if not list_of_steps:
        print(f"\033[91m{BOLD}!! ERROR: SEQUENCE_EMPTY !!{END}")
    else:
        created = create_action_plan(u_name, u_goal, list_of_steps, u_date)
        try:
            os.startfile(created)
        except:
            pass
