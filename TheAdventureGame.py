#Task 1: Code Correction:Task 1: Code Correction You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

    #Task 2: Based on your corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark"< and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
if place == "cave":
    action = input("light a torch or proceed in darkness?")
    if action == "light a torch":
        print("Venture forth with torch in hand!")
    else:
        print("Slowly step into the pitch black cave.")

#Task 3: Default Path: If the user makes an invalid choice at any point, incorporate a pass statement to handle it. HINT: How can an else statement be of use here?

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
if place == "cave":
    action = input("light a torch or proceed in darkness?")
    if action == "light a torch":
        print("Venture forth with torch in hand!")
    pass #had a lot of issues with pass statement. May need to schedule a 1-on-1 as this one is leaving me very confused.
print("Slowly step into the pitch black cave.")
