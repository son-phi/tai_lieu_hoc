# if __name__ == "__main__":
#     import sys
#     fi = open("input1.txt")
#     fo = open("output","w")
#     sys.stdin= fi
#     sys.stdout = fo
#     st= input()
#     n = int(input())
#     dt = {}
#     ans = len(st)
#     for i in range(n):
#         c,x = input().split()
#         x = int(x) -1
#         ans += (st.count(c) +x-1 )/x
#         ans = int(ans)
#     print(ans)
from math import *
#cây phân đoạn
def upd(pos,val):
    u  = p+pos-1
    t[u]= val
    while u>1:
        u>>= 1
        t[u] = gcd(t[2*u], t[2*u+1])

if __name__ == "__main__":
    #ước chung lớn nhất
    import sys
    fi = open("input2.txt")
    fo = open("output","w")
    sys.stdin= fi
    sys.stdout = fo
    n = int(input())
    p = 1 
    while p<n: p<<=1
    t = [0]*(4*n)
    a = [int(i) for i in input().split()]
    for i in range(n) : t[p+i] = a[i]
    for i in range(p-1,0,-1): t[i] = t[2*i]+ t[2*i+1]
    ans = t[1]   
    for i in range(k,n):
        upd(i%k,a[i])
    
