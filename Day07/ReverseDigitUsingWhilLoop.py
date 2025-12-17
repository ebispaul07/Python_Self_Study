num=1234

rev=0

while num>0:
    digt=num%10
    rev=rev*10+digt
    num=num//10

print(rev)