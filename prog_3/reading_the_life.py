class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def reading(self):
        print("File content: ")
        read_file = open("prog_3/my_life.txt", "r")
        for line in read_file:
            print(line, end="")

        read_file.close()