def tofahrenheit(c):
    f = (c * 9/5) + 32
    return f
def tocelsius(f):
    c = ((f-32)*5)/9
    return c
t = int(input())
print(t,"°C is",tofahrenheit(t),"in Fahrenheit")
print(t,"°F is",tocelsius(t),"in Celsius")
