user_input = input("Input: ")
vowels = { "A", "E", "I", "O", "U", "a", "e", "i", "o", "u" }
print("Output: ", end="")
for char in user_input:
    if char in vowels:
        print(end="")
    else:
        print(char, end="")