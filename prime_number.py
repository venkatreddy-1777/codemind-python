num=int(input())
flag = False
if num == 1:
    print("not a prime")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print("not a prime")
else:
    print("prime")