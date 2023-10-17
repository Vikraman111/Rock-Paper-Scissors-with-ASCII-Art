import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
compch = random.randint(1,3)
rounds = int(input("Enter Number of Rounds you want to Play"))
win=lost=draw=0
for i in range(rounds):
    print(f"Round {i+1}:")
    print("Choose\n1 for rock\n2 for paper\n3 for scissor")
    userch = int(input("enter choice"))
    if userch == 1:
        print("Comp Choice is",compch)
        if compch == 1:
            print(rock)
        elif compch == 2:
            print(paper)
        else:
            print(scissors)
        print("Your choice was ROCK")
        print(rock)
        if compch == 1:
            print("Draw!")
            draw+=1
            print("*******************************************************")
        elif compch ==2:
            print("Lost")
            lost += 1
            print("*******************************************************")
        elif compch == 3:
            print("Win")
            win += 1
            print("*******************************************************")
    if userch == 2:
        print("Comp Choice is", compch)
        if compch == 1:
            print(rock)
        elif compch == 2:
            print(paper)
        else:
            print(scissors)
        print("Your choice was PAPER")
        print(paper)
        if compch == 1:
            print("Win")
            win += 1
            print("*******************************************************")
        elif compch ==2:
            print("Draw")
            draw += 1
            print("*******************************************************")
        elif compch == 3:
            print("Lost")
            lost += 1
            print("*******************************************************")
    if userch == 3:
        print("Comp Choice is", compch)
        if compch == 1:
            print(rock)
        elif compch == 2:
            print(paper)
        else:
            print(scissors)
        print("Your choice was SCISSORS")
        print(scissors)
        if compch == 1:
            print("Lost")
            win += 1
            print("*******************************************************")
        elif compch ==2:
            print("Win")
            win += 1
            print("*******************************************************")
        elif compch == 3:
            print("Draw")
            draw += 1
            print("*******************************************************")
print(f"You plated a total of {rounds}")
print("Your Stats!")
print(f"WINS: {win}\nLOSS: {lost}\nDraws: {draw}")