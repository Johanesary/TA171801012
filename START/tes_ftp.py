#!/usr/bin/env python

import ftplib
#session = ftplib.FTP(host='192.168.88.28',user='FTP-User',passwd='hololens')
session = ftplib.FTP(host='192.168.88.22',user='voice',passwd='hololens')
file = open('/home/pi/Desktop/copy.wav','rb')                  # file to send
session.storbinary('STOR /copy.wav', file)     # send the file
file.close()                                    # close file and FTP
#print (session.retrlines('LIST'))
print (session.dir())
#session.mkd('voice')
#print (session.pwd())
#session.cwd(/voice)
#print (session.dir())
#print (session.dir())
session.quit()