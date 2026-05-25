import random

print("===== ROCK PAPER SCISSOR GAME =====")

choices = ["rock", "paper", "scissor"]

uscore = 0
cscore = 0

while True:

    uch = input("Enter rock / paper / scissor: ").lower()
    cch = random.choice(choices)

    print("Computer Choice:", cch)

    if uch not in choices:
        print("Invalid Choice")
        continue

    if uch == cch:
        print("Game Draw")
        uscore += 1
        cscore += 1

    elif ((uch == "rock" and cch == "scissor") or
          (uch == "paper" and cch == "rock") or
          (uch == "scissor" and cch == "paper")):

        uscore += 2
        print("You Win")
    else:
        cscore += 2
        print("Computer Wins")

    print("Your Score:", uscore)
    print("Computer Score:", cscore)

    ch = input("Do you want to continue? (yes/no): ").lower()

    if ch == "no":
        break

print("\n===== FINAL SCORE =====")
print("Your Score:", uscore)
print("Computer Score:", cscore)

if uscore > cscore:
    print("Overall Winner: You")
elif cscore > uscore:
    print("Overall Winner: Computer")
else:
    print("Match Draw")