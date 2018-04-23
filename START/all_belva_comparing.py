#!/usr/bin/env python

import ftplib
import glob
import os
import sys
from shutil import copyfile

sistem = True
stamp = "Null"
#session = ftplib.FTP(host='192.168.88.28',user='FTP-User',passwd='hololens')
session = ftplib.FTP(host='192.168.43.47',user='voice',passwd='hololens')
while (sistem==True):
    list_of_files = glob.glob('/home/pi/Desktop/START/*.wav')
    latest_file = max(list_of_files, key=os.path.getmtime)
    if (stamp != latest_file):
        stamp = latest_file
        print (stamp)
        copyfile (stamp, '/home/pi/Desktop/copy.wav')
        a = 0
        b = 1
        c = 0
        while (a != b and c != 10):
            b = os.path.getsize(stamp)
            #b = os.path.getsize ('/home/pi/Desktop/copy.wav')
            print(b)
            c = c + 1
            a = os.path.getsize(stamp)
            print(a)
        if (c == 10) :
            file = open(stamp,'rb')                  # file to send
            session.storbinary('STOR /data.0000.wav', file)     # send the file
            file.close()                                    # close file and FTP
            print (session.dir())
#print (session.retrlines('LIST'))
print (session.dir())
#session.mkd('voice')
#print (session.pwd())
#session.cwd(/voice)
#print (session.dir())
#print (session.dir())
session.quit()