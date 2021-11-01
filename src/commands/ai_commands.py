import random

class AiCommands:
    # InDir: attack, loot_drops()

    def __init__(self, name='Slime'):
        self.name = name
        self.loot_table = {
            0: 'Wooden Sword',
            1: '10 Gold'
        }
        self.battle_select = {
            0: 'Slash',
            1: 'Bite'
        }

    def get_name(self):
        return self.name

    def set_name(self, name:str):
        self.name = name
        return self.name

    def get_loot(self):
        return self.loot_table

    def set_loot(self, loot_table:dict):
        if type(loot_table) != dict:
            raise AttributeError("Please enter dictionary with loot values.")
        self.loot_table = loot_table
        return self.loot_table

    def get_attacks(self):
        return self.battle_select

    def set_attacks(self, attacks:dict):
        self.battle_select = attacks
        return self.battle_select

    def attack(self):
        random_select = random.randint(0, 1)
        return f'{self.name} has attacked with {self.battle_select[random_select]}!'

    def drop(self):
        random_select = random.randint(0, 1)
        return f'{self.name} has dropped {self.loot_table[random_select]}!'    

    loot = property(get_loot, set_loot)
    name = property(get_name, set_name)
    attacks = property(get_attacks, set_attacks)