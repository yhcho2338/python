String = input("입력 : ")
String = float(String)  #이런식도 가능하지만 깔끔하지 못함

print("입력 + 100: ", String + 100) 

# input() 함수는 입력값을 모두 문자열로 인식
# 숫자를 활용하고자 할땐 integer로 형변환(cast) 필요 


# 형변환 방식 001

input_a = int(input("입력i: "))
input_b = float(input("입력f: "))

print("입력i - 100: ", input_a - 100)
print("입력f * 2: ", input_b * 2)



