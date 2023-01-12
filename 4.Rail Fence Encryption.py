

def EncryptMessage(message,keylength):
    l=[]
    message=message.lower()
    w=""
    p=[" ","!","@","#","$","%","^","&","*","(",")"]
    for i in message:
        if i.isalpha() and i!=[" ","!","@","#","$","%","^","&","*","(",")"]:
            w=w+i
    x=len(w)
    for i in range(keylength):
        for j in range(i,x,keylength):
            l.append(w[j])
    s=""
    for i in l:
        s=s+i
    return s

message=input(f"Enter the plain text:\n")
keylength=int(input(f"Enter the Key length value\n"))
result=EncryptMessage(message, keylength)
print(result)
