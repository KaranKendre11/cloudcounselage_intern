def sum_series(n):
    s = n;
    for i in range(2,n,2):
        s += (n - i)

    return s;
n = int(input())
print(sum_series(n))
