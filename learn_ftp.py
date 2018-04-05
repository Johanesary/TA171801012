import ftplib
session = ftplib.FTP(host='167.205.7.226',user='ftpimageproc|imageproc',passwd='Img0305@')
file = open('output.wav','rb')                  # file to send
session.storbinary('STOR output.wav', file)     # send the file
file.close()                                    # close file and FTP
#print (session.retrlines('LIST'))
print (session.dir())
#session.mkd('voice')
#print (session.pwd())
#session.cwd(/voice)
#print (session.dir())
#print (session.dir())
session.quit()