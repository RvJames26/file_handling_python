class students_gwa:

    def __init__(self, students, highest_gwa, top_student):

        
        students = open("prog_2/students_gwa.txt", "r")
        highet_gwa = 5.00
        top_student = ""

        for line in students:
            data = line.split(",")
            float_data = float(data[1])
            
            if float_data < highet_gwa:
                highet_gwa = float_data
                top_student = data[0]

        print(f"The student who have the highest GWA is {top_student}, that have {highet_gwa}")

        students.close()