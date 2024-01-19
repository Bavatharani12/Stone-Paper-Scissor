import random
user=0
computer=0
choice=["stone","paper","scissor"]
while True:
    user_choice=input("Choose stone or paper or scissor or exit")
    user_choice.lower()
    if(user_choice=="exit"):
        quit()
    randnum=random.randint(0,2)
    comp_choice=choice[randnum]
    print("Computer :",comp_choice)
    if(user_choice=="stone" and comp_choice=="scissors"):
        print("You won")
        user+=1
    elif(user_choice=="paper" and comp_choice=="stone"):
        print("You won")
        user+=1
    elif(user_choice=="scissor" and comp_choice=="paper"):
        print("You won")
        user+=1
    else:
        print("You lost")
        computer+=1
    print("Your score:",user)
    print("Computer score:",computer)
        
        
