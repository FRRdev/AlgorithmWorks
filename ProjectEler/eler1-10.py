import math


def Eler1():
    ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
    return ans

def Eler2():
    f1, f2, s = 1, 2, 0
    while f2 <= 4000000:
        s = s + f2 if f2 % 2 == 0 else s
        f1, f2 = f2, f1 + f2
    return s

def Eler3(a):
    r = math.ceil(math.sqrt(a))
    lst = []
    for i in range(3, r):
        if a % i == 0:
            if Eler3(i) == []:
                lst.append(i)
    return lst


def Eler4():
    arr1 = [k for k in range(100, 1000)]
    arr2 = arr1[:]
    local_max = 0
    for k in range(len(arr1)):
        for i in range(len(arr2)):
            number = arr1[k] * arr2[i]
            number_to_str = str(number)
            if number_to_str[::-1] == number_to_str:
                local_max1 = number
                if local_max1 > local_max:
                    local_max = local_max1
    return local_max


def Eler5():
    maxRange = 20
    lst = range(maxRange, 0, -1)
    count = 1
    sum = maxRange
    lstcount = lst[count]
    while lstcount != 1:
        tmp = sum
        while sum % lstcount != 0:
            sum += tmp
        count += 1
        lstcount = lst[count]
    return sum


def Eler6():
    sum1 = sum(i ** 2 for i in range(1, 101))
    sum2 = pow(sum(i for i in range(1, 101)), 2)
    rez = sum2 - sum1
    return rez


def Eler7():
    simpl_arr = []
    a = 2
    while len(simpl_arr) <= 10000:
        d = 2
        while d * d <= a and a % d != 0:
            d += 1
        if d * d > a:
            simpl_arr.append(a)
        a += 1
    return simpl_arr[-1]


def digit_product(s):
    result = 1
    for c in s:
        result *= int(c)
    return result


def Eler8():
    NUMBER = open("number.txt").read()
    ADJACENT = 13
    return max(digit_product(NUMBER[i: i + ADJACENT]) for i in range(len(NUMBER) - ADJACENT + 1))


def Eler9():
    PERIMETER = 1000
    for a in range(1, PERIMETER + 1):
        for b in range(a + 1, PERIMETER + 1):
            c = PERIMETER - a - b
            if a * a + b * b == c * c:
                return str(a * b * c)


def Eler10(n=20000000):
    sieve = list(range(n))
    sieve[1] = 0
    for i in sieve[2:]:
        for j in range(i + i, len(sieve), i):
            sieve[j] = 0
    return sieve
