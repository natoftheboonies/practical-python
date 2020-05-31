# stock.py

class Stock(object):
	"""docstring for Stock"""
	def __init__(self, name, shares, price):
		super(Stock, self).__init__()
		self.name = name
		self.shares = shares
		self.price = price

	def cost(self):
		return self.shares*self.price

	def sell(self,shares):
		self.shares -= shares

	def __repr__(self):
		return f'Stock(\'{self.name}\',{self.shares},{self.price})'

class MyStock(Stock):
	"""docstring for MyStock"""
	def panic(self):
		self.sell(self.shares)

	def cost(self):
		return 1.25*super().cost()
		