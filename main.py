def n_length_combo(lst, n):
    if n == 0:
        return [[]]

    l = []
    for i in range(0, len(lst)):

        m = lst[i]
        remLst = lst[i + 1:]

        for p in n_length_combo(remLst, n - 1):
            l.append([m] + p)

    return l


# Driver code
T = int(input())

for ite in range(T):
    arr = map(int, input().split())
    d = list(arr)

    N = d[0]
    M = d[1]

    a = []
    for i in range(N):
        strinp = input()
        a.append(strinp)

    b = []
    for i in a:
        b.append(list(i))
    # print(a)
    # clear a
    del a

    """"
    c = []
    for m in range(M):
        c.append(list('0'))

    for i in range(len(b)):
        count = 0
        for j in range(M):
            if b[i][j] == 'y':
                c[j].append(i)
    """

    # print(b)
    # # print(c)

    #clear b

    """
    for i in c:
        i.pop(0)
    """

    comb = n_length_combo([x for x in range(N)], 3)

    tot = len(comb)

    for i in comb:
        # print(i)
        sub = []
        for m in range(M):
            sub.append(list('0'))

        for j in i:
            # print(j)
            # print(b[j])
            for k in range(len(b[j])):
                # print(b[j][k])
                if b[j][k] == "y":
                    # print("=======================================")
                    sub[k].append(1)
        # print(sub)
        for i in sub:
            if len(i) == 1:
                tot = tot - 1
                continue
    #del c

    if tot < 0:
        print(0)
    else:
        print(tot)
