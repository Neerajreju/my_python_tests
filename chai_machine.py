# chai machine
# creates 3 different types of teas
# kattan  ,  strong with milk  , milk chai
# kattan  = 100g of teapwder , 20g of sugar , 100ml of water
# strong = 150 g of tea powder , 30g of sugar , 100ml of water
#milk chai = 100g of tea powder , 40g of sugar , 70 ml of water
# coin operated only  ,  coin of 1 , 2 , 10 can only be accepted
price ={"kattan":10 , "strong":12 , "milkchai":15}
print("welcome to the CHAI MACHINE")
print(f"please pay the desired amount to enjoy your tea {price}")
print("the only available option is coin of 1  ,  2  , 5 , 10")
coin_1= int(input("enter the number of coin 1 are you paying"))
coin_2 = int(input("enter the number of coin 2 are you paying"))
coin_5 = int(input("enter the number of coin 5 are you paying"))
coin_10 = int(input("enter the number of coin 10 are you paying"))

amount = (1*coin_1)+(coin_2*2)+(5*coin_5)+(coin_10*10)

tea_dict = {"kattan": {"powder":100 , "sugar":20 , "water":100}, 
            "strong": {"powder":150 , "sugar":30 , "water":100},
            "milk_chai": {"powder":100 , "sugar":40 , "water":70},}
in_stock_items = [400 , 70 , 300]
compare_to_storing=[]
user_choice = input("enter the tea of your choice\nKATTAN\nSTRONG\nMILK CHAI").lower()

def choice(user_choice):

   # print(tea_dict[user_choice])
    for i in tea_dict[user_choice]:
        user_key = tea_dict[user_choice][i]
        compare_to_storing.append(user_key)
        
    #print(f"the values for the certain tea{compare_to_storing}")
    #to compare the with in stoch items 
    incrementer=0
    for i in in_stock_items:
        res =i - compare_to_storing[incrementer]
        if res<0:
            print("there is no enough items to make your desired type of tea")
            break
        elif res>0:
            in_stock_items[incrementer]=res
            incrementer+=1
    print("enjoy your tea")
    #print(f"in stock items renewed after the detection for making the certain tea {in_stock_items}")


# driver part
if amount>price[user_choice]:
    refund = amount - price[user_choice]
    print(f"you have paid more than the required amount and balance of {refund} will be refunded")
    choice(user_choice)
elif amount<price[user_choice]:
    print("sorry u have not paid the entire amount")

elif amount==price[user_choice]:
    choice(user_choice)

#check if the ordered item has enough stock to make
#if user_choice=="strong":



         
    
    