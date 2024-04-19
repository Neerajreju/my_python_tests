# ceaser cyphher
#taking a the message and converting in to cypher by shifting that

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

encrypted= []
decrypted=[]

def encrypt(user_input , shift_position):
    for i in user_input:
        if i ==" " :
            encrypted.append(" ")
        position = alphabet.index(i)
        new_position = (position+shift_position)%26
        new_letter= alphabet[new_position]
        encrypted.append(new_letter)
    string_encypted="".join(encrypted)
    print(string_encypted)

def decrypt(user_input , shift_position):
    for i in user_input:
        if i ==" " :
            continue
        pos = alphabet.index(i)
        new_pos = (pos-shift_position)%26
        new_decrpted_letter = alphabet[new_pos]
        decrypted.append(new_decrpted_letter)
    string_decrypted="".join(decrypted)
    print(string_decrypted)

cn="yes"
while cn:
    choice= input("enter operation \n1.type 'encode' to encode\n2.type 'decode' to decode")

    if choice=='encode':
        user_input= input("type the message").upper()
        shift_position = int(input("type the position"))
        encrypt(user_input , shift_position)

    elif choice=='decode':
        user_input= input("type the message").upper()
        shift_position = int(input("type the position"))
        decrypt(user_input , shift_position)
    cn = input("do you want to continue ..'YES' or 'NO'")


