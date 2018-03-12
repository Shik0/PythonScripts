def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    result = 0
    maxx = max(a,b)
    return max([x for x in range(maxx,0,-1) if a%x==0 and b%x==0])
    '''
    #2nd solution
    while maxx > 0 :
        if a % maxx == 0 and b % maxx == 0:
            result = maxx
            break
        maxx -= 1
    return result
    '''
print(gcdIter(6,12))
