# 자료와 함께 리턴 연습

def return_test():
    return 100

value = return_test()
print(value)



# 리턴값이 없을때의 연습

def return_test1():
    return

value2 = return_test1()
print(value2)   

# 리턴값이 없더라도 돌아와서 끝나야 한다
# 이 경우 파이썬은 None을 출력한다 
# 다른 프로그램은 오류가 뜸