# 입력
def Insert(student):
    name = input("이름 입력:> ")

    if (name not in student) == True:

       kor = int(input("국어성적 입력란:> "))
       eng = int(input("영어성적 입력란:> "))
       math = int(input("수학성적 입력란:> "))
       print("성적이 정상 입력되었습니다.")

       score = kor+eng+math
       avg = round(score/3, 3)

    else:
        print("이미 존재하는 학생입니다.")
        return Insert(student)


    student[name] = [kor, eng, math, score, avg]
    person = student[name]
    return student


# 보기
def View(student):
    print("==================================================")
    print(" 점수 :  [국, 영, 수, 총점, 평균]")

    for key, value in student.items():
        print(key,":",value)
    print("==============================================+==+")

    return student


# 검색
def Search(student):
    search_name = input("검색할 학생의 이름을 입력하세요:> ")

    if(search_name in student) == True:
       print("==================================================")
       print(" 점수 :  [국, 영, 수, 총점, 평균]")   
       print(search_name,":", student.get(search_name), " ")
       print("==================================================")

    else:
        print("해당 이름이 없습니다.")
        print("다시 검색하시려면 1번, 메인 화면으로 돌아가시려면 2번을 눌러주세요.")
        num = int(input("번호 입력란:> "))
        if num == 1:
            Search(student)
        else:
            main()
    
    return student            


# 수정
def Update(student):
    update_name = input("수정할 학생의 이름을 입력하세요:> ")

    if(update_name in student) == True:
        print("국 영 수 성적 입력란:> ")

        kor, eng, math = map(int, input().split())

        score = kor+eng+math
        avg = round(score/3, 3)

        student[update_name] = [kor, eng, math, score, avg]
        person = student[update_name]

    else:
        print("해당 이름이 없습니다.")
        print("수정할 이름을 재입력 하려면 1번, 메인으로 돌아가려면 2번")
        num = int(input("번호 입력란:>"))
        if num == 1:
            Update(student)
        else:
            main()

    return student            


# 삭제
def Delete(student):
    delete_name = input("삭제할 이름을 입력하세요:> ")

    if(delete_name in student) == True:
        student.pop(delete_name)

    return student


# 메인
def main():

    student = dict()
    print()
    print("---------------------------------------------------")
    print("|             성적 관리 Tool                       |")
    print("|                         Copyed by Cho yong-ho   |")
    print("---------------------------------------------------")
    print()

    while True:
       select = int(input("1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료 \n"))

        # 성적 입력
       if select == 1:
            student = Insert(student)

       elif select == 2:
            student = View(student)

       elif select == 3:
            student = Search(student)

       elif select == 4:
            student = Update(student)

       elif select == 5:
            student = Delete(student)

       else:
            print("종료 되었습니다.")
            break

main()                        

