class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to inventory.")

    def show(self):
        print("Inventory:")
        for item in self.items:
            print(f"- {item}")
