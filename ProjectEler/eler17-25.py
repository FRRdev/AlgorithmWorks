import math
import itertools


def eler17():
    l = 0
    M = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7,
         17: 9, 18: 8, 19: 8, 20: 6}
    N = {0: 0, 2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}
    P = {10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}
    for i in range(1, 21):
        l += M[i]
    for i in range(21, 100):
        num1 = i // 10
        num2 = int(i % 10)
        l += (N[num1] + M[num2])
    for i in range(100, 1000):
        num1 = i // 100
        num2 = int((i % 100) // 10)
        num3 = int(i % 10)
        if num2 == 1:
            ex = int(i % 100)
            l += (10 + M[num1] + P[ex])
        else:
            l += (10 + M[num1] + N[num2] + M[num3])
    l += 11
    return l


def eler18():
    arr = []
    for line in open("number.txt"):
        line = line.rstrip()
        arr_line = line.split()
        arr.append(arr_line)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = int(arr[i][j])
    print(arr)
    ans = [75]
    i = 0
    for k in range(len(arr) - 1):
        if arr[k + 1][i] > arr[k + 1][i + 1]:
            ans.append(arr[k + 1][i])
        else:
            ans.append(arr[k + 1][i + 1])
            i = i + 1
    return sum(ans)


def eler20():
    a = str(math.factorial(100))
    mas = list(a)
    mas = [int(c) for c in mas]
    return sum(mas)


def get_sum_del(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s


def eler21(n):
    res = []
    for i in range(1, n):
        if i not in res:
            temp = get_sum_del(i)
            if i == get_sum_del(temp) and i != temp:
                res.append(i)
                res.append(temp)
    return res


def eler22():
    p = open("number.txt").read()
    arr = p.split(",")
    for i in range(len(arr)):
        arr[i] = arr[i][1:][:-1]
    arr.sort()
    print(arr)
    alp = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
           'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
           'Z': 26}
    ans = []
    for i in range(len(arr)):
        suma = 0
        for c in arr[i]:
            suma += alp[c]
            answer = suma * (i + 1)
        ans.append(answer)
    return sum(ans)


def eler23():
    LIMIT = 28124
    divisorsum = [0] * LIMIT
    for i in range(1, LIMIT):
        for j in range(i * 2, LIMIT, i):
            divisorsum[j] += i
    abundantnums = [i for (i, x) in enumerate(divisorsum) if x > i]

    expressible = [False] * LIMIT
    for i in abundantnums:
        for j in abundantnums:
            if i + j < LIMIT:
                expressible[i + j] = True
            else:
                break

    ans = sum(i for (i, x) in enumerate(expressible) if not x)
    return str(ans)


def eler24():
    arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    a = list(itertools.permutations(arr))
    new_a = ["".join(c) for c in a]
    return new_a[999999]


def eler25():
    n = 4
    while len(Fibb(n)) < 1000:
        n += 1
    else:
        ans = n
    return ans


def Fibb(n):
    arr = [None] * n
    arr[0] = 1
    arr[1] = 1
    for i in range(2, n):
        arr[i] = arr[i - 2] + arr[i - 1]
    return str(arr[n - 1])
