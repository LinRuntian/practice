class Airline(object):
	def __init__(self, name, stars):
		self.name = name
		self.stars = stars
	def get_airline_stars(self):
	 	return self.name + self.stars 

	def  get_infor(self):
		 message = "The airline name is "
		 message += self.get_airline_stars()
		 return message
		 
name = "Cathay Pacific"
Stars = " five star airline"
cathy = Airline(name, Stars)
print(cathy.get_infor())

