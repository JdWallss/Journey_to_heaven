class MountainVillage:
    def __init__(self):
        self.name = "Mountain Village"
        self.description = "A remote village nestled in the mountains."
        self.available_directions = ["south", "west"]

    def __str__(self):
        return self.description