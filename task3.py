print("Type any value")

myvalue = int(input())
reslist = []

if myvalue == 1:
    print("Result =", 1)

elif myvalue == 0:
    print("Result =", 0)

else:
    for i in range(9, 2, -1):
        if myvalue % i == 0:
            myvalue /= i
            reslist.extend([i])
    if myvalue > 9:
        print("Nothing to multiply")
    else:
        reslist.extend([myvalue])
        reslist.sort()
        print(reslist)
