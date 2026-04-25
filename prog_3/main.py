from writing_into_life import FileWriter

class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def reading(self):
        print("File content: ")
        read_file = open("prog_3/my_life.txt", "r")
        for line in read_file:
            print(line, end="")

        read_file.close()

writer = FileWriter("prog_3/my_life.txt")
writer.writing_life()

reader = FileReader("prog_3/my_life.txt")
reader.reading()