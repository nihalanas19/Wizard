import random
import time
class wizard:
    def __init__(self, name):
        self.name = name
        
    def cast_spell(self):
        print(self.name + "  is casting a spell...!")
        time.sleep(2)
        
        damage = random.randint(0, 50)

        print("🔥Fireball")
        print("Damage:", damage)

wizard1 = wizard("peter")
wizard1.cast_spell()