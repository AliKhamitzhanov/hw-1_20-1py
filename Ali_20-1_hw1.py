class Car:

    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f"{self.title} {self.model} engine started!")

    def stop_engine(self):
        print(f"{self.title} {self.model} engine stoped!")

    def info(self):
        print(f"{Bmw.title}, {Bmw.model}, {Bmw.weight}, {Bmw.hp}, {Bmw.nm}, {Bmw.max_speed}, {Bmw.color}\n"
              f"{Mercedes.title}, {Mercedes.model}, {Mercedes.weight}, {Mercedes.hp}, {Mercedes.nm}, {Mercedes.max_speed}, {Mercedes.color}")


Bmw = Car('Bmw', 'x7', '3200kg', '3340', '1500', '275', 'black')
Mercedes = Car('Mercedes', 'AMG GT', '1300kg', '510', '650', '318', 'gold')

Bmw.start_engine()
Bmw.stop_engine()
Mercedes.start_engine()
Mercedes.stop_engine()
Bmw.info()
