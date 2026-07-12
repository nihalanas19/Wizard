import random
import time
class wizard:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def show_health(self):
        print(self.name, "has", self.health, "health.")
    
    def cast_spell(self):
        spell = random.choice(["🔥Fireball", "🧊Ice Blast", "⚡Lightning", "🌪️Wind Slash"])
        print(self.name, "is preparing a spell...")
        time.sleep(2)
        print(self.name, "casts", spell + "!")
        print("✨ The spell was successful!")
      

    def introduce(self):
        print("Hello! I am", self.name)

wizard1 = wizard("Nihal", 100)
wizard2 = wizard("Merlin", 80)
wizard3 = wizard("Harry", 120)

wizard1.introduce()
wizard1.show_health()
wizard1.cast_spell()

wizard2.introduce()
wizard2.show_health()
wizard2.cast_spell()

wizard3.introduce()
wizard3.show_health()
wizard3.cast_spell()