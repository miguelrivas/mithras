#!/usr/bin/python3

import math

def Main():
	try:
		radius = float(input("Please enter a radius: "))
		area = math.pi * radius**2
		print('Area is '+ str( area))
	
	except:
		print("You did not enter a number")

if __name__ == "__main__":
	Main()

