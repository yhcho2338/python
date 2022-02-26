PI = 3.14159

try: 
    number_input_a = int(input("정수입력: "))
    print("원의 반지름: ", number_input_a)
    print("원의 둘레: ", 2 * PI * number_input_a)
    print("원의 넓이: ", PI * number_input_a * number_input_a)
    
except:
    print("정수 입력 하라는데 뭐하냐?")

else :
    print("예외가 발생하지 않았습니다")

finally:
    print("일단 프로그램이 종료되었습니다")    

    