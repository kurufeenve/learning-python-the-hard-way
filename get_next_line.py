import sys
from sys import argv

def	get_next_line(f):
	line = f.readline()
	return(line)

try:
	script, input_file = argv
except:
	sys.exit("Please, enter the filename to read from.")
try:
	f = open(input_file)
except:
	sys.exit(f"Check whether the file {input_file} exists")
while (True):
	line = get_next_line(f)
	print(line)
	if len(line) == 0:
		break
