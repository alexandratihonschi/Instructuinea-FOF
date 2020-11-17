n=int(input("n este agl cu"))
s=0
for i in range (1, n+2):
    if (i%3==0) and  (i%5==0):
        s+=i
print('suma nr impare este:', s)
