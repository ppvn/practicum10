with open ('input.txt') as f1:
    data = list(map(str.strip, f1.readlines()))
with open('output.txt', 'w') as f2:
    try:
        if len(data) - 1 == int(data[0]):
            f2.write('YES')
        else:
            f2.write('NO')
    except ValueError:
        f2.write('ERROR')