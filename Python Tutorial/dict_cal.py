stocks = {
	'GOOG' : 434,
	'AAPL' : 325,
	'FB'   : 54,
	'AMZN' : 623,
	'F' : 32,
	'MSFT' : 549
}

new_tuple = max(list(zip(stocks.values(), stocks.keys())))
print(new_tuple)