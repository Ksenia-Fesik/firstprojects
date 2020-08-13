print("введіть перше число")
a=int(input())
print("введіть друге число")
b=int(input())
print("введіть дію")
d=input()
if d=="+": 
    print(a, d, b, "=", a+b)
if d=="-": 
    print(a, d, b, "=", a-b)
if d=="*": 
    print(a, d, b, "=", a*b)
if d=="/":
    if b==0:
        print("Error")
    else:
        print(a, d, b, "=", a/b) 