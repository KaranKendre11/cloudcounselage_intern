n1 = int(input())
n2 = int(input())
count  = 0
for i in range(1,min(n1,n2)):
    if( n1 % i == 0 and n2 % i == 0):
        count += 1
print(count)
