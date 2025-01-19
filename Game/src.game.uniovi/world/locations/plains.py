import sys
import time


class Plains:
    def __init__(self):
        self.name = "Plains"
        self.description = (
            "\nYou find yourself standing at the edge of an endless plain, \nwhere the horizon melts into a pale sky. "
            "\nThe air is heavy, almost tangible, \nas if the weight of your own thoughts presses upon you. "
            "\nAhead, there are no roads, no clear paths, only an expanse of \ngolden grass shifting like whispers in the wind."
        )
        self.available_directions = ["east", "north"]
        self.correct_insight = False
        self.decisions_made = []
        self.mist_will_clear = False
        self.aimless_wander_count = 0  # Track aimless wandering choices

    def __str__(self):
        return self.description

    def enter_plains(self, player):
        self.print_fading_text(
            "\nStepping into the Plains of Reflection, you feel a strange sensation"
            "\nas though each step draws you deeper, not into the world, but into yourself."
        )

        self.print_fading_text(
            "\nThe grass, once soft and golden, now seems to ripple with unease. "
            "\nIn the distance, you see a vague outline, perhaps a figure, or maybe just a shadow. "
            "\nThere are no landmarks, only choices to be made, and each one pulls at something deep within you."
        )

        while not self.mist_will_clear:
            self.make_decision(player)

        if self.correct_insight:
            self.print_fading_text(
                "\nAs the realization dawns upon you, a gust of wind parts the grass, \nrevealing a narrow path leading towards the mountains. "
                "\nYou have found your way, not through the plains, but through yourself."
            )

    def make_decision(self, player):
        self.print_fading_text(
            "\nA question lingers in the air, unspoken yet deafening in its silence: \n'You...'"
        )
        decision = input(
            "\nWalk aimlessly (aimless), Sit and reflect (reflect), Focus on the distant outline (focus): \n> ").lower()

        if decision == "aimless":
            self.aimless_wander_count += 1
            self.print_fading_text(
                "\nYou wander through the plains, letting your thoughts drift like the wind. "
                "\nThe grass beneath your feet bends and sways, \nyet every step feels like a circle. "
                "\nNo matter how far you walk, the horizon never draws closer."
            )
            self.decisions_made.append("aimless")

            if self.aimless_wander_count >= 3:
                self.trigger_sandworm_ending()

        elif decision == "reflect":
            self.print_fading_text(
                "\nYou sit upon the earth, the grass brushing against your skin, and close your eyes. "
                "\nIn the silence, you hear the echoes of your own thoughts, the fragments of who you are. "
                "\nWhat drives you, what haunts you—these truths come not from the world but from within."
            )
            if self.check_insight(player):
                self.correct_insight = True
                self.mist_will_clear = True
            else:
                self.print_fading_text(
                    "\nBut the answers elude you. It seems there is still more to learn."
                )
            self.decisions_made.append("reflect")

        elif decision == "focus":
            self.print_fading_text(
                "\nFixing your eyes on the distant outline, you try to make sense of its shape. "
                "\nIs it a person, or merely a shadow? Each time you blink, \nthe figure shifts, becoming clearer, then dissolving again."
            )
            self.print_fading_text(
                "\nThe harder you focus, the more it evades you. \nPerhaps some things are not meant to be understood by force alone."
            )
            self.decisions_made.append("focus")

        else:
            self.print_fading_text(
                "\nUnsure of what to do, you hesitate, and the plains seem to whisper in response, \nwaiting for your next choice."
            )

    def check_insight(self, player):
        # Check if the player has made the correct introspective choices
        if "reflect" in self.decisions_made and "aimless" not in self.decisions_made:
            self.print_fading_text(
                "\nIn your reflection, you feel a shift within yourself. \nThe path forward is not one of aimless wandering, "
                "\nnor one of external focus, but of quiet understanding. \nYou realize now: it is not about finding something out there, "
                "\nbut something in here."
            )
            return True
        return False

    def trigger_sandworm_ending(self):
        self.print_fading_text(
            "\nAs you continue to wander aimlessly, the ground beneath your feet trembles ever so slightly. "
            "\nThe grass begins to part in strange, uneven patterns, as though something massive stirs beneath the surface."
        )
        self.print_fading_text(
            "\nBefore you can react, the earth erupts in a violent explosion of sand and dirt. "
            "\nA massive sandworm, its scales shimmering like molten gold, bursts from the ground. \nIts gaping maw; large enough to swallow you whole, opens wide."
        )
        self.print_fading_text(
            "\nYou try to run, but it's too late. The sandworm lunges at you with terrifying speed. In an instant, "
            "\nthe world goes dark as you're swallowed whole."
        )
        self.print_fading_text("\nGAME OVER\n")
        sys.exit()

    def print_fading_text(self, text, speed=0.005, fade_duration=0.03):
        for i, char in enumerate(text):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed + (fade_duration * (i % 2)))
        print("")