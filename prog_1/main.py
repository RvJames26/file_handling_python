numbers = open("prog_1/numbers.txt", "r")
even_num = open("prog_1/even.txt", "w")
for line in numbers:
    num = int(line)

#even
    if num % 2 == 0:
        print(num)
        even_num.write(line)

#odd
    if num % 2 == 1:
        print(num)

numbers.close()
even_num.close()