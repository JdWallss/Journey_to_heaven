import sys
import time


class Mountains:
    def __init__(self):
        self.name = "Mount Oralion"
        self.faced_inner_demons = False
        self.description = (
            "The air thins as you approach the base of Mount Oralion, \na towering giant whose peak is lost in the clouds. "
            "The path before you is steep and treacherous, carved from stone older than time itself. "
            "The weight of your journey presses upon you, \nyet the whisper of destiny lingers in the back of your mind. "
            "This is where your true test begins.")
        self.has_started_climb = False
        self.has_seen_the_storm = False
        self.nearing_peak = False
        self.choices_made = 0  # Tracks the depth of choices made
        self.spoke_to_hermit = False
        self.inner_vision = False

    def __str__(self):
        return self.description

    def start_climb(self, player):
        self.print_fading_text(
            "\nTaking cautious steps, you begin your ascent. \nEach foothold is a challenge, the rocks slick with mist, "
            "\nand your breath grows shallow in the thin air. \nThe world below fades into a distant memory as the mountain consumes your focus.")

        self.print_fading_text(
            "\nHours pass, or perhaps days—time is elusive here. \nYou pause on a narrow ledge, gazing down at the forest "
            "\nand desert you have already crossed. \nThe vastness of your journey strikes you, yet there is so much farther to go.")

        self.print_fading_text(
            "\nA low rumble echoes from above. Dark clouds gather, \ncasting the path ahead into shadow. "
            "Do you press on, trusting in your strength, or do you seek shelter and wait out the storm?")

        self.decision_storm(player)

    def decision_storm(self, player):
        choice = input("\nYou continue... (climb/shelter)\n> ").lower()

        if choice == "climb":
            self.print_fading_text(
                "\nIgnoring the gathering storm, you press onward. \nEach step becomes heavier as the winds howl and the sky darkens. "
                "\nLightning flashes, illuminating the jagged cliffs in stark relief. \nBut your resolve is iron, and you climb higher still.")
            self.has_started_climb = True
            self.choices_made += 1
            self.face_storm(player)
        elif choice == "shelter":
            self.print_fading_text(
                "\nYou take refuge in a small cave, its entrance hidden beneath an overhang of rock. \nAs the storm rages outside, "
                "\nyou close your eyes and feel the mountain’s ancient pulse beneath your feet, \nas if it whispers secrets only the patient may hear.")
            self.has_seen_the_storm = True
            self.choices_made += 1
            self.encounter_hermit(player)
        else:
            self.print_fading_text("\nThe mountain seems to wait for you to decide, \nyet the storm does not. Try again.")
            self.decision_storm(player)

    def face_storm(self, player):
        self.print_fading_text(
            "\nThe storm grows furious, rain pelting your face, \nwinds threatening to tear you from the cliffside. "
            "Your fingers slip on the slick stone,\n but something within you drives you to continue.")

        self.print_fading_text(
            "\nSuddenly, a vision floods your mind—of yourself, standing not on the mountain, but in a place that feels both familiar and foreign. "
            "\nYou see your reflection, but the face staring back is not yours. \nIt's older, wiser, and full of sorrow and joy intertwined. Who is this? Is it you?")

        choice = input(
            "\nDo you confront this vision or dismiss it as a trick of the storm? (confront/dismiss)\n> ").lower()

        if choice == "confront":
            self.print_fading_text(
                "\nYou face the vision, and it speaks without words, its thoughts mingling with yours. "
                "\n'The mountain is not your trial—it is but a reflection of the one within. \nOnly by understanding yourself can you reach the summit.'")

            self.inner_vision = True
            self.faced_inner_demons = True
            self.choices_made += 1
            self.continue_climb(player)
        else:
            self.print_fading_text(
                "\nYou dismiss the vision, focusing instead on the mountain before you. \nYet, a part of you wonders if you missed something vital.")
            self.faced_inner_demons = False
            self.choices_made += 1
            self.continue_climb(player)

    def encounter_hermit(self, player):
        self.print_fading_text(
            "\nAs the storm rages on, you hear a faint rustling from deeper within the cave. \nThere, a figure sits, cloaked in rags, "
            "\nwith eyes that gleam like distant stars. The hermit speaks in a low voice, barely more than a whisper.")

        self.print_fading_text(
            '\nHermit: "Climbing the mountain alone, are you? \nMany have tried, many have failed. Few truly understand what lies at the peak. '
            '\nAre you one of the few, or just another soul lost in search of what cannot be found?"')

        choice = input("\nDo you ask the hermit for guidance, or leave without a word? (ask/leave)\n> ").lower()

        if choice == "ask":
            self.print_fading_text(
                "\nHermit: 'Wisdom lies not in answers, \nbut in the courage to face what you do not know. "
                "The amulet you carry, it is not a key, but a mirror. \nReflect upon it, and you may find the clarity you seek.'")

            self.spoke_to_hermit = True
            self.choices_made += 1
            self.face_inner_trial(player)
        else:
            self.print_fading_text(
                "\nYou leave the hermit to his musings, \nstepping back out into the storm as it rages around you, "
                "\nunsure if you have gained or lost something in that encounter.")
            self.continue_climb(player)

    def face_inner_trial(self, player):
        self.print_fading_text(
            "\nYou leave the cave and continue your climb, \nthe storm less fierce but your thoughts more turbulent. "
            "\nThe hermit's words echo in your mind. \nAs you climb, you glance at the amulet around your neck, its faint glow pulsing in time with your heartbeat.")

        self.print_fading_text(
            "\nYou stop to reflect on the amulet's meaning, or continue your climb without pausing?")

        choice = input("\n(reflect/continue)\n> ").lower()

        if choice == "reflect":
            self.print_fading_text(
                "\nHolding the amulet in your hand, you feel a warmth spread through your chest. \nMemories flood your mind—"
                "\nnot just of this journey, but of the life you lived before, \nof decisions made and paths not taken. "
                "\nYou realize that this amulet is not a mere object; \nit is a symbol of your choices, your failures, and your triumphs.")
            self.choices_made += 1
            self.inner_vision = True
            self.continue_climb(player)
        else:
            self.print_fading_text(
                "\nYou push forward, your focus entirely on the summit. \nThe amulet pulses at your chest, "
                "\nbut you do not stop to understand its significance.")
            self.continue_climb(player)

    def continue_climb(self, player):
        self.print_fading_text(
            "\nThe storm begins to break as you near the peak. \nThe air grows colder, and the path more treacherous, "
            "\nbut a strange peace settles over you, as though the mountain itself recognizes your resolve.")

        if self.inner_vision:
            self.print_fading_text(
                "\nYou feel lighter, as though you have shed the weight of doubts that once clung to your soul. "
                "\nYour journey here is no longer just about seeking answers, \nbut about understanding the power of your own choices.")
        else:
            self.print_fading_text(
                "\nEach step is a burden, every rock a challenge. \nYou fight through the fatigue, but there is a lingering sense "
                "\nthat you have missed something vital along the way.")

        self.print_fading_text(
            "\nFinally, you reach the summit. \nThe Temple of the Eternal Flame stands before you, ancient and silent, waiting.")

        self.end_on_cliffhanger(player)

    def end_on_cliffhanger(self, player):
        self.print_fading_text(
            "\nAs you step toward the temple doors, a voice faint, yet clear whispers your name on the wind. "
            "\nBut the name it speaks is not the one you know yourself by... \nit is a name long forgotten, tied to a truth you have yet to discover.")

        self.print_fading_text("\nThe door creaks open before you. And then—darkness.")
        self.print_fading_text("\nTo be continued...")
        # Cliffhanger ending

    def print_fading_text(self, text, speed=0.005, fade_duration=0.03):
        for i, char in enumerate(text):
             # Simulate fading by gradually increasing the speed of text rendering'
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed + (fade_duration * (i % 2)))  # Increase speed for fluid fading
        print("")