# import sys
#
# user_input = input("Greting: ").strip().title()
# words = user_input.split()
# for word in words:
#     if word == "Hello":
#         print("$0")
#         sys.exit()
# for word in words:
#     for char in word:
#         if char == "H":
#             print("$20")
#             sys.exit()
# print("$100")

greeting = input("Greeting: ").strip().lower()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h") and not greeting.startswith("hello"):
    print("$20")
else:
    print("$100")
