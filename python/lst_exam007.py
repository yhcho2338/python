list_a = [1, 2, 3, 4, 5, 6]

print()

del list_a[2]
print("del list[2]: ", list_a) # [1, 2, 4, 5, 6]

print()

list_a.pop(3) 
print("pop(3): ", list_a)  # [1,2,4,6] 위 메소드에서 [2]가 빠졌으므로

print()