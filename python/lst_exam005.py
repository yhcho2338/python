array=[1, 2, 3]

# append 뒤에 요소를 추가
array.append(4)
array.append(5)
print(array)

print()


# insert 필요한 위치에 요소 추가
array.insert(1, 40)
print(array)


# extend 리스트에 많은 요소를 합치기
list_a = [1,2,3]
list_a.extend([10, 20, 30])
print("[1,2,3].extend([10,20,30]) = ", list_a)