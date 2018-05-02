import os
import subprocess
from subprocess import call
import glob
import sys
sys.path.insert(0, 'D:/FTP/speaker')
from test4 import test1234
import wave
from shutil import copyfile
import json
import pika

def check(stamp):
    try:
        wave.open(stamp)
        return 1
    except wave.Error:
        print ("could not read")
        return 0


"""				
credentials = pika.PlainCredentials('kondisiruang', 'kondisiruang')
parameters = pika.ConnectionParameters('167.205.7.226',
                                       5672,
                                       '/kondisiruang',
                                       credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='Aktuator')
"""
sistem = True
stamp = "Null"
while (sistem==True):
    list_of_files = glob.glob('D:/FTP/*.txt') 
    list_of_files_wav = glob.glob('D:/FTP/*.wav') 
    latest_file = max(list_of_files, key = os.path.getmtime)
    if (stamp != latest_file):
        stamp = latest_file
        stamp_wav = max(list_of_files_wav, key = os.path.getmtime)
        #print (stamp)
        #checkfile = check(stamp)
        #print(checkfile)
        #while(checkfile == 0):
            #checkfile = check(stamp)
            #print(checkfile)
        copyfile(stamp_wav,'D:/FTP/speech/data.wav')
        copyfile(stamp_wav,'D:/FTP/speaker/data.wav')
        os.chdir('D:/FTP/speech')
        call('julius-4.3.1 -input rawfile -filelist halotitan.txt -C sample.jconf > output.txt', shell = True)
        call('python parsingkata.py > perintah.txt', shell = True)
        f = open("perintah.txt","r")
        perintah = f.read()
        print (perintah)
        if (perintah == "HALO TITAN\n"):
            #os.chdir('D:/FTP/speaker')
            #call('python test4.py')
            test1234()
        f2 = open("speaker.txt","r")
        nama = f2.read()
        data = { 'nama':nama,
        'perintah':perintah
        }
        with open('data1.txt', 'w') as outfile:  
            json.dump(data, outfile)
        """
        f3 = open("data1.txt","r")
        channel.basic_publish(exchange='',
             		routing_key='kondisiruang',
                  	body=f3.read())
        """