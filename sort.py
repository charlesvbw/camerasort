#This is a script to sort our camera jpg's into folders by day.
#We could probably use bash but I'm trying to learn git (and python) so here we are.
import datetime
import os
#loop through each file.  create directory based on filename with defined structure
#for the days.
path = 'C:/tmp/godo_timelapse' #set path for sorting pictures
for file in os.listdir(path):
    file_day = file[15:17]
    file_month = file[13:15]
    folder = file_month + "-" + file_day
    if os.path.isdir(path + folder):
        


