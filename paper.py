import math

h=int(input())

p=0

n=0

while p <= h:
    n+=1
    p=math.floor(0.00008*2**n)

print("紙を"+str(n)+"回折れば超えられる高さです（"+str(p)+"ｍ）")
