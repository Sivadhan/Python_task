def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Press Enter to continue...")
