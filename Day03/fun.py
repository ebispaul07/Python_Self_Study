#sample function

def gret():
    print("Hello")

gret()

#sample return function

def add(a,b):
    return a+b

res=add(10,8)
print(f"Result:{res}")


#default value function

def welcome(name="Ebi"):
    print(name)

welcome()
welcome("Emi")


#Argument fun

def sam(age,nam):
    print("My Name is",nam,"my age is",age)

sam(nam="Ebi",age=23)
sam(13,"emi")


#Arguments -positional args and Keyword args

def samplargs(*args,**kwargs):

    print(args)
    print(kwargs)

samplargs(1,3,4,a=10,b=60)


