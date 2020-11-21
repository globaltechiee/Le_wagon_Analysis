# pylint: disable=missing-docstring

# TODO: 1st exercise: Define the `forward_price` function

# define a function called forward_price
# PSEUCODE
# forward_price
# The function receives takes arguments (spot, interest_rate, time)
#Those 3 parameters we need to compute as equation
# multiply the spot by interest_rate * time


import math
import time

def forward_price(spot, interest_rate, time):

    exponent = interest_rate * time
    result = spot * math.exp(exponent)

    return round(result, 2)
print(forward_price(100, 0.02, 5 )) # => 110.52
print(forward_price(100, 0, 5))   # => 100



# TODO: 2nd exercise: Define the `short_pnl` function
# PSEUCODE
# function takes 2 arguments (positions, mtm)
# 1st arg: list of prices (positions)
#2nd arg: list of the current market value of each asset
# Examples
# position: [100,140,200]
# mtm:      [110,120,180] 

#example test
#(110-100) + (120-140) + (180-200) = -30
def short_pnl(positions, mtm):
    # define an empty list
    diff = []
    # iterate through positions
    # access element and index using enumerate
    for index, i in enumerate(positions):
        diff.append(mtm[index]- i)
    print(diff)
    return sum(diff)

print(short_pnl([100,140,200],[110,120,180]))

# we are accessing list and index

#         mtm(f"index: {index}")

#     PL = positions - mtm
#     return pl
    
# print(short_pnl(positions, mtm))