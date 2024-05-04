with open('input.txt', 'r') as f1:
    data = list(map(str.strip, f1.readlines()))
with open('output.txt', 'w') as f2:
    try:
        a = int(data[0]) / int(data[1]) + int(data[2])
        f2.write(str(a))
    except ZeroDivisionError:
        f2.write('Division by 0')
    except ValueError:
        f2.write('data error')