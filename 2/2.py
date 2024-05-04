data = []
with open('input.txt') as f1:
    for line in f1:
        if line[0] == 'a' or line[0] == 'A':
            data.append(line)
with open('output.txt', 'a+') as f2:
    for i in data:
        f2.write(i)
