N = int(input())

print()
v = []
for _ in range(N):
    arr = map(int, input().split())
    arr = list(arr)
    print(arr)
    u = [0] * N
    for k in range(arr[0] - 1, arr[1]):
        u[k] = 1
    v.append(u)

print(v)

f = []
for i in range(N):
    print(v[i])
    h = []
    for j in range(N):
        print("   k")
        print(v[i][j])
        if v[i][j] == 1:
            g = [0] * N
            g[j] = 1
            h.append(g)

    print(h)
    f.append(h)

print(f)

d = []
for i in range(N):
    c = [0] * N
    d.append(c)

for i in range(N):
    d[i][i] = 1

print(d)

print()
print(v)

ch = [0] * N

for i in range(len(v)):
    for j in range(N):
        print("v j ")
        print(v[i])
        print(v[j])
        if v[j][j] == 1:
            ch[i] = i
            v.pop(i)
            for k in range(len(v)):
                v[k][j] = 0

print(ch)
print(v)

# didn't work sadly
