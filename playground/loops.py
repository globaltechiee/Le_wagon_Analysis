# for i in range(0,4):
#     print(i)

for i in range(0,10):
    print(i*2)

for letter in "Python":
    print(letter)

words = ["Cat", "beer", "python"]

for word in words:
    print(word, len(word))

import math
import time

i = 0

while i < 10:
    #time.sleep(1)
    print(f'{i} is the factorial of {math.factorial(i)}')
    i+= 1



hour = 18

#open 
# 9-12
#14-17

if (hour > 9 and hour < 12) or (hour > 14 and  hour < 17):
    print("We are open")
else:
    print("Sorry, we are closed")
   

# Use for loop if you know # of iterations
# use while when you do not know


