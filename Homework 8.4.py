import random

chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
symbol_len = int(input("Enter your password length: "))
password = ""

for i in range(symbol_len):
    password += random.choice(chars)
print("Your generated password:", password)

is_digit = False
is_alnum = False
is_lower = False
is_upper = False

for symbol in password:
    if symbol.isdigit():
        is_digit = True
    elif not symbol.isalnum():
        is_alnum = True
    elif symbol.islower():
        is_lower = True
    elif symbol.isupper():
        is_upper = True

if password == "qwerty":
    print("1")
elif password == "admin":
    print("1")
elif password == "":
    print("1")
elif is_digit and is_lower and is_upper and is_alnum and len(password) > 8:
    print("5")
elif is_digit and is_lower and is_upper or is_digit and is_lower and is_alnum:
    print("4")
elif is_digit and is_upper and is_alnum or is_lower and is_upper and is_alnum:
    print("4")
elif is_digit and is_lower or is_digit and is_upper or is_digit and is_alnum:
    print("3")
elif is_lower and is_upper or is_lower and is_alnum or is_upper and is_alnum:
    print("3")
elif password.isdigit() or password.isalnum() or password.islower() or password.isupper():
    print("2")
else:
    exit(4)
