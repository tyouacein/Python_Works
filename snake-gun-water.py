import random
'''
1 for Snake
0 for Gun
-1 for Water
'''
computer = random.choice([-1,0,1])
youstr = input("Enter Your Choice: ")
youDict = {"s": 1, "g": 0, "w": -1}
reverseDict = {1: "Snake", 0: "Gun", -1: "Water"}
you = youDict[youstr]

print(f"You Choose {reverseDict[you]}\nComputer Choose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")
else:
    if((computer - you) == -1 or (computer - you) == 2):
        print("Lol! You Lose")
    else:
        print("Congratulation! You Win")
    # if(computer == -1 and you == 1):
    #     print("Congratulation! You Win")
    # elif(computer == -1 and you == 0):
    #     print("Sorry! You Lose")
    # elif(computer == 1 and you == -1):
    #     print("Sorry! You Lose")
    # elif(computer == 1 and you == 0):
    #     print("Congratulation! You Win")
    # elif(computer == 0 and you == -1):
    #     print("Congratulation! You Win")
    # elif(computer == 0 and you == 1):
    #     print("Sorry! You Lose")
    # else:
    #     print("Something went wrong")
