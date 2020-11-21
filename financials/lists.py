# pylint: disable=missing-docstring

aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

portfolio = [ aapl, goog, tsla, fb ]

# print(portfolio)
#getting the number of fb stocks  
# fb_portf = portfolio[3][0]
# print(fb_portf)

#            AAPL     GOOG    TSLA      FB
market = [ 198.84, 1217.93, 267.66, 179.06 ]

#TSLA PnL
# volume = portfolio[2][0]
# print(volume)

# price_bought = volume * portfolio[2][1]
# print(price_bought)

# market_price = volume * market[2]
# print(market_price)
# pnl = market_price - price_bought
# print(pnl)

# print(f"Volume bought: {volume}")
# print(f"Total paid: {round(price_bought)}")
# print(f"Current price * Volume: {market_price}")
# print(f"The P & L of TSLA: {round(pnl, 2)}")

# do this with all products

pnl_2 = []
for index, product in enumerate(portfolio):
    price = product[0] * product[1]
    mrkt = market[index] * product[0]
    pnl_2.append(round(mrkt - price, 2))

print(f"P&L: {(pnl_2)}")
print(f"Total P&L: {sum(pnl_2, 2)}")

