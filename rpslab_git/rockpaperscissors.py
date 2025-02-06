#directory name: rpslab_git
import random as rand

choice = input("Which do you choose? \n1. rock\n2. paper\n3. scissors\n")

opponentchoice = rand.choice(["rock", "paper", "scissors"])
print(opponentchoice)