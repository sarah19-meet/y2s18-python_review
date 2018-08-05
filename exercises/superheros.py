# Write your solutions for 1.5 here!
class Superheroes:
	def __init__(self, name,superpower, strength):
		self.name= name
		self.superpower= superpower
		self.strength=strength
	def print_me(self):
		print(self.name+str( self.strength))

superhero= Superheroes("sarah","mind reading",7)
superhero.print_me()

	
	