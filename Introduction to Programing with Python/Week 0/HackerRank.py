num_of_values = int(input().strip())

for _ in range(num_of_values):
    sum = 0
    number = int(input().strip())
    for num in range(number):
        if num >= 3:
            if num % 3 == 0 or num % 5 == 0:
                sum += num
    print(sum)