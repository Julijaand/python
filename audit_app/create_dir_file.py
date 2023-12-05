import os
from datetime import date
import constants as c

todayDate = date.today().strftime('%Y-%m-%d')
directory = '/home/sgtuser/Documents/Devops/sgt/Audit_system'
file_name = os.path.join(directory, c.PERSONAL_ID + ".txt")

def create_directory():
    if not os.path.exists(todayDate):
        os.makedirs(todayDate)
    else:
        print("Today's directory already exists")

def create_file():
    x = os.path.join(todayDate, f"{c.PERSONAL_ID}.txt")
    with open(x, "a") as fn:
        fn.write(c.NAME + c.SURNAME + c.PERSONAL_ID)

def output_info():
    for path, dirs, files in os.walk('/home/sgtuser/Documents/Devops/sgt/Audit_system'):
        for f in files:
            file_name2 = os.path.join(path, f)
            with open(file_name2, "r") as myFile:
                print(myFile.read())


