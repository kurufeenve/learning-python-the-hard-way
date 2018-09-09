import sys
from sys import argv

try:
	script, input_file = argv
except:
	sys.exit("Please, enter the filename to read from.")

def	print_all(f):
	print(f.read())

def	rewind(f):
	f.seek(0) #this probably return carriage to the beginning of the file.

def	print_a_line(line_count, f):
	print(line_count, f.readline(), "") #"" here to avoid doble \n.

try:
	current_file = open(input_file)
except:
	sys.exit(f"Check whether the file {input_file} exists")

print("First let's print whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:\n")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
