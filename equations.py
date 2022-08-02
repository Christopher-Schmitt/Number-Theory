# Author: Christopher Schmitt
# Equations
# Description: Elementary Number Theory equations/solutions using elementary algorithms.
def gcd(x,y):
    # y = xq + r
    if x == 0 and y == 0:
        return float(inf) 
    elif x == 0:
        return y
    elif y == 0:
        return x
    else:
        r = 1
        while (r!=0):
            r = y % x
            y = x
            x = r
    
        return y  


def coprime_lc(a,b):
    assert gcd(a,b) == 1
    if a <= b:
        return coprime_lc_imp(a,b, (0,1), (1,0), b, a)
    else:
        ans = coprime_lc_imp(b,a, (0,1), (1,0), a, b)
        return (ans[1], ans[0])

def coprime_lc_imp(a,b, s_one, s_two, a_one, a_two):
    
    #6409(0) + 42823(1) = 42823 (s_one[0]*a + s_one[1]*b = a_one)
    #6409(1) + 42823(0) = 6409 (s_two[0]*a + s_two[1]*b = a_two) this becomes a_one
    #6409(-6) + 42823(1) = 4369 This becomes a_two
    #6409(7) + 42823(-1) = 2040
    #6409(-20) + 42823(3) = 289
    #
    
    assert a <= b
    if (a*s_one[0] + b*s_one[1] == 1):
        return s_one
    elif (a*s_two[0] + b*s_two[1] == 1):
        return s_two
    else:
        #a_one = a_two * q + r
        r = a_one % a_two
        q = int((a_one - r)/a_two)
        a_one = a_two
        a_two = r
        
        temp = (s_two[0], s_two[1])
        s_two = (s_one[0] - s_two[0] * q, s_one[1] - s_two[1] * q)
        s_one = temp
        
        return coprime_lc_imp(a, b, s_one, s_two, a_one, a_two)

def diophantine(a,b,c):
    #ax + by = c
    d = gcd(a,b)
    if c % d != 0:
        return None
    else:
        answer = coprime_lc(int(a/d),int(c/d))
        return (answer[0]*c, answer[1]*c)

def inverse_modulo(a,n):
    #ax + ny = 1
    if gcd(a,n) != 1:
        return None
    else:
        return (coprime_lc(a,n)[0] % n)
    



