class StudentsGwa:

    def __init__(self, file_path):
        self.file_path = file_path
        self.highet_gwa = 5.00
        self.top_student = ""

    def process_students(self):
        students = open("prog_2/students_gwa.txt", "r")

        for line in students:
            data = line.split(",")
            float_data = float(data[1])
            
            if float_data < self.highet_gwa:
                self.highet_gwa = float_data
                self.top_student = data[0]

        print(f"The student who have the highest GWA is {self.top_student}, that have {self.highet_gwa}")

        students.close()
