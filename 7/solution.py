with open ('input.txt') as f1:
    data = list(map(str.strip, f1.readlines()))
with open('input.txt', 'w') as f1:
    for str in data:
        if str != '100':
            f1.write(str)
            f1.write('\n')