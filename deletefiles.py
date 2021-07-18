import os
import datetime

path = input('Enter the name of the directory (not a file) : ')
list_of_files = os.listdir(path)
today = datetime.datetime.now()
for file in list_of_files:
    individual_file = path+'/'+file
    file_creation_sec = os.path.getctime(individual_file)
    file_creation_date = datetime.datetime.fromtimestamp(file_creation_sec)
    diff_days = (today-file_creation_date).days
    if diff_days>30:
        os.path.remove(individual_file)