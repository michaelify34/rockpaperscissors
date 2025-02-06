#directory name: rpslab_git
import random as rand

choice = input("Which do you choose? \n1. rock\n2. paper\n3. scissors\n")


opponentchoice = rand.choice(["rock", "paper", "scissors"])

if choice == "rock":
    print(opponentchoice)
    if opponentchoice == "rock":
        print("Tie")
    elif opponentchoice == "paper":
        print("You lose!")
    elif opponentchoice == "scissors":
        print("You win!")
elif choice == "paper":
    print(opponentchoice)
    if opponentchoice == "rock":
        print("You win!")
    elif opponentchoice == "paper":
        print("Tie")
    elif opponentchoice == "scissors":
        print("You lose!")
elif choice == "scissors":
    print(opponentchoice)
    if opponentchoice == "rock":
        print("You lose!")
    elif opponentchoice == "paper":
        print("You win!")
    elif opponentchoice == "scissors":
        print("Tie")
else:
    print("Please type rock, paper, or scissors.")