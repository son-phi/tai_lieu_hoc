from math import *
def computeGCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

def check_prime(n):
    n = int(n)
    if(n<2): return False
    for i in range(2,isqrt(n) + 1):
        if(n%i == 0): return False
    return True
# if __name__ == "__main__":
#     t = int(input())
#     while t>0:
#         a, b = map(int, input().split())
#         n = computeGCD(a,b)
#         st= str(n)
#         sum = 0
#         for i in st:
#             sum+= int(i)
#         if check_prime(sum):
#             print("YES")
#         else:
#             print("NO")
#         t-=1
a= {
    "Bach Duong":[3.21,4.19],
    "Kim Nguu": [4.20,5.20],
    "Song Tu":[5.21,6.20],
    "Cu Giai":[6.21,7.22],
    "Su Tu":[7.23,8.22],
    "Xu Nu":[8.23,9.22],
    "Thien Binh":[9.23,10.22],
    "Thien Yet":[10.23,11.22],
    "Nhan Ma":[11.23,12.21],
    "Bao Binh":[1.20,2.18],
    "Song Ngu":[2.19,3.20]
}


# if __name__ == "__main__":
#     t = int(input())
#     for _ in range(t):
#         n, m = map(int,input().split())
#         b = m+n/100
#         k =0
#         for i,j in a.items():
#             if j[0]<= b<=j[1]:
#                 print(i)
#                 k=1
#                 break
#         if k == 0:
#             print("Ma Ket")

# if __name__ == "__main__":
#     a, b = map(int, input().split())
#     lst =[]
#     for i in range(a):
#         hang = list(map(int,input().split()))
#         lst.append(hang)
#     for i in range(a):
#         for j in range(b):
#             if check_prime(lst[i][j]):
#                 lst[i][j] = 1 
#             else:
#                 lst[i][j] = 0
#     for i in range(a):
#         print(*lst[i])


if __name__ == "__main__":
    n = int(input())
    lst = list(map(int, input().split()))
    cnt=0
    for i in range(1,n):
        if lst[i] !=lst[i-1]:
            cnt+=1
            i+=1
    print(cnt)













