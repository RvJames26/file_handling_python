numbers = open("prog_4/integers.txt", "r")
for line in numbers:
    num = int(line)

#even
    if num % 2 == 0:
        square = num ** 2