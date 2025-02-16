user_input = input("camelCase: ")
print("snake_case: ", end="")
for char in user_input:
    if char.isupper():
        print(f"_{char.lower()}", end = "")
    else:
        print(char, end = "")