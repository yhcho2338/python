user_input_a = input("정수입력: ")
PI = 3.14159

if user_input_a.isdigit():  #입력 값이 숫자열인지 판별 하여 회피?

    number_input_a = int(user_input_a)

    print("원의 반지름: ", number_input_a)
    print("원의 둘레: ", 2 * PI * number_input_a)
    print("원의 넓이: ", PI * number_input_a * number_input_a)

else :
    print("정수 입력 하라는데 뭐하냐?")
