def myfunc(magic,dist):
    x=0
    sum1=0
    if sum(magic)>sum(dist):
        for i in range(len(magic)):
            if sum1<0:
                x=i
                sum1=0
            sum1+=(magic[i]-dist[i])
        return x
    else:
        return -1
n=int(input())
magic=[]
dist=[]
for i in range(n):
    magic=magic+[int(input())]
m=int(input())
for j in range(m):
    dist=dist+[int(input())]

print(myfunc(magic,dist))

