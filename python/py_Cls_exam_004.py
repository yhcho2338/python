class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_avg(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avg())

students = [ 
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92),
    Student("김미화", 82, 86, 98, 88),
    Student("김연화", 88, 74, 78, 92),
    Student("박아현", 97, 92, 88, 95),
    Student("서준서", 45, 52, 72, 78)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student))