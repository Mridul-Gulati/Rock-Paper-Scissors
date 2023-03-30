import random


score=0
score_comp=0
while(score!=5 and score_comp!=5):
    
    user=input("Enter the value: Rock/Paper/Scissors/Quit  ")
    comp=random.choice(["Rock","Paper","Scissors"])
    if(user=="quit"):
        break
    print(f"YOU: {user}")
    print(f"COMPUTER: {comp}\n
          ")
    
    if(comp.lower()=="rock" and user.lower()=="paper"):
        score+=1
        print(f"Your score: {score} \t\t Comp score: {score_comp}")
        print("\n")
    elif(comp.lower()=="rock" and user.lower()=="rock"):
        score+=0
        print(f"Your score: {score} \t\t Comp score: {score_comp}")
        print("\n")
    elif(comp.lower()=="rock" and user.lower()=="scissors"):
        score_comp+=1
        print(f"Your score: {score} \t\t Comp score: {score_comp}")
        print("\n")
    elif(comp.lower()=="scissors" and user.lower()=="paper"):
        score_comp+=1
        print(f"Your score: {score} \t\t Comp score: {score_comp}")
        print("\n")
    elif(comp.lower()=="scissors" and user.lower()=="scissors"):
        score+=0
        print(f"Your score: {score} \t\t Comp score: {score_comp}")
        print("\n")
    elif(comp.lower()=="scissors" and user.lower()=="rock"):
        score+=1
        print(f"Your score: {score} \t\t Comp score: {score_comp}")
        print("\n")
    elif(comp.lower()=="paper" and user.lower()=="paper"):
        score+=0
        print(f"Your score: {score} \t\t Comp score: {score_comp}")
        print("\n")
    elif(comp.lower()=="paper" and user.lower()=="scissors"):
        score+=1
        print(f"Your score: {score} \t\t Comp score: {score_comp}")
        print("\n")
    elif(comp.lower()=="paper" and user.lower()=="rock"):
        score_comp+=1
        print(f"Your score: {score} \t\t Comp score: {score_comp}")
        print("\n")
    else:
        print("The value you enterd is wrong")
if(score==5):
    print("YOU WIN")
else:
    print("YOU LOST")
        
