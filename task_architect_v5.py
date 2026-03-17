import os
import csv  # Tato knihovna umí vytvářet tabulky pro Excel
from datetime import datetime

def create_action_plan(name, main_goal, steps, deadline):
    # --- 1. PŘÍPRAVA DAT ---
    current_time = datetime.now()
    created_at = current_time.strftime("%d.%m.%Y %H:%M")
    file_timestamp = current_time.strftime("%H%M%S")
    
    # Názvy souborů (vytvoříme dva různé výstupy)
    txt_file = f"plan_{name.lower()}_{file_timestamp}.txt"
    csv_file = f"plan_{name.lower()}_{file_timestamp}.csv"

    # --- 2. EXPORT DO TXT (Klasický přehled pro lidi) ---
    with open(txt_file, "w", encoding="utf-8") as file:
        file.write(f"ACTION PLAN: {main_goal.upper()}\n")
        file.write(f"Created: {created_at} | Deadline: {deadline}\n")
        file.write("-" * 30 + "\n")
        for i, step in enumerate(steps, 1):
            file.write(f"{i}. [ ] {step}\n")

    # --- 3. EXPORT DO CSV (Tabulka pro firmy a Excel) ---
    # CSV = Comma Separated Values (data oddělená čárkou)
    with open(csv_file, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        # Hlavička tabulky
        writer.writerow(["ID", "Task Description", "Status", "Created At"])
        # Jednotlivé řádky
        for i, step in enumerate(steps, 1):
            writer.writerow([i, step, "To Do", created_at])

    print(f"\n" + "="*40)
    print(f"✅ ÚSPĚCH! Vygenerovány 2 formáty:")
    print(f"1. TEXT: {txt_file} (pro rychlé čtení)")
    print(f"2. DATA: {csv_file} (pro Excel/Analýzu)")
    print("="*40)
    
    return txt_file

# --- HLAVNÍ SMYČKA ---
while True:
    print("\n--- GLOBAL TASK ARCHITECT v5 ---")
    u_name = input("Tvoje jméno: ")
    u_goal = input("Hlavní cíl: ")
    u_date = input("Termín (Deadline): ")
    u_steps = input("Kroky (odděluj čárkou): ")

    list_of_steps = [s.strip() for s in u_steps.split(",") if s.strip()]

    if not list_of_steps:
        print("❌ Chyba: Musíš zadat aspoň jeden krok!")
    else:
        created = create_action_plan(u_name, u_goal, list_of_steps, u_date)
        os.startfile(created) # Otevře TXT soubor pro kontrolu

    if input("\nChceš vytvořit další plán? (ano/ne): ").lower() != "ano":
        print("Měj produktivní den! Ahoj.")
        break
