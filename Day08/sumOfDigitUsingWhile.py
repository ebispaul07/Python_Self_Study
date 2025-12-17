num=123

sum=0

while num!=0:
    digit=num%10
    sum=sum+digit
    num=num//10


print(f"Sum of Numbers:{sum}")