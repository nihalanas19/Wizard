class Robot:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def introduce(self):
        print("Hello! My name is " + self.name)

    def show_power(self):
        print("Power:", self.power)

    def work(self):
        print(self.name, "is working")

Robot1 = Robot("Robo", "122")
Robot2 = Robot("Alpha", "90")

Robot1.introduce()
Robot1.show_power()
Robot1.work()

Robot2.introduce()
Robot2.show_power()
Robot2.work()
