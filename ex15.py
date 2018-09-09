import sys
from sys import argv

try:
	script, filename = argv
except:
	sys.exit("Please, eneter one filename after name of the program")

try:
	txt = open(filename)
except:
	sys.exit(f"""Failed to open a file {filename}.
Please, check whether this file exists""")

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

print("Please, type the filename again:")
file_again = input("> ")

try:
	txt_again = open(file_again)
except:
	sys.exit(f"""Failed to open a file {file_again}.
Please, check whether this file exists""")

print(txt_again.read())
txt_again.close()

