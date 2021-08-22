n = int(input())
a = 0
b = 1
d=[1]
if n < 0:
    print("KHATA lotfan add bozogtar az sefr bashad")
elif n == 0:
    a=0
    d.append(a)
    
elif n == 1:
    b=1
    d.append(b)
    
    
else:
    for i in range(1 ,n):
        
        c = a + b
        a = b
        b = c 
    
        d.append(b)

print(d)