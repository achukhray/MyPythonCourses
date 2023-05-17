import sys

filename = "1.txt"
f = open(filename, 'r')

for line in f:

    fizz, buzz, num = (int(str) for str in line.split(' '))

    for i in range(1,num+1):
        if not i%fizz and not i%buzz:
            print('FB', end = ' ')
        elif not i%fizz:
            print('F', end = ' ')
        elif not i%buzz:
            print('B', end = ' ')
        else:
            print(i, end = ' ')
    print()

f.close()