#remove spaces in string

a="  hello  "
b="---hello---"
c="  hello  "

print(a.strip())
print(a.lstrip())
print(a.rstrip())

#remove character by strip

print(b.strip("-"))
print(b.lstrip("-"))
print(b.rstrip("-"))

#use replace alse

print("Replace:"+a.replace(" ",""))