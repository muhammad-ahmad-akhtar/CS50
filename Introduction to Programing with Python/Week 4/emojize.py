import emoji

user_input = input("Input: ")
if user_input == ':thumbsup:':
    user_input = ':thumbs_up:'
output = emoji.emojize(user_input)
print(f"Output: {output}")
