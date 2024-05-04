with open ('input.txt') as f1:
    data = f1.readlines()
with open('output.txt', 'a+') as f2:
    for i in data:
        f2.write(i[0])