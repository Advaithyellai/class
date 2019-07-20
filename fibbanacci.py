a = [1]
f = 0
e = 1
b = int(input("Type a Number Here -    "))
c = 0
def fibb(a, f, e, b, c):
    c += 1
    if a[-1] >= b:
        print(a[0:-1])
    else:
        if c%2 == 0:
            e = f+e
            a.append(e)
            fibb(a, f, e, b, c)
        else:
            f = f+e
            a.append(f)
            fibb(a, f, e, b, c)
if b == 0:
    print("0")
else:
    fibb(a, f, e, b, c)