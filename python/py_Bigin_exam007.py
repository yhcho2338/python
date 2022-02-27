def test(a, b=10, c=100):
    print(a + b + c)


test(10, 20, 30)    

test(a=10, b=100, c=200)

test(b=200, c=10, a=100)

test(10, c=200)


# 복습 후 주석 필요