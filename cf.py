import os
import datetime

path = "/home/fjp/Programmieren/createfolder/"

raw_path = "raw"
cals_path = "cals"
processed_path = "processed"

timestring = str(datetime.date.today())

fullpath = os.path.join(path,timestring)

print fullpath

if not os.path.exists(fullpath):
  os.mkdir(fullpath)
  os.mkdir(os.path.join(fullpath,raw_path))
  os.mkdir(os.path.join(fullpath,cals_path))
  os.mkdir(os.path.join(fullpath,processed_path))
  print "Folders created"
else:
  print "Folder exists"