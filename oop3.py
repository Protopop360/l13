class Jokers:
	def __init__(self, name, nose_color, bad_jokes, equipment):
		self.name = name
		self.nose_color = nose_color
		self.bad_jokes = bad_jokes
		self.equipment= equipment

	def joke(self):
		print(self.name , " почесал свой", self.nose_color, " нос и заорал" , self.bad_jokes , "Достав из кармана", self.equipment )

# def funnies(person):
sulik = Jokers("Сулик", "сизый", "А твой пап не на стекольном заводе работает?" , "сборник анекдотов 2007")
amin = Jokers("Амин", "кривой", "Так бл*т (соре за мат)", "Пистолет, который выстреливает шуткаами")

sulik.joke()
amin.joke()

class Antijokers:
	def __init__(self, name, ring, nice_hear):
		self.name = name
		self.ring = ring
		self.nice_hear = nice_hear
	def goodjoke(self):
		print(self.name, "Кто тебе подарил тебе сборник анекдотов. У меня глаза кровью исходят. Кстати у тебя ошибка в слове и почесал своим", self.ring , "Свой", self.nice_hear)

standup = Antijokers("Эльдарич", "Обручальным перстнем", "Роскошный горшок")
standup.goodjoke()