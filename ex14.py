from sys import argv

script, user_name = argv
prompt = '> '
a = "a "
an = "an "

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

if computer[0] == 'a' or computer[0] == 'e' or\
computer[0] == 'i' or computer[0] == 'o' or\
computer[0] == 'u' or computer[0] == 'y':
	computer = an + computer
else:
	computer = a + computer

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have {computer} computer. Nice.
Now I will find you and kill you :)
""")
