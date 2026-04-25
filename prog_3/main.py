class life_file:

    def __init__(self, file_path):
        self.file_path = file_path

    def writing_life(self):
        my_life = open("prog_3/my_life.txt", "a")

        while True:
            line = input("Enter line: ")
            my_life.write(line + "\n")

            yes_no = input("Are there more lines y/n? ")
            if yes_no == "y":
                continue
            if yes_no == "n":
                break
                read_file = open("prog_3/my_life.txt", "r")
                for line in read_file:
                    print(line)
                    read_file.close()

            
            else:
                print("Invalid input, use only y and n")

            


        my_life.close()