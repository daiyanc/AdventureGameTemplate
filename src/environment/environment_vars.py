class Environment:
    def __init__(self, length=200, width=200):
        self.length = length
        self.width = width
        self.npcs = 1
        self.environment_boost = None

    def get_length(self):
        return self.length

    def set_length(self, length:int):
        self.length = length
        return self.length
    
    def get_width(self):
        return self.width

    def set_width(self, width:int):
        self.width = width
        return self.width

    def get_npcs(self):
        return self.npcs

    def set_npcs(self, value=int):
        self.npcs = value
        return self.npcs

    def get_boost(self):
        return self.environment_boost
    
    def set_boost(self, boost:str):
        self.environment_boost = boost
        return self.environment_boost

    length = property(get_length, set_length)
    width = property(get_length, set_length)
    npcs = property(get_npcs, set_npcs)
    environment_boost = property(get_boost, set_boost)