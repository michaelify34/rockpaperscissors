#directory name: rpslab_git
import random as rand

choice = input("Which do you choose? \n1. rock\n2. paper\n3. scissors\n")
if not choice == "rock":
    raise ValueError("Please type rock, paper, or scissors")
elif not choice == "paper":
    raise ValueError("Please type rock, paper, or scissors")
elif not choice == "scissors":
    raise ValueError("Please type rock, paper, or scissors")

opponentchoice = rand.choice(["rock", "paper", "scissors"])
print(opponentchoice)

if choice == "rock":
    if opponentchoice == "rock":
        print("Tie")
    elif opponentchoice == "paper":
        print("You lose!")
    elif opponentchoice == "scissors":
        print("You win!")
elif choice == "paper":
    if opponentchoice == "rock":
        print("You win!")
    elif opponentchoice == "paper":
        print("Tie")
    elif opponentchoice == "scissors":
        print("You lose!")
elif choice == "scissors":
    if opponentchoice == "rock":
        print("You lose!")
    elif opponentchoice == "paper":
        print("You win!")
    elif opponentchoice == "scissors":
        print("Tie")

