import os
import subprocess
from subprocess import call
import glob
import sys
sys.path.insert(0, 'D:/FTP/speaker')
from test4 import test1234
from soundloc import sound_loc
import wave
from shutil import copyfile
import json
import pika
'''
def check(stamp):
    try:
        wave.open(stamp)
        return 1
    except wave.Error:
        print ("could not read")
        return 0
'''

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

def sending() :
    try :
        f3 = open("data1.txt","r")
        channel.basic_publish(exchange='',
             		routing_key='kondisiruang',
                  	body=f3.read())
        return 1
        except EOFError,e:
            print("the EOFError is occured")
            return 0
        except IOError,e:
            print("the IOError is occured")
            return 0
        except pika.exceptions.AMQPChannelError,e:
            print("AMQPChannel is Error")
            return 0
        except pika.exceptions.AMQPConnectionError,e:
            print("AMQP Connection is error")
            return 0
        except pika.exceptions.AMQPError,e:
            print("AMQP error is occured")
            return 0
        except pika.exceptions.AMQPHeartbeatTimeout,e:
            print("Connection was dropped as the result of heartbeat timeout")
            return 0
        except pika.exceptions.AuthenticationError,e:
            print("The Authentication is Error")
            return 0
        except pika.exceptions.ChannelWrongStateError,e:
            print("Channel is in wrong state for requested operation")
            return 0
        except pika.exceptions.ConsumerCancelled,e:
            print("Consumer of Pika is cancelled")
            return 0


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
        copyfile(stamp_wav,'D:/FTP/localization/direct/data.wav') #copy wav file from speaker directly
		# file from reference mic ???
		
		
        os.chdir('D:/FTP/speech')
		#Run Julius for speech recognition
        call('julius-4.3.1 -input rawfile -filelist halotitan.txt -C sample.jconf > output.txt', shell = True)
        call('python parsingkata.py > perintah.txt', shell = True)
        f = open("perintah.txt","r")
        perintah = f.read() #return perintah
        print (perintah)
		#Run Speaker Recognition
        if (perintah == "HALO TITAN\n"):
            #os.chdir('D:/FTP/speaker')
            #call('python test4.py')
            test1234()
		#f3 = open("output3.txt","w")
		#f3.write(WelcomeText)
		
        f2 = open("speaker.txt","r")
        nama = f2.read() #return nama
        welcomeText = "SELAMAT DATANG" + nama + "ADA YANG BISA SAYA BANTU"
        call('balcon -n Vocalizer -f' + welcomeText, shell = True)
		
		#Run Speaker Localization
        sound_loc() #return jarak
		#JSON Data
        data = { 'nama':nama,
        'perintah':perintah,
        'lokasi' :jarak
        }
        with open('data1.txt', 'w') as outfile:  
            json.dump(data, outfile)
        
        checkConnection = sending()
		while (checkConnection == 0):
            checkConnection = sending()
		
		"""
        try :
            f3 = open("data1.txt","r")
            channel.basic_publish(exchange='',
             		routing_key='kondisiruang',
                  	body=f3.read())
        except EOFError,e:
            print("the EOFError is occured")
        except IOError,e:
            print("the IOError is occured")
        except pika.exceptions.AMQPChannelError,e:
            print("AMQPChannel is Error")
        except pika.exceptions.AMQPConnectionError,e:
            print("AMQP Connection is error")
        except pika.exceptions.AMQPError,e:
            print("AMQP error is occured")
        except pika.exceptions.AMQPHeartbeatTimeout,e:
            print("Connection was dropped as the result of heartbeat timeout")
        except pika.exceptions.AuthenticationError,e:
            print("The Authentication is Error")
        except pika.exceptions.ChannelWrongStateError,e:
            print("Channel is in wrong state for requested operation")
        exception pika.exceptions.ConsumerCancelled,e:
            print("Consumer of Pika is cancelled")		
			
					
					
        """