#PyPassword Generator:


import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n= int(input("How many letters would you like in your password?\n")) 
sym= int(input(f"How many symbols would you like?\n"))
num = int(input(f"How many numbers would you like?\n"))
pas=[]
for i in range(n):
    pas.append(r.choice(letters))
for i in range(sym):
    pas.append(r.choice(symbols))
for i in range(num):
    pas.append(r.choice(numbers))
password=""
r.shuffle(pas)
for i in range(len(pas)):
    password=password+pas[i]
    
print(password)
