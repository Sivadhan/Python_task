from character import Character
from story import Story
from inventory import Inventory
from puzzles import solve_puzzle
from quests import start_quest
def main():
    print("Welcome to the Adventure Game!")
    name = input("Enter your character's name: ")
    character = Character(name)

    story = Story(character)
    inventory = Inventory()

    while True:
        story.tell()
        choice = input("What do you want to do? (explore, check inventory, solve puzzle, start quest, quit): ")
        if choice == "explore":
            story.explore()
        elif choice == "check inventory":
            inventory.show()
        elif choice == "solve puzzle":
            solve_puzzle()
        elif choice == "start quest":
            start_quest(character, inventory)
        elif choice == "quit":
            print("Thanks for playing! Have a great day")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()
