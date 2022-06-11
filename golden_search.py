from math import sqrt

def golden_search(fun, left,right, eps=1e-5):
    k = ( sqrt(5) - 1) / 2
    L = right - left
    xL = right - k*L
    xR = left + k*L
    while abs(L) > eps:
        if fun(xL) < fun(xR):
            right = xR; 
            xR = xL
            L = right - left
            xL = right - k*L
        else:
            left = xL
            xL = xR
            L = right - left
            xR = left + k*L  
    return (left + right)/2