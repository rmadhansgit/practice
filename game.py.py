
import random
user_choice=int(input("what do you choose ? type 0 for rock ,1 for pappe or 2 for scissors"))

print("user choice",user_choice)

computer_choice= random.randint(0,2)

print("computer choice",computer_choice)

if user_choice==0 and computer_choice==2 :
    print ("rock smashes scissors ! you win ")
elif computer_choice==0 and user_choice==2:
    print("rock smashes scissors !you lose ")
elif user_choice>computer_choice :
    print("you lose")
elif computer_choice > user_choice:
    print("you win")
elif computer_choice==user_choice:
    print("the match is tie")
else:
    print("invalid input ! choose option 0 to 2")


