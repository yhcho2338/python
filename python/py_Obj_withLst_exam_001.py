students = [ 
    {"name": "A", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "B", "korean": 92, "math": 98, "english": 96, "science": 98},
    {"name": "C", "korean": 76, "math": 96, "english": 94, "science": 90},
    {"name": "D", "korean": 98, "math": 92, "english": 96, "science": 92},
    {"name": "E", "korean": 95, "math": 98, "english": 98, "science": 98},
    {"name": "F", "korean": 64, "math": 88, "english": 92, "science": 92},
    {"name": "G", "korean": 82, "math": 86, "english": 98, "science": 88},
    {"name": "H", "korean": 88, "math": 74, "english": 78, "science": 92},
    {"name": "I", "korean": 97, "math": 92, "english": 88, "science": 95},
    {"name": "J", "korean": 45, "math": 52, "english": 72, "science": 78}
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_avg = score_sum / 4

    print(student["name"], score_sum, score_avg, sep="\t")