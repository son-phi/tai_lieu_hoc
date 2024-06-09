import sys
fin = open("triangles.inp")
fout = open("triangles.out","w")
sys.stdin = fin
sys.stdout = fout
n =int(input())
ans = 0
for i in range(n):
    s = fin.readline().split()
    xa,ya,xb,yb,xc,yc=[int(j) for j in s]
    t = abs(xa*yb-xb*ya+xb*yc-xc*yb+xc*ya-xa*yc)/2
    if t>ans:
        ans=t
    print(ans)

fin.close()
fout.close()