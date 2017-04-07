#!/usr/bin/python3

def Main():
	words = ['cat', 'hat', 'that', 'fat']

	#with open as function variable. Prevents you from needing f.open, f.close	
	with open("words.txt", 'w') as f:
		for word in words:
			f.write(word + '\n')

if __name__ == "__main__":
	Main()

