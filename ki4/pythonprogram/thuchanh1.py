import re
from math import *
def check_prime(n):
    n = int(n)
    if(n<2): return False
    for i in range(2,isqrt(n) + 1):
        if(n%i == 0): return False
    return True

def mang():
    lst = []
    for i in range(1,170000):
        if check_prime(i*6 - 1):
            lst.append(i*6 - 1)
        if check_prime(i*6 +1):
            lst.append(i*6 +1)
    return lst

def main():
    lst = mang()
    t = int(input())
    while t>0:
        n = int(input())
        cnt=0
        for i in lst:
            if i<n:
                cnt+=1
            else: break
        print(cnt - 2)
        t-=1
if __name__ == "__main__":
    main()
