password = input("Enter your row: ")

is_digit = False
is_space = False
is_lower = False
is_upper = False

for symbol in password:
    if symbol.isdigit():
        is_digit = True
    elif symbol.isspace():
        is_space = True
    elif symbol.islower():
        is_lower = True
    elif symbol.isupper():
        is_upper = True

if is_digit and is_space and is_lower and is_upper:
    print("YES")
else:
    print("NO")
