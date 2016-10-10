def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return base*0 + 1
    else:
        return base * recurPower(base,exp - 1)

print(recurPower(5,3))
