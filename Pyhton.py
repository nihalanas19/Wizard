import time
import random
class Wizard:
    def __init__(self, name):
        self.name = name

    def cast_spell(self):
        print(self.name + " casts a spell!")
        time.sleep(1)

        damage = random.randint(0,50)
        print("🔥Fireball")
        print("Damage:", damage)

wizard1=Wizard("Nihal")
wizard2=Wizard("Merlin")
wizard3=Wizard("Harry")
wizard1.cast_spell()
wizard2.cast_spell()
wizard3.cast_spell()