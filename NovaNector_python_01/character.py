class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.strength = 10
        self.intelligence = 10
        self.inventory = []

    def __str__(self):
        return f"{self.name}: Health: {self.health}, Strength: {self.strength}, Intelligence: {self.intelligence}"

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} added to inventory.")

    def show_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(f"- {item}")
