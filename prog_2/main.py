students = open("prog_2/students_gwa.txt", "r")
for line in students:
    data = line.split(",")
    float_data = float(data[1])
    print(data)







students.close()