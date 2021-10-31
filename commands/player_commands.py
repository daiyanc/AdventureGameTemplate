from environment import environment_vars

class PlayerCommands:
    # InDir: attack(), walk(), item_bag()

    def __init__(self, environment:environment_vars.Environment):
        self.bag = {}
        self.position = 0
        self.battle_select = {
            'Slash': 30,
            'Punch': 10
        }
        self.environment = environment


    def get_attacks(self):
        return self.battle_select

    def set_attacks(self, attacks:dict):
        if type(attacks) != dict:
            raise AttributeError("Please enter dictionary for attacks.")
    
    attacks = property(get_attacks, set_attacks)

    def item_bag(self):
        return self.bag

    def attack(self, value:str):
        print(f'Select an attack: {self.battle_select}')

        if value.title() in self.battle_select.keys:
            print(f'Player has {value}ed the opponent for {self.battle_select[value]}')
        else:
            raise AttributeError(f'{value} not in selection...')

    def walk(self, direction:str, distance=1):
        cardinal = ['East', 'West']

        if distance < 1 or distance > 100:
            raise ValueError("Invalid distance.")
        
        if direction.title() not in cardinal:
            raise AttributeError("Invalid direction.")

        if direction.title() == 'East':
            self.position += distance
            if self.position > self.environment.get_length():
                self.position -= self.environment.get_length()
        return f'Traveling {direction} for {distance} pixels...'

    def add_item(self, item:str):
        bag_index = 0
        self.bag[bag_index] = item
        bag_index += 1