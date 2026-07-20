# Create class

class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	# Method to print points in co-ordinate format
	def __str__(self):
		return (self.x, self.y)

# create object
p1 = Point(2,3)
print(p1.x, p1.y)

