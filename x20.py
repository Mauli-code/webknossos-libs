# Your code 
a= int(input())
b= int(input())

for i in range(a, b + 1):
    d= i
    c = 0
    while d > 0:
        c += 1
        d//= 10
    d= i
    z = 0
    while d> 0:
        e =d% 10
        x = 1
        for j in range(c):
            x *= e
        z += x
        d//= 10
    if z == i:
        print(i,end=" ")
