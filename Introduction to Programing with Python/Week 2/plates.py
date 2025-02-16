def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    elif not (s[0].isalpha() or s[1].isalpha()):
        return False
    i = -1
    j = len(s)
    for char in s:
        i += 1
        if char.isnumeric():
            if s[i-1] == "0":
                return False
            for ch in s[i:j]:
                if ch.isalpha():
                    return False

        elif char.isspace():
            return False
        elif not (char.isalpha() or char.isnumeric()):
            return False
    return True

main()