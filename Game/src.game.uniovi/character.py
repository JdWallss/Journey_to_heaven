class Character:
    def __init__(self, name, description):
        self.name = name + " Alaric"
        self.description = description
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def display_inventory(self):
        if not self.inventory:
            return "Your inventory is empty."
        else:
            inventory_list = "\n".join(f"- {item}" for item in self.inventory)
            return f"Your inventory contains:\n{inventory_list}"

    def __str__(self):
        return f"{self.name}: {self.description}"

    # Method to add items
    '''if current_location.has_item:
        item = current_location.get_item()  # Let's assume locations can have items
        self.player.add_item(item)  # Add the item to the player's inventory
        self.print_fading_text(f"\nYou found a {item} and added it to your inventory!\n")'''