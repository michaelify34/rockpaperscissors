#directory name: rpslab_git
import random as rand

choice = input("Which do you choose? \n1. rock\n2. paper\n3. scissors\n")

opponentchoice = rand.choice(["rock", "paper", "scissors"])
print(opponentchoice)

if choice == "rock":
    if opponentchoice == "rock":
        print("Tie")
    elif opponentchoice == "paper":
        print("You lose!")
    elif opponentchoice == "scissors":
        print("You win!")