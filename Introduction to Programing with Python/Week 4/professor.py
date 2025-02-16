import random

def main():
    level = get_level()
    score = 0
    for i in range(10):
        num_1, num_2 = generate_integer(level)
        answer = num_1 + num_2
        attempt = 1
        while attempt <= 4:
            if attempt == 4:
                print(f"{num_1} + {num_2} = {answer}")
                break
            try:
                solution = int(input(f"{num_1} + {num_2} = "))
            except ValueError:
                pass
            else:
                if solution == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempt += 1
    print(f"Score: {score}/10")

def get_level():
    try:
        level = int(input("Level: "))
    except ValueError or level < 1 or level > 3:
        pass
    else:
        return level

def generate_integer(level):
    num_1 = random.randint(1,9)
    num_2 = random.randint(1, 9)
    return num_1, num_2

if __name__ == "__main__":
    main()
