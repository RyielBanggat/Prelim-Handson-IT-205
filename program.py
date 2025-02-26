def describe_room():
    print("You are in a small, dimly lit room. You see a dusty bookshelf, a locked drawer, and a window.")

def examine_bookshelf():
    print("You examine the bookshelf and find an old, tattered book. Inside, you discover a small key!")
    return True

def open_drawer(has_key):
    if has_key:
        print("You use the key to open the drawer. Inside, you find a door key and escape! Congratulations!")
        return True
    else:
        print("The drawer is locked. You need a key to open it.")
        return False

def look_out_window():
    print("You look out the window and see darkness. There is no way out from here.")

def main():
    has_key = False
    escaped = False
    print("Welcome to Escape the Room!")
    describe_room()
    
    while not escaped:
        action = input("What do you want to do? (examine bookshelf, open drawer, look out window, quit): ").strip().lower()
        
        if action == "examine bookshelf":
            has_key = examine_bookshelf()
        elif action == "open drawer":
            escaped = open_drawer(has_key)
        elif action == "look out window":
            look_out_window()
        elif action == "quit":
            print("You give up. Game over.")
            break
        else:
            print("Invalid action. Try again.")
    
if __name__ == "__main__":
    main()