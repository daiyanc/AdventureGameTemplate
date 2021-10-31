from environment.environment_vars import Environment
import random

class Seed(Environment):
    def __init__(self):
        self.seeded_environment = {
            0: "Volcano",
            1: "Ocean",
            2: "Sky"
        }
        self.length = self.set_length(random.randint(200, 400))
        self.width = self.set_width(random.randint(200, 400))
        self.npcs = self.set_npcs(random.randint(1, 9))