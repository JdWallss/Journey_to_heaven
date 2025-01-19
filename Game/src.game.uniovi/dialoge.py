class Dialogue:
    def __init__(self):
        self.dialogues = {
            "greeting": "Hello, traveler! How can I assist you today?",
            "goodbye": "Safe travels, adventurer!"
        }

    def start_conversation(self, character):
        print(self.dialogues["greeting"])
        response = input("(1) Ask for help, (2) Say goodbye: ")
        if response == "1":
            print("Certainly! I can guide you to the nearest village.")
        elif response == "2":
            print(self.dialogues["goodbye"])