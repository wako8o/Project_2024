number = int(input())


for index in range(1, number + 1):
    digit = index
    special_num = 0
    while digit > 0:
        special_num += digit % 10
        digit //= 10
    if special_num in [5, 7, 11]:
        print(f'{index} -> True')
    else:
        print(f'{index} -> False')
