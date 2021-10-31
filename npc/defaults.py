from commands import ai_commands

class NPC:
    def __init__(self, hp=10, base_stat=1, accuracy=40, block=0):
        self.hp = hp
        self.base_stat = base_stat
        self.accuracy = accuracy
        self.block = block

    def get_hp(self):
        return self.hp
    
    def set_hp(self, hp:int):
        self.hp = hp
        return self.hp

    def get_stats(self):
        return self.base_stat

    def set_stats(self, value:int):
        self.base_stat = value
        return self.base_stat

    def get_accuracy(self):
        return self.accuracy

    def set_accuracy(self, value:int):
        self.accuracy = value
        return self.accuracy

    def get_block(self):
        return self.block

    def set_block(self, value:int):
        self.block = value
        return self.block

    hp = property(get_hp, set_hp)
    stats = property(get_stats, set_stats)
    accuracy = property(get_accuracy, set_accuracy)
    block = property(get_block, set_block)