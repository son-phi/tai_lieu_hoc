import math

# int 0
# str 'Tim'
# bool True, False
# float 0.32

# num1 = input()
# num2 = input()
# print(type(num1))
# Count = num1 + num2
# print(f"{Count = }")
name = "lisa"
print("name is {}".format(name))
num3 = float(input())
print('{:.2f}'.format(num3))  

epsilon = input()
epsilon = float(epsilon)
answer = 0
n = 1.0
flag = 1.0
while 1/n >= epsilon:
    answer += flag/n
    flag = -flag
    n+= 1.0
print(answer)




