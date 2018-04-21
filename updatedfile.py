import glob
import os
import sys

sistem = True
stamp = "Null"
while (sistem == True):
    list_of_files = glob.glob('C:/Users/Jo/Documents/Projek TA/*.wav') 
    latest_file = max(list_of_files, key = os.path.getmtime)
    #print latest_file
    if (stamp != latest_file):
        #do something
        stamp = latest_file
        print (latest_file)
        print (stamp)
