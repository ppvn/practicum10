with open('input.txt') as f1:
    data = list(map(str.strip, f1.readlines()))
with open('output.txt', 'a+') as f2:
    for line in data:
        if len(line) > 20:
            f2.write(line)
