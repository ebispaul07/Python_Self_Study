#1st method

print("Vowel Count:")

a="hello"

sa=a.lower()

count=0

for i in range(0,len(a)):
    if sa[i]=="a":
        count+=1
    elif sa[i]=="e":
        count+=1
    elif sa[i]=="i":
        count+=1
    elif sa[i]=="o":
        count+=1
    elif sa[i]=="u":
        count+=1

print(f"First Method:{count}")


#2nd

b="Ebi"
sb=b.lower()

cont=0

for j in range(0,len(sb)):

    if sb[j] in "aeiou":
        cont +=1

print(f"Second Method:{cont}")

