import datetime

now = datetime.datetime.now()


if now.hour < 12:
    print("현재 시간은 {}시로 오전입니다.".format(now.hour))


print()


if now.hour >= 12:
    print("현재 시간은 {}시로 오후입니다.".format(now.hour))


