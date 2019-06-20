s = int(8)
print("Your number is:", s)
bin1 = bin(s)
rList = []
for i in list(bin1)[2:]:
    if i == '0':
        rList.append('1')
    else:
        rList.append('0')
r = ''.join(rList)
print("Complement number is:", int(r,2))