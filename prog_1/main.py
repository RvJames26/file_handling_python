numbers = open("prog_1/numbers.txt", "r")
for line in numbers:
    num = int(line)

#even
    if num % 2 == 0:
        print (num)

numbers.close()