class Person:

    def __init__(self, name, birthday, id):
        self.name = name
        self.birthday = birthday
        self.id = id

    def __str__(self):
        return "이름: " + self.name + ", 생일: " + self.birthday + ", 아이디: " + self.id

    def __repr__(self):
        return "이름: " + self.name + ", 생일: " + self.birthday + ", 아이디: " + self.id



class Employee(Person):

    def __init__(self, name, birthday, id, salary, career_year):
        super().__init__(name, birthday, id)
        self.salary = salary
        self.career_year = career_year


    def __str__(self):
        return super().__str__() + ", 연봉: " + str(self.salary) + ", 경력: " + str(self.career_year)

    def __repr__(self):
        return super().__str__() + ", 연봉: " + str(self.salary) + ", 경력: " + str(self.career_year)


employee = Employee("홍길동","12월12일","개발자",2500,0)

print(str(employee))