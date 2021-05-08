def direct_search(line: str, subline: str):
    """
    Implementing direct search
    sub_line-substring,
    line - where to search
    """
    count = 0
    flag = False
    while (len(line) >= len(subline)) and not flag:
        for index in range(len(subline)):
            if subline[index] == line[index]:
                count += 1
            else:
                count = 0
                line = line[1:]
                break
        if count == len(subline):
            flag = True
        else:
            flag = False

    return flag


def find_prefix(s):
    '''
    Finding the array P
    (for the knuth-morris-pratt algorithm)
    '''
    P = [0] * len(s)
    j = 0
    i = 1

    while i < len(s):
        if s[j] == s[i]:
            P[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                P[i] = 0
                i += 1
            else:
                j = P[j - 1]
    return P


def kmp_search(line: str, sub_line: str):
    """
    Implementation of the Knuth-Morris-Pratt algorithm
    sub_line - substring,
    line - where to search
    """
    P = find_prefix(sub_line)
    m = len(sub_line)
    n = len(line)
    i, j = 0, 0
    while i < n:
        if line[i] == sub_line[j]:
            i += 1
            j += 1
            if j == m:
                return True
        else:
            if j > 0:
                j = P[j - 1]
            else:
                i += 1
    if i == n:
        return False


def forming_d(pattern):
    """
    Forming an array d
    (for the Boyer-Moore algorithm)
    """
    d = [len(pattern) for _ in range(1105)]
    new_p = pattern[::-1]

    for i in range(len(new_p)):
        if d[ord(new_p[i])] == len(new_p):
            d[ord(new_p[i])] = i
        else:
            continue
    return d


def bm_search(line: str, sub_line: str):
    """
    The Boyer-Moore search algorithm.
    sub_line-substring,
    line - where to search
    """
    d = forming_d(sub_line)
    len_p = x = j = k = len(sub_line)
    while x <= len(line) and j > 0:
        if sub_line[j - 1] == line[k - 1]:
            j -= 1
            k -= 1
        else:
            x += d[ord(line[k - 1])]
            k = x
            j = len_p
    if j <= 0:
        return True
    else:
        return False


if __name__ == "__main__":
    line = open('line.txt').read()
    subline = 'nulla'
    print(direct_search(line, subline))
    print(kmp_search(line, subline))
    print(bm_search(line, subline))
