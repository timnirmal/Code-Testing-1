# Function to create combinations
# without itertools
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
    c = list(arr)
    N = c[0]
    M = c[1]

    a = []
    for h in range(N):
        strinp = input()
        a.append(strinp)

    # a = ["ynnn", "nynn", "nnyn", "nnny", "nnnn"]
    # a = ["yyyyy", "yyynn", "nyyyn", "nnnny", ]
    # a = [ "yynnyy", "yynnyy", "nnyyyy", "nnyyyy", "yyyynn", "yyyynn", ]
    # a = ["ynn", "nyn", "yyn", "yny", ]

    b = []
    for i in a:
        b.append(list(i))

    # print(b)

    c = []
    for m in range(M):
        c.append(list('0'))

    # print(c)

    for i in range(len(b)):
        count = 0
        for j in range(M):
            if b[i][j] == 'y':
                c[j].append(i)

    # print(c)

    for i in c:
        i.pop(0)

    # print(c)

    comb = n_length_combo([x for x in range(N)], 3)
    # print(comb)
    # print()

    tot = len(comb)
    # print(tot)

    for i in comb:
        sub = []
        for m in range(M):
            sub.append(list('0'))

        # print()
        # print(i)
        for j in i:
            # # print(j)
            for k in range(len(c)):
                # # print(c[k])
                if j in c[k]:
                    sub[k].append(1)
                    # # print(sub)
            # if j in k
            # # print(sub)

        for i in sub:
            i.pop(0)

        # print(sub)

        for i in sub:
            if len(i) == 0:
                tot = tot - 1
                # print(tot)
                continue;

    if tot <= 0:
        print(0)
    else:
        print(tot)
