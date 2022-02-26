def facto(n):
    output = 1

    for i in range(1, n + 1):
        output *= i
    return output


print("1!: ", facto(1))        
print("2!: ", facto(2))
print("3!: ", facto(3))          