def my_facto(n):
    if(n > 1):
        return n * my_facto(n-1)
    else:
        return 1  
   

a = int(input("숫자를 입력해 주세요:> " ))
print(my_facto(a))