number_rows = int(input())

result = 0

for _ in range(number_rows):
    letters = input()
    result += ord(letters)

print(f'The sum equals: {result}')
