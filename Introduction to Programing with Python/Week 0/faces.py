user_input = input()
for word in user_input:
    if word == ":":
        continue
    if word == ")":
        print("🙂", end= '')
    elif word == "(":
        print("🙁", end = '')
    else:
        print(word, end= '')