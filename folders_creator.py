import os
import datetime # for getting today's day
import sys
import select
import time #for waiting

def is_valid_time_and_day():
    now = datetime.datetime.now()

    if not (8 <= now.hour < 16):
        return False
    if now.weekday() >= 5:
        return False
    return True

def read_input(name):
    file = open(f"{name}.txt", "r")
    content = file.read()
    return content.split("\n")

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully!")
    else:
        print(f"Folder '{folder_name}' already exists.")

def get_date_today():
    from datetime import date
    local_today = date.today()
    return str(local_today).split("-")

def split_date(date):
    return date[0], date[1], date[2]

def main1():
    """Create only one folder, for today"""
    if not is_valid_time_and_day():
        sys.exit("Script terminated: Not within allowed time or it's a weekend.")

    today = get_date_today()
    year, month, day = split_date(today)

    structure = str(read_input("structure")[0])
    fstructure = f"f'{structure}'"

    symbol = input("special symbol at the end: ")

    if symbol.strip().lower() in ["", " "]:
        symbol = "ClassWork"  # Hardcoded for class work
    elif symbol.lower() == "l":
        symbol = "Linux"
    elif symbol.lower() == "n":
        symbol = "Network"
    elif symbol.lower() == "h":
        symbol="HealthTechnology"

    folder_name = eval(fstructure)
    create_folder(folder_name)

if __name__ == "__main__":
    main1()
