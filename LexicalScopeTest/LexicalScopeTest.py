def f(n):
    def g(x):
        i = n
        while(i > 0):
            print(x)
            i -= 1
    return g

