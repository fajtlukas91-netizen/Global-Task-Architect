# Project: Global Task Architect
# Version: 3.0 (Analytics Edition)
# Description: Automated tool for generating structured action plans with task counting and interactive loop.

import os
from datetime import datetime

def create_action_plan(name, main_goal, steps, deadline):
    """
    Function to process data, count tasks, and save the result to a file.
    """
    # 1. Setup Time and Analytics
    current_time = datetime.now()
    created_at = current_time.strftime("%d.%m.%Y %H:%M")
    total_tasks = len(steps) # Here is our math!

    # 2. Console Output
    print(f"\n" + "="*40)
    print(f"ACTION PLAN FOR: {name.upper()}")
    print(f"CREATED AT: {created_at}")
    print(f"MAIN GOAL: {main_goal}")
    print(f"DEADLINE: {deadline}")
    print(f"TOTAL TASKS: {total_tasks}") # Showing the count to the user
    print("="*40)
    
    # 3. File Creation
    file_name = f"plan_{name.lower()}.txt"
    
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"ACTION PLAN RESULT - {name.upper()}\n")
        file.write(f"Created on: {created_at}\n")
        file.write(f"Main Goal: {main_goal}\n")
        file.write(f"Deadline: {deadline}\n")
        file.write(f"Total tasks to complete: {total_tasks}\n") # Writing count to file
        file.write("-" * 40 + "\n")
        
        # The loop that processes each task
        for i, step in enumerate(steps, 1):
            line = f"{i}. [ ] {step}"
            print(line)               
            file.write(line + "\n")   
            
    print("="*40)
    print(f"✅ DONE! Your plan is saved in: {file_name}")
    return file_name

# --- MAIN PROGRAM (Interactive Loop) ---

while True:
    # Data collection
    user_name = input("\nEnter your name: ")
    goal = input("What is your main goal? ")
    target_date = input("When do you want to achieve it? ")
    steps_input = input("Enter steps separated by commas: ")

    # Data cleaning (stripping whitespace and removing empty entries)
    step_list = [s.strip() for s in steps_input.split(",") if s.strip() != ""]

    if len(step_list) == 0:
        print("\n❌ Error: You must enter at least one step to create a plan.")
    else:
        # Running the engine
        created_file = create_action_plan(user_name, goal, step_list, target_date)
        
        # Open the result automatically (Windows)
        os.startfile(created_file)

    # Ask for continuation
    choice = input("\nDo you want to create another plan? (yes/no): ").lower().strip()
    
    if choice != "yes":
        print("\nThank you for using Global Task Architect. Stay productive! Goodbye.")
        break
