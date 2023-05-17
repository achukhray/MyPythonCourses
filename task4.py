import sys

filename_input = "1.txt"
filename_output = "2.txt"
fin = open(filename_input, 'r')
fout = open(filename_output, 'w')

for line in fin:

    fizz, buzz, num = (int(str) for str in line.split(' '))

    for i in range(1,num+1):
        if not i%fizz and not i%buzz:
            fout.write('FB ')
        elif not i%fizz:
            fout.write('F ')
        elif not i%buzz:
            fout.write('B ')
        else:
            fout.write(str(i)+' ')
    fout.write("\n")

fin.close()
fout.close()