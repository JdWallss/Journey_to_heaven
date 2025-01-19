import sys
import time


class StartingVillage:
    def __init__(self):
        self.name = "Starting Village"
        self.description = ("You stand in the center of your village, a small, peaceful place surrounded by "
                            "the wilderness. The sun is rising, casting a golden light on the cobblestone streets. "
                            "Ahead of you, the road north leads to the Forest of Echoes, but you can also visit the "
                            "village elder or explore the surroundings.")
        self.available_directions = ["north"]  # Only north leads out to the forest
        self.explored = False
        self.has_amulet = False
        self.spoke_to_elder = False

    def __str__(self):
        return self.description

    def explore_village(self, player):
        if self.explored:
            self.print_fading_text(
                "\nYou've already explored the village and gathered what it has to offer. \nNothing more stirs in the quiet corners.")
        else:
            self.print_fading_text(
                "\nby with deliberate steps, you take your time to explore the village, \nwandering through familiar paths that now feel distant, as if shrouded in a thin veil of mystery.")
            self.print_fading_text(
                "\nAs your footsteps echo along the deserted lanes, your gaze is drawn to an old, abandoned house \nwith Its windows darkened, its door slightly ajar as though inviting yet foreboding.")

            choice = input("\nYou enter the house (yes/no)\n> ").lower()

            if choice == "yes":
                self.print_fading_text(
                    "\nTaking a deep breath, you push open the creaking door and step inside. \nDust dances in the shafts of light that pierce through the dilapidated walls. \nAs your eyes adjust, you notice something faintly glowing in the dimness.")
                self.print_fading_text(
                    "\nThere, lying on the floor as if discarded by time itself, is a Mysterious Amulet, \nPulsing faintly with an energy you cannot quite understand.")
                player.add_to_inventory("Mysterious Amulet")
                self.print_fading_text(
                    "\nWith reverence, you pick up the amulet, feeling its warmth seep into your hand. \nThe weight of it seems to settle not just in your palm but in your very soul.")
            else:
                self.print_fading_text(
                    "\nA chill runs through you, and you decide it's best to leave the house undisturbed, \nIts secrets left to the shadows that claim it.")

            self.explored = True

    def talk_to_elder(self, player):
        self.print_fading_text(
            "\nYou make your way to the elder’s hut, a modest abode perched at the village’s edge. \nThe air feels heavier here, as if burdened by the weight of years and wisdom.")
        self.print_fading_text(
            "\nThe village elder, an old man with a beard like silver threads spun by time itself, \nSits quietly, gazing into the distance as though he sees beyond the horizon, into realms untouched by mortal eyes.")

        self.print_fading_text(
            '\nElder: "I knew you would come, Alaric. \nYour heart is restless, your mind full of questions for which you seek answers not of this world."')

        choice = input(
            'Do you seek advice from the elder or leave him to his silent contemplation? (advice/leave): \n>').lower()

        if choice == "advice":
            self.print_fading_text(
                '\nElder: "The path you walk is one that will test not just your body, but your soul. \nThe amulet, it is more than a trinket \nIt is a key to doors unseen, a guide through the darkness that lies ahead."')

            if "Mysterious Amulet" not in player.inventory:
                player.add_to_inventory("Mysterious Amulet")
                self.print_fading_text(
                    "\nGiving a knowing smile, the elder hands you the Mysterious Amulet, the warmth of his hand lingering on the metal as you take it.")
            else:
                self.print_fading_text(
                    "\nThe elder glances at the amulet you already carry. \nHe nods slowly, his eyes filled with a wisdom beyond words, as though he understands the trials you will face.")

            self.spoke_to_elder = True
        else:
            self.print_fading_text(
                "\nYou bow slightly, a silent farewell, and leave the elder to his musings, \nfeeling both lighter and heavier with the weight of unspoken words.")

    def allow_north(self):
        return self.spoke_to_elder

    def print_fading_text(self, text, speed=0.005, fade_duration=0.03):
        for i, char in enumerate(text):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed + (fade_duration * (i % 2)))  # Increase speed for fluid fading
        print("")