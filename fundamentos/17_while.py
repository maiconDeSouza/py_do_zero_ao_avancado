number_list = list(range(1, 51))

index = 0

while index != 50:
    if number_list[index] % 2 != 0:
        index += 1
        continue
    else:
        print(number_list[index])
        index += 1
