class Animals:
    def __init__(self):
        self.num_eyes = 2

    def __int__(self, eye_number):
        self.num_eyes = eye_number

    def breathe(self):
        print("inhale, exhale")


class Fish(Animals):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("move in water")

    def breathe(self):
        super().breathe()
        print("using gills")


nemo = Fish()
deer = Animals()

nemo.swim()
print(nemo.num_eyes)
nemo.breathe()
print()
deer.breathe()
print(deer.num_eyes)

