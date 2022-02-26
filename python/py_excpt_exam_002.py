list_input_a = ["10", "130", "사쿠라", "1050"]

list_nb = []
for i in list_input_a:
    try:
        i = float(i)  # 변환값을 i에 다시 넣어줘야 한다, 선언만 하면 안됨
        list_nb.append(i) # 그뒤에 i를 활용해야 작동함

    except:
        pass

print("{} 안에 존재하는 숫자는".format(list_input_a))    
print("{}입니다.".format(list_nb))

