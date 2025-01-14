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

    today = date.today()
    today = str(today)
    today = today.split("-")
    return today


def split_date(date):
    year = date[0]
    month = date[1]
    day = date[2]
    return year, month, day

today = get_date_today()
year, month, day = split_date(today)

structure=str(read_input("structure")[0])

fstructure="f'"+structure+"'"


symbol="C" # hardcoded for class work

print(eval(fstructure))

folder_name=eval(fstructure)

create_folder(folder_name)

