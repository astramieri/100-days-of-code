class Animal():
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

    def move(self):
        print("Move")


class Fish(Animal):
    def __init__(self):
        super().__init__()  # This is recommended, but not strictly required

    def breathe(self):
        super().breathe() # "Extending"
        print("Underwater")

    def move(self):
        print("Move in water.") # Override


nemo = Fish()
nemo.breathe()
nemo.move()
