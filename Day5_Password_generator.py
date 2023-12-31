#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# str=""
# for n in range(nr_letters):
#   str+=random.choice(letters)

# for m in range(nr_symbols):
#   str+=random.choice(symbols)

# for l in range(nr_numbers):
#   str+=random.choice(numbers)


# print(str)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

str_list= []
for n in range(nr_letters):
  str_list+=random.choice(letters)

for m in range(nr_symbols):
  str_list+=random.choice(symbols)

for l in range(nr_numbers):
  str_list+=random.choice(numbers)


random.shuffle(str_list)
# password = "".join(str_list)     This is one way to join a letters in list into a single string or below is another method.
#print(password)

password = ""
for letter in str_list:
  password += letter
print(f"Your password is: {password}")

