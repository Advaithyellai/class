print("0")
def fibbanacci(a, f, c):
    if f+c >= a:
        print(f+c)
        return
    else:
        b = f
        d = b+c
        fibbanacci(a, d, b)
e = int(input("Number: "))
fibbanacci(e, 1, 0)