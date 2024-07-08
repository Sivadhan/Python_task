class Story:
    def __init__(self, character):
        self.character = character

    def tell(self):
        print(f"{self.character.name}, you are in a dark forest. You can explore further or check your inventory.")

    def explore(self):
        print(f"{self.character.name} explores the forest and finds a mysterious object.")
        self.character.add_to_inventory("Mysterious Object")
