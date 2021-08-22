n=int(input())
d=[]

for i in range(n):
    a =int(input())

    if a<=20:
        d.append(a)
        c=sum(d)
        x=min(d)
        z=max(d)
    else:
        print("khata dobare noreh ra vared konid")
        exit
        
    
print("avarege :",c)
print("min : ",x)
print("max : ",z)

