import sys
from sys import argv
from os.path import exists

try:
	script, from_file, to_file = argv
except:
	sys.exit("Please, enter the filename from wich to copy and the filename to\
where to copy.")

try:
	indata = open(from_file).read()
	#or in_file = open(from_file); indata = in_file.read()
except:
	sys.exit(f"Please, check whether the file {from_file} exists.")

print(f"Copying from {from_file} to {to_file}")
print(f"The input file is {len(indata)} bytes long")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
