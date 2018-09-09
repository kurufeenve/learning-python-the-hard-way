import sys
from sys import argv

try:
	script, filename = argv
except:
	sys.exit("Please, eneter only filename after the name of the program.")

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
#this part with the while cycle is not necessary here. Wrote it here for the future to remember.
target = None
while (target == None):
	target = open(filename, 'w')
	if target == None:
		print(f"Please, check whether the file {filename} exists.")
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()

