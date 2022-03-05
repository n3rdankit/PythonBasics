a=int(input())
b=a-(a-1)
for i in range(a):
    c=b%2
    if(c==0):
        print(b)
    b=b+1
