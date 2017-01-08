#monster list
import random

lv1 = random.randint(1,5)
lv2 = random.randint(1,10)
lv3 = random.randint(1,20)
lv4 = random.randint(1,50)
 




class Enemy():
	def __init__(self, name, description, hp, attack):
		self.name = name
		self.description = description
		self.hp = hp
		self.attack = attack

		def is_alive(self):
			return self.hp > 0

class Goblin(Enemy):
	def __init__(self):
		super().__init__("Goblin", "A small creature", 100, 5, random.randint(1,5))

#Goblin = Enemy("Goblin", "A small creature", 100, (random.randint(1,5)))


