datos=input("ingrese los datos a,b,c,d en ese orden ")
(a,b,c,d)=datos.split(",")
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if (d<0):
  print ("el valor de d es erroneo")
else:
   if (d==0):
     print ((a-c)**2)
   else :
     print (((a-b)**3)/d)

  
 
  