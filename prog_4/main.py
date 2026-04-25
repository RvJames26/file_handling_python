numbers = open("prog_4/integers.txt", "r")
square_even = open("prog_4/double.txt", "w")

for line in numbers:
    num = int(line)

#even
    if num % 2 == 0:
        square = num ** 2
        print(square)
        square_even.write(str(square) + "\n")

numbers.close()
square_even.close()