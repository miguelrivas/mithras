#!/usr/bin/python

choice = raw_input('What do you want to train? ')

if choice == 'mining':
	ore = raw_input('Which ore? ')

if ore == 'iron':
	currentxp = raw_input('How much XP do you have? ')
	desiredxp = raw_input('How much XP do you want to have? ')
	differencexp = int(desiredxp) - int(currentxp)
	orecount = int(differencexp) / 35

print 'You need to mine ' + str(orecount) + ' more iron ores'


