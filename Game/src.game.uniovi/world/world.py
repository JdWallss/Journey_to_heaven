from .locations.starting_village import StartingVillage
from .locations.forest import Forest
from .locations.plains import Plains
from .locations.mountains import Mountains
from .locations.mountain_village import MountainVillage
from .locations.secret_temple import SecretTemple

class World:
    def __init__(self):
        # Map Layout based on the described locations
        self.map = {
            "StartingVillage": StartingVillage(),
            "Forest": Forest(),
            "Plains": Plains(),
            "Mountains": Mountains(),
            "MountainVillage": MountainVillage(),
            "SecretTemple": SecretTemple(),
        }

        # Player starts in the village
        self.current_location = "Mountains"

    def get_current_location(self):
        return self.map[self.current_location]

    def move(self, direction):
        current_location_obj = self.get_current_location()
        available_directions = current_location_obj.available_directions

        # Check if the move is valid
        if direction in available_directions:
            if direction == "north" and self.current_location == "StartingVillage":
                # Check if player is allowed to go north
                if not current_location_obj.allow_north():
                    print("\nWhy do you want to leave?")
                else:
                    print("You proceed north, towards the Forest of Echoes.")
                    self.current_location = "Forest"
            elif direction == "south" and self.current_location == "Forest":
                self.current_location = "StartingVillage"
            elif direction == "west" and self.current_location == "Forest":
                self.current_location = "Plains"
            elif direction == "north" and self.current_location == "Plains":
                self.current_location = "Mountains"
            elif direction == "east" and self.current_location == "Mountains":
                self.current_location = "MountainVillage"
            elif direction == "south" and self.current_location == "MountainVillage":
                self.current_location = "SecretTemple"
            # Add more conditions if more movement is needed in the future

            print(f"You moved {direction}. \n Now you're in the {self.get_current_location().name}.")
            self.explore()
        else:
            print("You can't move in that direction.")

    def explore(self):
        # Introduces the player to the current location and available directions.
        current_location = self.get_current_location()
        print(f"\nYou look around the {current_location.name}...")
        print(current_location)

        # Show available directions
        print("\nAvailable directions to move:")
        for direction in current_location.available_directions:
            print(f"- {direction}")