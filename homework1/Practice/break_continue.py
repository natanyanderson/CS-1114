for i in range (1,21):
    if i == 4:
        continue
    if i == 6:
        break
    print(i)
print("Finish for-loop")
num = 0
while num <= 20:
    num += 1
    if num == 4:
        continue
    if num == 6:
        break
    print(num)

num = 1
while num <= 20:
    if num == 4:
        num +=1
        continue
    if num == 6:
        break
    print(num)
    num += 1