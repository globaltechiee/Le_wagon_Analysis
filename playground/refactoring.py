# PSEUCODE
#formula for perimeter
#formula for area
#perimeter = 3.14 * 2 * radius
#area =  3.14 * radius * radius
  
from math import pi


# radius = int(input("Enter a number for radius to get the area "))
def circle_math(radius):
    
    perimeter = 2 * pi * radius
    area = pi * radius**2

    return [perimeter, area]

print(circle_math(5))
print(circle_math(6))


