#!/usr/bin/python

total_cats = raw_input('How many cats do you have? ')

boy_cats = raw_input('How many of your cats are boys? ')

girl_cats = raw_input('How many of your cats are girls? ')

total_cats_calculated = int(boy_cats) + int(girl_cats)

if int(total_cats) != (total_cats_calculated):
	print ('You made a counting error')

else:
	print ('Good counting! You have a total of ' + str(total_cats_calculated) +' cats!')
