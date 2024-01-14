name = input("What is your name traveler? ")
print(f"Welcome, {name}! You find yourself standing in front of a mysterious castle gates.")

choice1 = input("Do you want to enter the castle? (yes/no) ").lower()

if choice1 == "yes":
    print("You open the giant gates and walk through the grand courtyard.")
    choice2 = input("As you explore further, you find a hidden staircase leading down. Do you want to go down? (yes/no) ").lower()
    if choice2 == "yes":
        print("You descend deep into the underground tunnels. After many twists and turns, you find treasure beyond imagination. You've achieved victory!")
    elif choice2 == "no":
        print("You turn away from the staircase and venture into the castle's opulent halls. Suddenly, you are captured by the dark forces. Game over.")
    else:
        print("Invalid input. Game over.")
elif choice1 == "no":
    print("You decide not to enter the castle. As you turn away, a dragon descends and takes you on an epic adventure. You've unlocked a special quest!")
else:
    print("Invalid input. The end.")
    
print(f"Thank you for your visit {name}. Please come again!")