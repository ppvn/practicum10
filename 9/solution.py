import os
if not os.path.exists('simple'):
    os.makedirs('simple')
with open('input.txt') as f1:
    data = list(map(str.strip, f1.readlines()))
with open('simple/output.txt', 'a+') as f2:
    for i, str in enumerate(data):
        if i % 2 == 1:
            f2.write(str)
            f2.write('\n')
