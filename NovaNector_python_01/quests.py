def start_quest(character, inventory):
    print(f"{character.name}, you have been given a quest.")
    quest = "Find the ancient sword in the cave."
    print(f"Quest: {quest}")

    if "Mysterious Object" in character.inventory:
        print("You use the Mysterious Object to find the hidden entrance to the cave.")
        inventory.add_item("Ancient Sword")
    else:
        print("You need the Mysterious Object to complete this quest.")
