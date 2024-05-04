with open('input.txt') as f1:
    a = f1.read()
with open('output.txt', 'a+') as f2:
    a = str(a.upper())
    f2.write(a)