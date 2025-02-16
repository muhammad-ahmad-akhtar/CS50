def main():
    time_str = input("What time is it? ")
    time = convert(time_str)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time_str):
    colon_index = time_str.index(":")
    hours = float(time_str[:colon_index])
    minutes = float(time_str[colon_index + 1:])
    return hours + minutes / 60

if __name__ == "__main__":
    main()
