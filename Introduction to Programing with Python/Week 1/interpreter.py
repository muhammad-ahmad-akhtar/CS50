user_input = input()

words = user_input.split(" ")
if words[1] == '+':
    print(float(int(words[0])+int(words[2])))
elif words[1] == '-':
    print(float(int(words[0]) - int(words[2])))
elif words[1] == '*':
    print(float(int(words[0]) * int(words[2])))
else:
    print(float(int(words[0]) / int(words[2])))