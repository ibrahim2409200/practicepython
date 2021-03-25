#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
#print out a message of congratulations to the winner, and ask if the players want to start a new game)
print("Rock Papers And Scissors")
i=True
loop="yes"
while loop=="yes":
    p1 = int(input("Player1! Enter your move: \nPress 1 for Rock \nPress 2 for Scissors \nPress 3 for Paper\n Enter here: "))
    p2 = int(input("Player2! Enter your move:\nPress 1 for Rock \nPress 2 for Scissors \nPress 3 for Paper\n Enter here: "))
    while i==True:
        if (p1 == 1 and p2 == 2):
            print("Player1 wins")
            break
        elif (p2 == 1 and p1 == 2):
            print("Player2 wins")
            break
        elif (p1 == 2 and p2 == 3):
            print("Player1 wins")
            break
        elif (p2 == 2 and p1 == 3):
            print("Player2 wins")
            break
        elif (p1 == 3 and p2 == 1):
            print("Player1 wins")
            break
        elif (p2 == 3 and p1 == 1):
            print("Player2 wins")
            break
        elif (p1 == p2):
            print("Draw")
            break
        else:
            i=False
            break
    print()

    loop=str(input("Do you wanna play again?\nType yes or no:\n"))
