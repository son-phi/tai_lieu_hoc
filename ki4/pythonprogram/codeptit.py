from math import *
import re

def check_prime(n):
    n = int(n)
    if(n<2): return False
    for i in range(2,isqrt(n) + 1):
        if(n%i == 0): return False
    return True

def computeGCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

def count_unique_digits(input_string):
    unique_digits_set = set()
    count_of_digits = 0

    for char in input_string:
        if char.isdigit() and char not in unique_digits_set:
            unique_digits_set.add(char)
            count_of_digits += 1

    return count_of_digits>1

def sieve_of_eratosthenes(N):
    # Tạo một danh sách boolean ban đầu với tất cả các giá trị True
    primes = [True] * (N+1)
    primes[0] = primes[1] = False  # 0 và 1 không phải số nguyên tố

    for i in range(2, int(N**0.5) + 1):
        if primes[i]:
            # Đánh dấu tất cả các bội số của i là False vì chúng không phải là số nguyên tố
            for j in range(i*i, N+1, i):
                primes[j] = False

    # Trích xuất các số nguyên tố từ danh sách primes
    prime_numbers = [num for num, is_prime in enumerate(primes) if is_prime]
    return prime_numbers




def check(a):
    st = str(a)
    if len(st)%2==1: return False
    n= len(st)
    h1 = st[:n//2]
    h2 = st[n//2:]

    if h1 != h2[::-1]: return False
    for x in st:
        if int(x)%2==1: return False
    return True


    
if __name__ == "__main__":
    t = int(input())
    while t>0:
        n = int(input())
        for i in range(10,n):
            if check(i):
                print(i,end=" ")
        print()
        t-=1

    
    

    
    


        
        


        



    
    


        

    
                

    


    


            

    


    
    
        
        
            










        
    





