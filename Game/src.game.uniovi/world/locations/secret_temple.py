class SecretTemple:
    def __init__(self):
        self.name = "Secret Temple"
        self.description = "A hidden temple deep in the mountains, said to hold ancient secrets."
        self.available_directions = ["north"]

    def __str__(self):
        return self.description