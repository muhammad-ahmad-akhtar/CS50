while True:
    try:
        fraction = input("Fraction: ")
        num1, num2 = fraction.split("/")
        if num1 > num2:
            continue
        percentage = int((int(num1) / int(num2)) * 100)
        break
    except EOFError:
        continue
    except ZeroDivisionError:
        continue

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(percentage,"%", sep='')