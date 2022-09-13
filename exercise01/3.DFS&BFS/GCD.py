def gcd_recursive(x,y):
    print('x: ', x, ',y: ', y)
    if x%y ==0:
        return y
    return gcd_recursive(y,x%y)

print(gcd_recursive(192,162))