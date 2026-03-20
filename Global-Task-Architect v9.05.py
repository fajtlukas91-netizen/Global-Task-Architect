import os
import json
import getpass
import time
import sys
from datetime import datetime

# --- HIGH_CONTRAST_PALETTE ---
AMBER = '\033[33m'       # Standard Amber (Base text)
GRAY = '\033[90m'        # Dark Gray (Decorations)
MAGENTA = '\033[95m'     # Bright Magenta (CRITICAL WARNING - 3 days left)
BOLD_RED = '\033[1;31m'  # Bold Red (EXPIRED)
RESET = '\033[0m'

USER_DIR = "architect_users"
if not os.path.exists(USER_DIR): os.makedirs(USER_DIR)

def refined_logo():
    """Renders the logo once at session start"""
    print(f"{AMBER}  ▄▀▀▄ █▀▀▄ ▄▀▀▄ █  █ ▀█▀ ▀█▀ █▀▀ ▄▀▀▄ ▀█▀")
    print(f"  █▄▄█ █▄▄▀ █    █▀▀█  █   █  █▀▀ █    █")
    print(f"  █  █ █  █ ▀▄▄▀ █  █ ▄█▄  █  █▄▄ ▀▄▄▀ █  {RESET}")
    print(f"{GRAY}  -- TERMINAL_MANAGEMENT_SYSTEM_v10.0 --{RESET}\n")

def login():
    """Handles operator authentication and registration"""
    os.system('cls' if os.name == 'nt' else 'clear')
    refined_logo()
    print(f"  {GRAY}>> {AMBER}SYSTEM AUTHORIZATION{RESET}")
    op_id = input(f"  {AMBER}OPERATOR_ID: {RESET}").strip()
    if not op_id: return None, None
    
    user_file = os.path.join(USER_DIR, f"{op_id}.json")
    if os.path.exists(user_file):
        with open(user_file, 'r', encoding='utf-8') as f:
            user_data = json.load(f)
        pwd = getpass.getpass(f"  {AMBER}ACCESS_KEY: {RESET}")
        if pwd != user_data.get('key', '')[::-1]: 
            print(f"  {BOLD_RED}ACCESS DENIED.{RESET}")
            time.sleep(1)
            return None, None
    else:
        print(f"  {AMBER}NEW OPERATOR DETECTED...{RESET}")
        pwd = getpass.getpass(f"  {AMBER}SET ACCESS_KEY: {RESET}")
        user_data = {"key": pwd[::-1], "tasks": []}
        with open(user_file, 'w', encoding='utf-8') as f:
            json.dump(user_data, f, indent=4)
    
    print(f"  {AMBER}LOGGED IN. SYSTEM READY.{RESET}")
    time.sleep(0.5)
    return op_id, user_data

def system_health_check(tasks):
    """Scans deadlines and applies priority color-coding"""
    today = datetime.now()
    found_issues = False
    print(f"\n  {GRAY}[ DEADLINE ANALYSIS ]{RESET}")
    
    if not tasks:
        print(f"  {GRAY}DATABASE IS CURRENTLY EMPTY{RESET}")
    else:
        for t in tasks:
            d_str = t.get('deadline')
            if d_str and d_str != "NONE":
                try:
                    dt = datetime.strptime(d_str, "%d.%m.%Y")
                    diff = (dt - today).days + 1
                    
                    if diff < 0:
                        # EXPIRED
                        print(f"  {BOLD_RED}[!!!] EXPIRED: {t['title']} ({d_str}){RESET}")
                        found_issues = True
                    elif diff <= 3:
                        # CRITICAL (3 days left)
                        print(f"  {MAGENTA}[ * ] WARNING: {t['title']} ({diff} days left!){RESET}")
                        found_issues = True
                except ValueError:
                    continue
                
    if not found_issues and tasks:
        print(f"  {AMBER}STATUS: NOMINAL (All deadlines cleared){RESET}")
    print(f"  {GRAY}------------------------------------------{RESET}")

def main():
    op_id, user_data = login()
    if not op_id: return

    user_file = os.path.join(USER_DIR, f"{op_id}.json")
    print(f"  {GRAY}ACTIVE SESSION: {AMBER}{op_id}{RESET}")

    while True:
        system_health_check(user_data['tasks'])
        
        # English Menu
        print(f"  {AMBER}[1] NEW PROJECT  [2] DATABASE  [Q] LOGOUT{RESET}")
        choice = input(f"\n  {AMBER}COMMAND >> {RESET}").upper()

        if choice == '1':
            title = input(f"  {AMBER}PROJECT NAME: {RESET}").strip()
            if title:
                deadline = "NONE"
                while True:
                    d_in = input(f"  {AMBER}DEADLINE (DD.MM.YYYY / ENTER for NONE): {RESET}").strip()
                    if not d_in: break
                    try:
                        datetime.strptime(d_in, "%d.%m.%Y")
                        deadline = d_in; break
                    except ValueError:
                        print(f"  {BOLD_RED}[!] ERROR: Enter date as DD.MM.YYYY (e.g., 25.12.2026){RESET}")
                
                user_data['tasks'].append({"title": title, "deadline": deadline})
                with open(user_file, 'w', encoding='utf-8') as f:
                    json.dump(user_data, f, indent=4)
                print(f"  {AMBER}>> RECORD SUCCESSFULLY ARCHIVED.{RESET}")

        elif choice == '2':
            print(f"\n  {GRAY}--- PROJECT DATABASE ---{RESET}")
            if not user_data['tasks']:
                print(f"  {GRAY}(Database is empty){RESET}")
            else:
                for i, t in enumerate(user_data['tasks']):
                    print(f"  {GRAY}[{i}] {AMBER}{t['title']:<18} {GRAY}| DEADLINE: {t.get('deadline','---')}{RESET}")
                
                print(f"\n  {GRAY}Enter ID to DELETE or ENTER to return{RESET}")
                del_in = input(f"  {AMBER}ACTION: {RESET}").strip()
                if del_in.isdigit():
                    idx = int(del_in)
                    if 0 <= idx < len(user_data['tasks']):
                        removed = user_data['tasks'].pop(idx)
                        with open(user_file, 'w', encoding='utf-8') as f:
                            json.dump(user_data, f, indent=4)
                        print(f"  {BOLD_RED}REMOVED: {removed['title']}{RESET}")
                        time.sleep(0.5)

        elif choice == 'Q':
            print(f"  {AMBER}SYSTEM SHUTDOWN. SESSION TERMINATED.{RESET}")
            time.sleep(0.5)
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n  {AMBER}EMERGENCY SYSTEM SHUTDOWN...{RESET}")
        sys.exit()
