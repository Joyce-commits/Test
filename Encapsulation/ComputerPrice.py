class Computer:
	def __init__(self):
		self.__maxprice = 900   # private instant attribute
	
	def sell(self):
		print("Selling price : ", self.__maxprice)

	# setter function
	def setMaxPrice(self, price):
		self.__maxprice = price  # private instant attribute

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()