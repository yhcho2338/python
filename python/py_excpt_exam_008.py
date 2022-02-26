list_number = [52, 273, 32, 72, 100]

try:
    number_input_a = int(input("정수 입력: "))

    print("{}번째 요소: {}".format(number_input_a, list_number[number_input_a]))

except ValueError as exception:
    print("정수를 입력하세요!")
    print(type(exception), exception)

except IndexError as exception:
    print("리스트의 인덱스 범위를 벗어났어요!")
    print(type(exception), exception)

except Exception as exception:
    print("미처 파악하지 못한 예외가 발생했습니다!")
    print(type(exception), exception)