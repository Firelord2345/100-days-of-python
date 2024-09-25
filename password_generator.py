import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to pypassword generator")
# pass_length=int(input("whats the length of the password?"))
letter_length=int(input("whats the length of the letter?"))
sym=int(input("How much symbols would you like?"))
num=int(input("how many numbers?"))
# Easy level
# password=""
# for char in range(1,letter_length+1):
#     password+=random.choice(letters)
# for char in range(1,sym+1):
#     password+=random.choice(symbols)
#
# for char in range(1,num+1):
#     password+=random.choice(symbols)
# Hard level
password=[]
pass1=""
for char in range(1,letter_length+1):
    password.append(random.choice(letters))
for char in range(1,sym+1):
    password.append(random.choice(symbols))

for char in range(1,num+1):
    password.append(random.choice(numbers))
random.shuffle(password)


for char in password:

    pass1+=str(char)
print(pass1)

