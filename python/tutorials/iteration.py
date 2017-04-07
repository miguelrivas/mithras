#!/usr/bin/python3

def Main():
	for step in range(5):
		print(step)

	words = ['cat', 'bat', 'rat', 'hat', 'sat']
	
	for word in words:
		print(word)

	num = 0
	while num <= 0:
		num = int(input('Please enter a positive integer: '))
	
	#requires ctrl+c to stop the following infinite loop
	while True:
		print('hello')


if __name__ == "__main__":
	Main()

