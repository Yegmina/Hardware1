import os

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
    local_today = str(local_today)
    local_today = local_today.split("-")
    return local_today


def split_date(date):
    local_year = date[0]
    local_month = date[1]
    local_day = date[2]
    return local_year, local_month, local_day



today = get_date_today()
year, month, day = split_date(today)

structure=str(read_input("structure")[0])

fstructure="f'"+structure+"'"

symbol="C" # hardcoded for class work

print(eval(fstructure))

folder_name=eval(fstructure)

create_folder(folder_name)

