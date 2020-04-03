#n = int(input())
x = input().split(",")
x = [int(item) for item in x]
for i in range(0,len(x)):
    min_idx = i
    for j in range(i+1,len(x)):
        if x[min_idx] > x[j]:
            temp = x[min_idx]
            x[min_idx] = x[j]
            x[j] = temp
print(x)
