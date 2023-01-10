def love(x,y):
    x=x.lower()
    y=y.lower()
    a=x.count("t")
    b=x.count("r")
    c=x.count("u")
    d=x.count("e")
    e=x.count("l")
    f=x.count("o")
    g=x.count("v")
    h=x.count("e")
    a=a+y.count("t")
    b=b+y.count("r")
    c=c+y.count("u")
    d=d+y.count("e")
    e=e+y.count("l")
    f=f+y.count("o")
    g=g+y.count("v")
    h=h+y.count("e")
    k=a+b+c+d
    l=e+f+g+h
    re=str(k)+str(l)
    res=int(re)
    if res<10 or res>90:
        print(f"Your score is {res}, you go together like coke and mentos.")
    elif 40<res<50:
        print(f"Your score is {res}, you are alright together.")
    else:
        print(f"your love score is {res}")

x=input("enter your name:")
y=input("enter your lover name:")
love(x,y)        
