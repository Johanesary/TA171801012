'''
This program is supposed to identify the location of the speaker and 
calculate the distance of the speaker relative to one reference
created 20/03/2018
'''

import pyaudio
import numpy as np
import math
import pika

CHUNK = 2**10 #chunk of data
RATE = 16000 #sampling frequency

p = pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,
              channels=1,
              rate=RATE,
              input=True,
              frames_per_buffer=CHUNK)

credentials = pika.PlainCredentials('belva','hololens')
connection = pika.BlockingConnection(pika.ConnectionParameters('10.5.26.79',5672,'/',credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
"""
def callback(ch, method, properties, body):
    L1 = float(body) #in dB
    print(L1)
    if (body != None) :
        L2 = 0 #in dB
        r1 = 0.1 #in meter
        r2 = 0 #in meter

        for i in range(int(2*16000/1024)): #go for a few seconds
            data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
            peak=np.average(np.abs(data))*2
            print(peak)
            bars="#"*int(50*peak/2**16)
            print("%04d %05d %s"%(i,peak,bars))
            L2 = 20 * math.log10(peak/32767)
            print ("%02d dB"%(L2))
            r2 = r1 * 10**(np.abs(L1 - L2)/20) #calculate the distance of the speaker by comparing the intensity dB between it and reference
            print ("%05f m"%(r2))
	
        

    #print(" [x] Received %r " %body)
"""
for i in range(int(2*16000/1024)): #go for a few seconds
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    print(peak)
    bars="#"*int(50*peak/2**16)
    print("%04d %05d %s"%(i,peak,bars))
    L2 = 20 * math.log10(peak/32767)
    print ("%02d dB"%(L2))
    #r2 = r1 * 10**(np.abs(L1 - L2)/20) #calculate the distance of the speaker by comparing the intensity dB between it and reference
    #print ("%05f m"%(r2))
    channel.basic_publish(exchange='',
                          routing_key = 'hello',
                          body = str(L2))
    print("sent[x]")
#stream.stop_stream()
#stream.close()
#p.terminate()
