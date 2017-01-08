
#adventure!!

import random, monster

p1 = random.randint(1,20)
player_health = random.randint(1,100)

def combat(p1, attack, hp, player_health):
	if p1 > attack:
		hp -= p1
	else:
		player_health -= attack


combat(p1, Goblin.attack, Goblin.hp, player_health)

print (p1)
print (player_health)
print (Goblin.hp)
print (Goblin.attack)


