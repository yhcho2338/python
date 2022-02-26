import time

output = 0
target_scd = time.time() + 2
while time.time() < target_scd:
    output += 1
    print("2초간 반복한 횟수: ", output) 