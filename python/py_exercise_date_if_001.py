import datetime

now = datetime.datetime.now()
a = now.hour
b = now.minute

if now.hour < 12:
    print("지금은 오전 {}시 {}분 입니다.".format(a,b))

else : 
    print("지금은 오후 {}시 {}분 입니다.".format((int(a)-12),b)) 


