string = list(input())

for letter in range(len(string)):
    if len(string) == 0:
        break
    print(string.pop(), end="")