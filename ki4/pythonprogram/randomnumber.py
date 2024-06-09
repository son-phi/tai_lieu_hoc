from random import random
from random import randint

# tạo 3 số nuyên ngẫu nhiên trong phạm vi từ 1 đến 10
print("3 số nguyên ngẫu nhiên trong đoạn [1, 10]")
for i in range(3):
    print(randint(1,11))

# tạo 2 số thực ngẫu nhiên trong khoảng [0,1)
print(" 2 số thực ngẫu nhiên trong khoảng [0,1]")
for i in range(2):
    print("{:f}".format(random()))

# tạo 2 số thực ngẫu nhiên trong khoảng [10, 1)
print("2 số thực ngẫu nhiên trong khoảng [10,15]")
for i in range(2):
    print('{:f}'.format(random()*5 +10))
