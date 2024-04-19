# number guessing gam3
# you are given two levels easy and hard
#if hard you have 5 chances and for easy you have 10 chances
import random
choice=input("which level you want\nEASY\nHARD").upper()
chance=5
if choice=="EASY":
    chance = 10
    

def game(chance):
    #chancer_looker=chance
    The_chosen_number = random.randint(0 , 100)
    print(The_chosen_number)
    for i in range(0 , chance):
        user_choice = int(input("guess the number"))
        if user_choice == The_chosen_number:
            print("you have guessed the right number")
            break
        elif user_choice>The_chosen_number:
            the_guesser = user_choice-The_chosen_number
            num= (the_guesser/user_choice)*100
            if(round(num)>75):
                print("the number is very high")
            elif(round(num) in range(50 , 76)):
                print("the number is high")
            elif(round(num) in range(25 , 50)):
                print("the number is high and close")
            else:
                print("the number is high and very close")
        
        elif The_chosen_number>user_choice:
            the_guesser = The_chosen_number-user_choice
            num = (the_guesser/The_chosen_number)*100
            if(round(num)>75):
                print("the number is very low")
            elif(round(num) in range(50 , 76)):
                print("the number is low")
            elif(round(num) in range(25 , 50)):
                print("the number is low and close")
            else:
                print("the number is low and very close")
        
        chance=-1
game(chance)
              

