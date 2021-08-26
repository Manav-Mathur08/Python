def add(a,b):
 return a+b
def sub(c,d):
 return c-d
def mul(e,f):
 return e*f
def div(g,h):
 return g/h
print("1. ADDITITON")
print("2. SUBTRACTION")
print("3. MULTIPICATION")
print("4. DIVISION")
choice = int(input("Enter Your choice"))
if choice ==1:
 a=int(input("1st value"))
 b=int(input("2nd value"))
 print(add(a,b))
elif choice ==2:
 c=int(input("1st value"))
 d=int(input("2nd value"))
 print(sub(c,d))
elif choice ==3:
 e=int(input("1st value"))
 f=int(input("2nd value"))
 print(mul(e,f))
elif choice ==4:
 g=int(input("1st value"))
 h=int(input("2nd value"))
 print(div (g,h))
else:
 print("Please Choose Again!!")
