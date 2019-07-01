
reverse_a = reverse_b = 0


def sort(a, b):

    if a > 0:
        a = a
        scale_a = 1
    else:
        a = -a
        scale_a = -1

    a = str(a)
    a = list(map(int, a))

    if scale_a > 0:
        a.sort(reverse=True)
    else:
        a.sort()
    s = ''.join(map(str, a))
    a = int(s)
    a1 = a * scale_a

    if b > 0:
        b = b
        scale_b = 1
    else:
        b = -b
        scale_b = -1

    b = str(b)
    b = list(map(int, b))

    if scale_b > 0:
        b.sort()
    else:
        b.sort(reverse=True)

    zeros = b.count(0)
    for i in range(zeros):
        if b[i] == 0:
            b.insert(zeros + 1, 0)
    s = ''.join(map(str, b))
    b = int(s)
    b1 = b * scale_b
    return a1, b1


def get_difference(a, b):
    a1, b1 = sort(a, b)
    res = a1 - b1
    return res


if __name__ == "__main__":
    print(get_difference(int(input()), int(input())))