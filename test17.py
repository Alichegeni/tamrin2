a = int(input())
 
for i in range(3) :
     b=[]
     c=(a//3600)
     d= (a % 3600)
     d=(d//60)
     y=(d %60 )

     b=[c , d , y]
     

print(b)