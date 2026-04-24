class numbers_sort:

    def __init__(self, even, odd, numbers):
        self.even = even
        self.odd = odd
        self.numbers = numbers

    def  process_file(self):
        numbers = open("prog_1/numbers.txt", "r")
        even_num = open("prog_1/even.txt", "w")
        odd_num = open("prog_1/odd.txt", "w")
        for line in numbers:
            num = int(line)

        #even
            if num % 2 == 0:
                print(num)
                even_num.write(line)

        #odd
            if num % 2 == 1:
                print(num)
                odd_num.write(line)


        numbers.close()
        even_num.close()
        odd_num.close()
        print("Finish")

sorter = numbers_sort("prog_1/even.txt", "prog_1/odd.txt", "prog_1/numbers.txt")
sorter.process_file()