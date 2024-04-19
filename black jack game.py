# black jack game 

# the total points to be needed is 21 cannot exceed 21
#king queen and joker will be javing 10 points
# ace will be having points 11 and 1 you can choose that vlues accordingly
import hangman_arts
import random
art = hangman_arts.black
# the user is given two cards as random
print(hangman_arts.black)
deck_of_cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace':11 }
user_list = []
computer_list =[]
q=2
Continue_cheyyano = True
while Continue_cheyyano:
    for i in range(q):
        user_key = random.choice(list(deck_of_cards))
        user_value = deck_of_cards[user_key]
        user_list.append(user_value)
        if len(user_list)>2:
            q=1
        #computerturn
        computer_key = random.choice(list(deck_of_cards))
        computer_value = deck_of_cards[computer_key]
        computer_list.append(computer_value)
        

    print(f"The cards you have {user_list} sum {sum(user_list)}")
    print(f"The computer choice {sum(computer_list)}")
    if sum(user_list)>21:
        # checking if you have the ace card in your selected cards 
        if 11 in user_list:
            user_list.remove(11)
            user_list.append(1)
            sum(user_list)
        print("you lose the game ")
        break
    elif sum(computer_list)>21:
        print("you won  the game ")
        break

    enim_continue_veno= input("do you want to get a new card from the deck or not 'Y'or'N' ").upper()
    q=1
    if enim_continue_veno =="N":
        Continue_cheyyano=False


#now computers turn to guess the two numbers
