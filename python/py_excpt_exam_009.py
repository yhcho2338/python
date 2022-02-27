number = input("정수입력: ")
number= int(number)

if number > 0:

    raise NotImplementedError 
    
    # print("아직 미구현 상태입니다.") 이렇게 처리구문을 넣어주는게 좋다
    # raise는 후처리 용으로 많이 활용, 그러나 나쁜 습관
   

else:
    raise NotImplementedError   

    # print("아직 미구현 상태입니다.") 