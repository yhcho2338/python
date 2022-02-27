import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("지금은 봄 입니다.")

elif 6 <= month <= 8:
    print("지금은 여름 입니다.")  

elif 9 <= month <= 11:
    print("지금은 가을 입니다.")    

else:
    print("지금은 겨울 입니다.")    
