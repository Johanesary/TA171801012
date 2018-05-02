#!/usr/bin/env python
import pika
import subprocess

count0 = len (open("output.txt").readlines())
cmd= "tail -n1 output.txt > ayam.txt"
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
file = open ("ayam.txt","r")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
             		routing_key='hello',
                  	body=file.read())
print(" [x] Sent ", file.read())

while (True):
	cmd= "tail -n1 output.txt > ayam.txt"
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	file = open ("ayam.txt","r")
	
	count1 = len (open("output.txt").readlines())
	
	if (count1>count0):
		connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
		channel = connection.channel()
		channel.queue_declare(queue='hello')
		channel.basic_publish(exchange='',
                      		routing_key='hello',
                      		body=file.read())
		print(" [x] Sent ", file.read())
	
	count0 = len (open("output.txt").readlines())
	
	#connection.close()
