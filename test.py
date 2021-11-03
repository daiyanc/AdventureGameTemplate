from src.character.defaults import Character
from src.environment import room_seed

plyr1 = Character()
print("Player", plyr1)

npc1 = Character(10, 1, 5, 0)
print("NPC", npc1)

room1 = room_seed()
print(room1)