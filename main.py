
import random

#Header
print("Welcome to the Dice Game\nWhere it's you against the machine, you got to keep guessing until you win\nYou have to guess the machine's choice, if you matched then you win or else you lose")

Yes = True
No = True

#input a number between 1 through 6
#choice = int(input("Choose a number between 1 through 6:\n"))

#choice = int (input("Choose a number between 1 through 6: "))


game_continue = False

while not game_continue:
    choice = int(input("Choose a number between 1 through 6:\n"))
    if choice < 1 or choice > 6:
        print("Sorry invalid number\nStart over")
    machine_Choice = random.randint(1, 6)
    print(machine_Choice)
    #print(machine_Choice)
    if choice == machine_Choice:
        print("You win")
        chance = input("Do you want to play again? Y - Yes or N - No? ").lower()
        if chance == "no":
            game_continue = True
            break
    elif choice != machine_Choice:
        print("You lose!")


