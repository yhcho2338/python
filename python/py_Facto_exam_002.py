# 19페이지 공부

def facto(n):

    if n == 1:
        return 1

    elif n > 1:
        return n * facto(n-1)

print("1!: ", facto(1))  
print("2!: ", facto(2))  
print("3!: ", facto(3))  
print("4!: ", facto(4))  
print("5!: ", facto(5))            