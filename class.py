print("Добро пожаловать в 1917 год, развернулась жесточайшая битва за власть")

class Bolshevik:
	def __init__(self, name, hand, salary):
		self.name = name
		self.salary = salary
		self.hand = hand
	def attack(self, target):
		print(self.name ," ударил " , target.name , "с силой " , self.hand)
class Traitor:
	def __init__(self, name, hand, salary):
		self.name = name
		self.hand = hand
		self.slary = salary
	def attack(self, target):
		print(self.name ," ударил " , target.name , "с силой " , self.hand)


Lenin = Bolshevik("Ленин", 1000, 10000)
Trotski = Traitor("Троцкий", 100, 1000)

def fight(fighter1, fighter2):
	fighter1.attack(fighter2)
	fighter2.attack(fighter1)


fight(Lenin, Trotski)
