#!/usr/bin/python


# What is important here is how to define functions in python



def askStuff():
	stuff = raw_input('What is your favorite stuff? ')
	return stuff

def sayStuff():
	print 'Look I am saying stuff. ' + askStuff()  + ' is nice and i like it.'


sayStuff()
