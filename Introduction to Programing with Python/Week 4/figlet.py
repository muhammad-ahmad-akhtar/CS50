import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

randomize = False
if len(sys.argv) == 1:
    randomize = True
if len(sys.argv) == 2:
    sys.exit(1)
if len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    randomize = False
else:
    sys.exit(1)
if not sys.argv[2] in fonts:
    print("Invalid Font Selected")
    sys.exit(2)

user_input = input("Input: ")

if randomize:
    style = random.choice(fonts)
    figlet.setFont(font=style)
else:
    figlet.setFont(font=sys.argv[2])

print(figlet.renderText(user_input))