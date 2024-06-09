# ab, bc, ac = map(int,input().split())
# tong = (ab+bc+ac)//2
# a= tong - bc
# b= tong - ac
# c= tong - ab
# print("An = {}, Binh = {}, Cuong = {}".format(a,b,c), sep=", ")


# a, b = map(int, input().split())
# a*= 10 
# b*= 10 
# bongden = (a//5 + b//5)*2 
# print(bongden)


# d, s = map(int,input().split())
# print(d//s, d%s, sep="\n")


# import sys 
# fi = open("review.inp")
# sys.stdin = fi
# n = int(input())
# a = [int(i) for i in input().split()]
# ans = 0
# for i in set(a):
#     t = a.count(i)
#     ans += t*(t-1)//2
# print(ans)
# fi.close()


# from random import randint
# n, a, b = map(int, input().split())
# print(n)
# for i in range(n):
#     print(randint(a,b), end=" ")


# n = int(input())
# def square(n):
#     p = int(n**0.5 +0.1)
#     return "yes" if p*p == n else "no"
# print(square(n))


# def s_round(x, k = 0):
#     t = x+ 0.5*10**(-k)
#     return(round(t,k))
# a= 12.565
# print(s_round(a))
# print(s_round(a,2))


# n = int(input())
# a , b = 1,1
# i = 2
# while i<=n:
#     a,b = b,a+b #fibonacci
#     i+=1
# print(b)


# st1 = input()
# st2 = st1[::-1]
# if st1 == st2:
#     print("Yes")
# else :
#     print("No")


# import sys
# fi = open("input.txt")
# sys.stdin = fi
# from datetime import date
# comp = date.today()
# s = str(comp)
# yyyy = s[:4]
# mm = s[5:7]
# dd = s[8:]

# print("Computer: ", s)
# print("Europa: ", end="")
# print(dd, mm, yyyy, sep= ".")
# print("America: ", end="")
# print(dd, mm, yyyy, sep= ",")
# print("Vietnam: ", end="")
# print(dd, mm, yyyy, sep= ".")


if __name__ == "__main__":
    import sys
    fi = open("ART.INP")
    fo = open("output","w")
    sys.stdin= fi
    sys.stdout = fo
    
    n = int(input())
    x = [0]*n
    y = [0]*n
    for i in range(n):
        x[i], y[i] = map(int,input().split())
    x.append(x[0])
    y.append(y[0])
    sum = 0
    for i in range(n):
        sum+= abs(x[i] - x[i+1]) + abs(y[i]- y[i+1])
    sum-= 2*(max(x) - min(x) + max(y)- min(y))
    print(sum)
    
    

    


