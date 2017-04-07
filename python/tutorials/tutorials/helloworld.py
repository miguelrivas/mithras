#!/usr/bin/python

cats = input('How many cats?')
dogs = input('How many dogs?')


#the int modifier will cast your variable to an integer
total_pets = int(cats) + int(dogs)



if int(total_pets) >= 7:
	print ('You have more than 7 pets')
else:
	print ('You are not a cat lady')



# chmod +x filename.py will allow you to run your script
