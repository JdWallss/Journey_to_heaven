import time
import sys

from character import Character
from world.world import (World)
from world.locations import StartingVillage
from world.locations import Forest
from world.locations import Plains
from world.locations import Mountains


class Game:
    def __init__(self):
        self.player = None
        self.world = World()

    # This is the logic that initialize the game
    def start_game(self):

        # Player introduction
        self.introduction()

        # Sequence to put a name to the character
        player_name = str(input("You can barely remember your name, it was something along the lines of ... "))
        self.player = Character(player_name, "A nonchalant lowkey chill guy")
        self.print_fading_text(f"Ahhh, Yess!, {self.player.name}")
        print("You can recall now ")  # Add some distance

        # Run the initial location
        self.explore()

        # Run the main decision loop
        self.main_loop()

    # Introduce the current location
    def explore(self):
        current_location = self.world.get_current_location()
        self.print_fading_text(f"\nYou look around from eyelid to eyelid across the {current_location.name}.\n")
        print(current_location)

    # This is the main loop of decisions a player can make
    def main_loop(self):
        while True:

            action = input("\nYou decide to...                         (travel/explore/inventory/quit) \n>")
            if action == "quit":
                self.print_fading_text("\nYou die from heart failure 3 \nGAME OVER")
                break

            elif action == "travel":
                direction = input("You travel...                            (north/south/east/west)\n>")
                self.world.move(direction)
                self.explore()  # Automatically show new location description

            elif action == "explore":
                # Process for exploring different places
                current_location = self.world.get_current_location()
                if isinstance(current_location, StartingVillage):
                    self.village_sequence()  # Trigger village exploration

                elif isinstance(current_location, Forest):
                    current_location.explore_forest(self.player)
                    if current_location.has_mirror and not current_location.puzzle_solved:
                        current_location.encounter_puzzle(self.player)

                elif isinstance(current_location, Plains):
                    current_location.enter_plains(self.player)# Plains exploration

                elif isinstance(current_location, Mountains):
                    # Trigger the Mount Oralion level sequence
                    current_location.start_climb(self.player)

                else:
                    self.print_fading_text("There's no one here...\n")

            elif action == "inventory":
                self.print_fading_text(self.player.display_inventory())

            else:
                self.print_fading_text("Invalid action.\n")


    def introduction(self):
        # This is the introduction to the game
        self.print_fading_text("\nThe morning breaks, casting a gentle light upon the quiet world around you. The air is still, thick with the scent of earth and dew.\n")
        self.print_fading_text(
            "You awaken in a small, humble bed, \nin a room little more than a rough hewn cabin within the sleepy village where you were born.\n")
        self.print_fading_text(
            "The room feels both familiar and foreign. \nIt has been years since you last awoke to such stillness, and yet there is something different today.\n")
        self.print_fading_text(
            "Something within you stirs, a yearning, \nan inexplicable pull to step beyond these walls.\n\n")

        self.print_fading_text(
            "The world lies before you, quiet and calm, but in your chest, a storm is rising.\n")
        self.print_fading_text("\nYou ... ")
        self.print_fading_text(
            "\n1. Sit up and ponder the strange feelings within, questioning your own existence.\n")
        self.print_fading_text("\n2. Rise swiftly, compelled by an unseen force to step into the unknown.\n")
        self.print_fading_text("\n3. Stay in bed, hoping the weight of the world will lift itself.\n")

        # Input for player decision
        choice = input("> ")

        # Handling the player's choice
        if choice == "1":
            self.print_fading_text("You sit up,  deep in thought. The questions of life swirl around you, but you feel no answers—only a growing urge to seek.\n")
        elif choice == "2":
            self.print_fading_text("You rise swiftly, filled with determination. The world calls to you, and you must answer.\n")
        elif choice == "3":
            self.print_fading_text("You hesitate, unsure of whether to leave the comfort of your bed.But the call of adventure is strong, and you cannot ignore it.\n")
        else:
            self.print_fading_text("\nPlease choose 1, 2, or 3.\n")
            self.introduction()  # Restart if the input is invalid


#Functions for each level interaction
    def village_sequence(self):
        """Runs the unique village interaction sequence."""
        while True:
            print("\nYou can: explore village, talk to elder, start journey, leave")
            action = input("> ").lower()

            if action == "explore village":
                self.world.get_current_location().explore_village(self.player)
            elif action == "talk to elder":
                self.world.get_current_location().talk_to_elder(self.player)
            elif action == "start journey":
                if self.world.get_current_location().spoke_to_elder:
                    print("With the amulet around your neck, you start your journey north to the Forest of Echoes.")
                    break  # Player can now leave the village
                else:
                    print("You cannot start your journey until you have spoken to the elder.")
            elif action == "leave":
                print("You decide to wait a little longer before leaving back home.")
                break  # Leave the village sequence
            else:
                print("Invalid action. Try again.")


    def print_fading_text(self, text, speed=0.005, fade_duration=0.03):
        for i, char in enumerate(text):
             # Simulate fading by gradually increasing the speed of text rendering'
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed + (fade_duration * (i % 2)))  # Increase speed for fluid fading
        print("")