def myFunc(f, val):
    print(f'{f.__name__}, {val}')
    return f(val)

myFunc(min, [1,2,3,4])
