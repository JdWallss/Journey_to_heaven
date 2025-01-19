import sys
import time


class Forest:
    def __init__(self):
        self.name = "Forest of Echoes"
        self.description = (
            "You stand at the edge of the Forest of Echoes, a place where shadows dance and the trees whisper ancient secrets. "
            "The air is thick with an eerie stillness, and yet, beneath it all, there is a hum—a low, resonant murmur as if the forest itself remembers.")

        self.available_directions = ["west", "south"]
        self.explored = False
        self.has_mirror = False
        self.puzzle_solved = False

    def __str__(self):
        return self.description

    def explore_forest(self, player):
        if self.explored:
            self.print_fading_text(
                "\nThe forest remains unchanged, though the whispers feel more insistent now, \nas if aware of your presence and the trials ahead.")
        else:
            self.print_fading_text(
                "\nVenturing deeper into the forest, the trees seem to close in around you, \ntheir branches thick with moss and memory. "
                "\nThe whispers grow louder—faint voices, half-formed, echoing like forgotten songs lost to time.")
            self.print_fading_text(
                "\nAmong the roots of an ancient oak, you find something half-buried: \na **Silver Mirror**. \nIt is small, yet when you lift it, \nit feels heavier than it should, as though it carries not just reflections but truths unknown.")
            player.add_to_inventory("Silver Mirror")
            self.has_mirror = True
            self.explored = True

    def encounter_puzzle(self, player):
        if not self.puzzle_solved:
            self.print_fading_text(
                "\nAs you wander deeper, the path before you fades into mist, \nthick and impenetrable. \nThe voices of the forest, once distant, \nnow rise into a chorus of dissonance—whispers laced with fear and forgotten promises.")
            self.print_fading_text(
                "\nSuddenly, a figure materializes from the mist \na **Wraith of Echoes**, \nits form ethereal, shifting like smoke in the wind. \nIts eyes, hollow yet all-seeing, fix upon you.")
            self.print_fading_text(
                "\nWraith: 'Traveler... you seek to pass, but none may leave until they see not with their eyes, but with their soul. \nThe mirror you carry may show the way, if you are clever enough to understand.'")

            self.print_fading_text(
                "\nThe wraith gestures toward a stone altar, \nwhere ancient symbols are carved into the surface—markings you cannot decipher.")
            self.print_fading_text(
                "\nThe puzzle is clear: the mirror holds the key, but what must you reflect upon the altar? \nThe wraith fades into the mist, leaving you alone with your thoughts.")

            choice = input("\nYou aatempt to find a solution        (yes/no)\n> ").lower()

            if choice == "yes":
                self.solve_puzzle(player)
            else:
                self.print_fading_text(
                    "\nYou hesitate, uncertain of what the mirror might reveal. \nThe mist thickens, and the whispers grow louder, urging you to make a decision.")

    def solve_puzzle(self, player):
        if not self.has_mirror:
            self.print_fading_text(
                "\nYou realize that you need something reflective \nperhaps the mirror you found earlier")
            return

        self.print_fading_text(
            "\nHolding the Silver Mirror before the altar, you tilt it carefully, \ntrying to catch the right angle. \nAt first, the symbols remain cryptic, but then, as the light shifts, something changes.")
        self.print_fading_text(
            "\nIn the reflection, you no longer see the altar or the forest. \nInstead, you see **your own eyes**,\nstaring back at you, glowing faintly with an inner light. \nThe symbols in the mirror shift, taking on new forms, \nwords you now understand.")

        puzzle_answer = input("\nThe answer is... \n> ").lower()

        if puzzle_answer == "yourself" or puzzle_answer == "me" or puzzle_answer == "my reflection":
            self.print_fading_text(
                "\nThe moment you speak the truth aloud, the altar glows, \nand the mist begins to lift. \nThe wraith's voice echoes one last time, soft and distant: \n'You have seen what many cannot. \nRemember, traveler, the answer was within you all along.'")
            self.puzzle_solved = True
            self.available_directions.append("west")  # Allows exit to the next area
        else:
            self.print_fading_text(
                "\nThe symbols remain unchanged, and the mist grows thicker, as if mocking your answer. The path remains closed for now.")

    def allow_west(self):
        return self.puzzle_solved

    def print_fading_text(self, text, speed=0.005, fade_duration=0.03):
        for i, char in enumerate(text):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed + (fade_duration * (i % 2)))  # Increase speed for fluid fading
        print("")