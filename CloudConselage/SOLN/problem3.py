n = int(input())
ls = [input() for _ in range(n)]
di = dict()
ks = []
for x in ls:
    k = ls.count(x)
    if x not in di:
        di[x] = k
        ks.append(k)
print(len(ks))
for x in ks:
    print(x,end=" ")
