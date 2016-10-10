def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        power = base*0 + 1
    else:
        power = 1
        while exp > 0 :
            power *= base
            exp -= 1
    return power

print(iterPower(89,5))
