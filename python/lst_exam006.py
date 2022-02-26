list_a = [1,2,3]


# 연결 연산자로 수행시
output = list_a + list_a

print("연결 연산자로 수행")
print("원본: ", list_a)
print("연산결과: ", output)
print()


# extend로 수행시
output = list_a.extend([1,2,3])
print("extend로 수행")
print("원본: ", list_a)
print("연산결과: ", output) # 연산식이 없으면 연산결과값을 내놓지 못한다

# 연산식에 의한 공간을 만들어주지 않고 붙였기때문에