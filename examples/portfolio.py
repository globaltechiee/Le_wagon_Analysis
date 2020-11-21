# pylint: disable=missing-docstring

aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]
#       count, val
#       volume, strike price

portfolio = [ aapl, goog, tsla, fb ]

print('FB: ', portfolio[3][1])

#            AAPL     GOOG    TSLA      FB
market = [ 198.84, 1217.93, 267.66, 179.06 ]

#TSLA P&L
volume = portfolio[2][0]

price_bought = portfolio[2][1] * volume

market_price = market[2] * volume

pl_tsla = market_price - price_bought
print ('pl TSLA: ', pl_tsla)

print ('-------------------------')
pnl = []

for elem in portfolio:
  #print('elem', elem)
  price = elem[1] * elem[0]
  #print('price', price)

  mkt = market[portfolio.index(elem)] * elem[0]
  print('mkt', mkt)
  pnl.append(mkt - price)
  print('-')

print('-----')
print('PNL: ', pnl)
print('Total PNL:', sum(pnl))


# Another version with enumerate
pnl_2 = []
for elem, product in enumerate(portfolio):
    price = product[0] * product[1]
    mrkt = market[elem] * product[0]
    pnl_2.append(round(mrkt - price, 2))

    print(f"P&L: {(pnl_2)}")
print(f"Total P&L: {sum(pnl_2, 2)}")