# stock.py

class Stock(object):
	"""docstring for Stock"""

	__slots__ = ('name','_shares','price')
	
	def __init__(self, name, shares, price):
		super(Stock, self).__init__()
		self.name = name
		self._shares = shares
		self.price = price

	@property
	def cost(self):
		return self.shares*self.price

	@property
	def shares(self):
		return self._shares
	
	@shares.setter
	def shares(self,shares):
		if not isinstance(shares,int):
			raise TypeError("expecting int")
		self._shares = shares

	def sell(self,shares):
		self._shares -= shares

	def __repr__(self):
		return f'Stock(\'{self.name}\',{self.shares},{self.price})'

class MyStock(Stock):
	"""docstring for MyStock"""
	def panic(self):
		self.sell(self.shares)

	def cost(self):
		return 1.25*super().cost()
		