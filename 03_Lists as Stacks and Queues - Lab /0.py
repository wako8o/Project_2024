sequence = [1, 1, 1, 2, 2, 3, 1, 1]

compressed = []
symbol = []
count = 0

for current in sequence:

    if not symbol:
        symbol.append(current)
        count += 1

    elif current == symbol[0]:
        count += 1

    else:
        compressed.append((symbol[0], count))
        symbol = []
        count = 0
        symbol.append(current)
        count += 1

compressed.append((symbol[-1], count))
print(compressed)