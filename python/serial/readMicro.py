#!/usr/bin/python2

#imports serial file
import serial

def Main():
	try:
		port = serial.Serial('/dev/ttyACM0', 9600)
		file = open('data.txt', 'a')
		data = port.read(size=20) 	#1 byte
		print (data)
		file.write(data)
		file.close()
		
	except: 
		print('There has been an error.')	

if __name__ == "__main__":
	Main()
