from math import *
class Point():
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
        pass
    def distance(self,other):
        return "{:.4f}".format(sqrt(pow(self.x-other.x,2)+pow(self.y-other.y,2)))
def Decimal(a):
    return float(a)

class Rectangle():
    def __init__(self,length, width, color) -> None:
        self.length = length
        self.width = width
        self.c = color
        pass
    def perimeter(self):
        return (self.length+self.width)*2
    def area(self):
        return self.length*self.width
    def color(self):
        return self.c
    
    
if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))