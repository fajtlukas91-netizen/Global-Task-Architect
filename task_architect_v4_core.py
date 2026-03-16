# Project: Global Task Architect
# Version: 4.0 (Professional Storage Edition)
# Description: Professional tool for generating non-overwriting action plans.

import os
from datetime import datetime

def create_action_plan(name, main_goal, steps, deadline):
    # 1. Setup Time and Analytics
    current_time = datetime.now()
    created_at = current_time.strftime("%d.%m.%Y %H:%M")
    # This timestamp will be used for the filename to prevent overwriting
    file_timestamp = current_time.strftime("%H%M%S") 
    total_tasks = len(steps)

    # 2. Console Output
    print(f"\n" + "="*40)
    print(f"GENERATING PLAN: {name.upper()}")
    print(f"TOTAL TASKS: {total_tasks}")
    print("="*40)
    
    # 3. Smart Filename Logic (The Upgrade)
    # Result: plan_lukas_104522.txt (name + hour/min/sec)
    file_name = f"plan_{name.lower()}_{file_timestamp}.txt"
    
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"ACTION PLAN RESULT - {name.upper()}\n")
        file.write(f"Created on: {created_at}\n")
        file.write(f"Main Goal: {main_goal}\n")
        file.write(f"Deadline: {deadline}\n")
        file.write(f"Total tasks to complete: {total_tasks}\n")
        file.write("-" * 40 + "\n")
        
        for i, step in enumerate(steps, 1):
            line = f"{i}. [ ] {step}"
            print(line)               
            file.write(line + "\n")   
            
    print("="*40)
    print(f"✅ SUCCESS! File created: {file_name}")
    return file_name

# --- MAIN PROGRAM ---

while True:
    user_name = input("\nEnter your name: ")
    goal = input("What is your main goal? ")
    target_date = input("When do you want to achieve it? ")
    steps_input = input("Enter steps separated by commas: ")

    step_list = [s.strip() for s in steps_input.split(",") if s.strip() != ""]

    if len(step_list) == 0:
        print("\n❌ Error: Please enter at least one step.")
    else:
        created_file = create_action_plan(user_name, goal, step_list, target_date)
        os.startfile(created_file)

    choice = input("\nCreate another plan? (yes/no): ").lower().strip()
    if choice != "yes":
        print("\nStay productive! Goodbye.")
        break
