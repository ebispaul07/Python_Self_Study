a="lal"
sa=a.lower()

rev=""
for i in range(len(sa)-1,-1,-1):
  rev=rev+sa[i]


if rev==sa:
    print("pal")
else:
    print("not pal")
