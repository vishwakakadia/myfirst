import random

print(" WELCOME TO THE GAME \nStone , Paper ,Scissors\n ")
print("S stands for Stone\nP stands for Paper\nI stands for Scissors")
lst = ["S","P","I"]
u_score = 0
c_score = 0
n = 0
while n <= 10:
    choice = random.choice(lst)
    user = input("computer is  guessed now it's your turn!")
    if choice == 'S' and user == 'P':
        print("Stone is caught by paper !! ")
        u_score += 1
        print("your score : ",u_score)
        print("Computer score : ",c_score)
    elif choice == 'S' and user == 'I':
        print("Scissors is broken by stone !!")
        c_score += 1
        print("your score : ", u_score)
        print("Computer score : ", c_score)
    elif choice == 'P' and user == 'S':
        print("Stone is caught by paper !!")
        c_score += 1
        print("your score : ", u_score)
        print("Computer score : ", c_score)
    elif choice == 'P' and user == 'I':
        print("Paper is cut by scissors !!")
        u_score += 1
        print("your score : ", u_score)
        print("Computer score : ", c_score)
    elif choice == 'I' and user == 'S':
        print("Scissors is broken by stone !!")
        u_score += 1
        print("your score : ", u_score)
        print("Computer score : ", c_score)
    elif choice == 'I' and user == 'P':
        print("Paper is cut by scissors !!")
        c_score += 1
        print("your score : ", u_score)
        print("Computer score : ", c_score)
    else:
        print("oh no , you guess same as computer ")
        print("your score : ", u_score)
        print("Computer score : ", c_score)
    n += 1
print("\nyour total Score  : ",u_score)
print("Computer total Score : ",c_score)
if u_score > c_score:
    print("congratulations.....you won the game")
elif u_score < c_score:
    print("sorry , you lost the game\n better luck for next time")
else:
    print("it's is tie !!!")






