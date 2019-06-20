from collections import defaultdict
print("Input 5 2 then input a, a, b, a, b, a, b")
n, m = map(int, input().split(' '))

#inputNums = [5, 2]
#input1 = ['a', 'a', 'b', 'a', 'b']
#input2 = ['a', 'b']

input1 = list()
for i in range(n):
    input1.append(input())

    input2 = list()
for i in range(m):
    input2.append(input())

d = defaultdict(list)

for i in range(n):
    d[input1[i]].append(i+1)

for i in input2:
    if i in d:
        print(*d[i])
    else:
        print(-1)