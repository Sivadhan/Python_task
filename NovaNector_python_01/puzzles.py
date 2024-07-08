def solve_puzzle():
    print("You encounter a puzzle. Solve it to proceed.")
    print("What has keys but can't open locks?")
    puzzle = "What has keys but can't open locks?"
    answer = input("Your answer: ").lower()
    if answer == "keyboard":
        print("Correct! You solved the puzzle.")
    else:
        print("Incorrect. Try again later.")
