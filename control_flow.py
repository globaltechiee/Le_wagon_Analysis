#Can you vote

#Pseudo-code

# Define age
# if age is over or equal 18
# => tell that user can vote
# else
# => tell that user can not

# age = 28 # non-interactive
# age = int(input("How old are you "))
# if age >= 18:
# 	print(f"You are {age} which means you can vote")
# else:
# 	print(f"You are {age} which means you cannot vote")


# function
# parameters => return a value

def can_you_vote(age): # parameter
	if age >= 18:
		return f"You are {age} which means you can vote"
	else:
		return f"You are {age} which means you cannot vote"

print(can_you_vote(17))

# number ins this example called parameter
def is_even(number):
	return number % 2 == 0

# 12 for example is an argument
print(is_even(12))

import datetime

def what_time_is_it():
	return datetime.date.today()

print(what_time_is_it())


#scope
# everything in function can be used outside the function
# which is scope
def greet(first_name, last_name):
	full_name = (f"{first_name.capitalize()} 	{last_name.upper()	}")
	return f"Hello {full_name}"

print(greet("jorgE", "RomeRo"))











