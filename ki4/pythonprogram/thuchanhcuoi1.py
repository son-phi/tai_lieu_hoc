

def lastover(a,x):
    l, r, res =0, len(a)-1, 0
    while l<=r:
        m = (l+r)//2
        if a[m] <x:
            res = m
            l = m+1
        else:
            r = m-1
    return res
if __name__ == '__main__':

    c =list(map(int,input().split()))
    t= c[0]
    idx = 1
    t = int(input())
    
    while t>0:
        n = int(input())
        pos = list(map(int,input().split()))
        idx +=n
        wall = list(map(int,input().split()))
        idx +=n+1
        water = [0]*(n+1)
        totalwall = [0]*(n+1)
        st= list()
        for i in range(1,n+1):
            totalwall[i]= totalwall[i-1]+wall[i]
            while len(st)!=0 and wall[i]>=wall[st[-1]]:
                st.pop()
            if len(st)==0:
                water[i]= pos[i]*wall[i]-totalwall[i-1]
            else:
                id = st[-1]
                water[i]= water[id]+(pos[i]-pos[id]-1)*wall[i]-(totalwall[i-1]-totalwall[id])
            st.append()
        q= c[idx]
        idx+=1
        while q>0:
            x = c[idx]
            idx +=1
            print(lastover(water,x))
            q-=1
        t-=1

