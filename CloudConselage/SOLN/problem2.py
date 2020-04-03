y = int(input())

def is_leap(n):
    if(y%100 == 0):
        if (y%400 == 0):
            return True
        else:
            return False
    if (y % 4 == 0):
        return True
    return False

print(is_leap(y))
