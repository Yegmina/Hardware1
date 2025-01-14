import os

def read_input(name):
    file = open(f"{name}.txt", "r")
    content = file.read()
    return content.split("\n")

from datetime import date

today = date.today()
today=str(today)
today=today.split("-")
year=today[0]
month=today[1]
day=today[2]


structure=str(read_input("structure")[0])

fstructure="f'"+structure+"'"


symbol="C" # hardcoded for class work

print(eval(fstructure))

folder_name=eval(fstructure)
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Folder '{folder_name}' created successfully!")
else:
    print(f"Folder '{folder_name}' already exists.")

