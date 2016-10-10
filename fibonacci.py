def fib(x):
    #x is a positive integer number
    if x > 1:
        return fib(x-1) + fib(x-2)
    else:
        return 1

print(fib(6))

