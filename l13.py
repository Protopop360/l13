class Drinks:
	def __init__(self, name, color, price):
		self.name = name
		self.color = color
		self.price = price
	def smell(self):
		print("Я слышу твой запах!!")

drinks = Drinks("Чай", "Зеленый", "56")

drinks.smell()
# Drinks.smell(drinks)
print(drinks.name)
print(drinks.price)


class Juice(Drinks):
	def __init__(self, name, color, price, fruit):
		super().__init__(name, color, price)
		self.fruit = fruit
	def smell(self):
		super().smell()
		print("Эльдар, хватит")

apple = Juice("Яблочный", "Зеленый", 99, "Яблока")
apple.smell()