#first method
a="eEbi"
a=a.lower()

freq={}

for ch in a:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1


print(freq)


#2..second method

from collections import Counter

s = "Hello World"
s = s.lower()
freq = Counter(s)
print(freq)

