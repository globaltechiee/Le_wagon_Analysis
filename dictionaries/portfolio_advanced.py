# pylint: disable=missing-docstring

# TODO: start by defining a `portfolio` using a dict!



portfolio = {
			"aapl": {"volume": 10, "strike": 154.12},
			"goog": {"volume": 2,"strike": 812.56},
			"tsla": {"volume": 12,"strike": 342.12},
			"fb": {"volume": 18, "strike": 209.0}

			}


#print(portfolio)
print(portfolio["tsla"]["volume"])

print(portfolio["goog"]["strike"])



market = { "appl": 198.84,
		  "goog": 1217.93, 
		  "tsla": 267.66, 
		  "fb": 179.06
		  }

print(market)

# Compute P&L
#PSEUDOCODE
#Cal the total amount spent  (volume * strike)
amount = portfolio['tsla']['volume'] * portfolio['tsla']['strike']
#Cal the present value (volume * market_price)
current_value = portfolio['tsla']['volume'] * market['tsla']
# cal the difference between them
pl - amount - current_value

print(f"TSLA PL {pl}")

def short_pnl()

results = []
for name, pos in portfolio.items():
	# name str: 'tsla
	# pos dict: {'volume: .....'strike'}
	# for each element append the pos to the new list
	volume = pos['volume']
	results.append(market[name] - pos['strike'])
return sum(results)
# for value in portfolio.values():
	





