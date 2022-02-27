def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

students = [
    create_student("A", 87, 98, 88, 95),
    create_student("B", 92, 98, 96, 98),
    create_student("C", 76, 96, 94, 90),
    create_student("D", 98, 92, 96, 92),
    create_student("E", 95, 98, 98, 98),
    create_student("F", 64, 88, 92, 92),
    create_student("G", 82, 86, 98, 88),
    create_student("H", 88, 74, 78, 92),
    create_student("I", 97, 92, 88, 95),
    create_student("J", 45, 52, 72, 78)
]    
    

def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_get_avg(student):
    return student_get_sum(student) / 4

def student_to_String(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_avg(student))




print("이름", "총점", "평균", sep="\t")
for student in students:

    print(student_to_String(student))





