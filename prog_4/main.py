class Numbers:

    numbers = open("prog_4/integers.txt", "r")
    square_even = open("prog_4/double.txt", "w")
    cube_odd = open("prog_4/triple.txt", "w")

    for line in numbers:
        num = int(line)

    #even_square
        if num % 2 == 0:
            square = num ** 2
            print(square)
            square_even.write(str(square) + "\n")

    #odd_cube
        if num % 2 == 1:
            cube = num ** 3
            print(cube)
            cube_odd.write(str(cube) + "\n")


    numbers.close()
    square_even.close()
    cube_odd.close()