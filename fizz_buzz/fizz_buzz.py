# Start with some pseudo-code!

#fizz buzz
#select number from 1 - 100
#if number is divisible by 3 
	#print(fizz)
#if number divisible by 5 
	#print(buzz)
#if number divisible 3 and 5
	#print(fizzbuzz)
#else
	
for n in range (1, 100, 1):
	if n % 3 == 0 and n % 5 == 0:
		print("fizzbuzz")

	elif n % 3 == 0:
		print("fizz")

	elif n % 5 == 0:
		print("buzz")
	
	else:
		print(n)

