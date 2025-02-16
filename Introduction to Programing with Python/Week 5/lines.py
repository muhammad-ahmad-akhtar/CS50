import sys


lines = 0


def check_line(row):
    if row.lstrip().startswith('#'):
        return False
    elif row.lstrip() == '':
        return False
    else:
        return True


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2 and not (".py" in sys.argv[1]):
    sys.exit("Not a Python file")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(sys.argv[1]) as file:
            for row in file:
                if check_line(row):
                    lines += 1
                    
    except FileNotFoundError:
        sys.exit("File does not exist")

print(lines)