user_input = input()
for word in user_input:
    if word == ' ':
        print('...', end = '')
        continue
    print(word, end = '')