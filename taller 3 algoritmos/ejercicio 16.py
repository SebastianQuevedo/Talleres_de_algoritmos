a=float(input("ingrese el valor a "))
b=float(input("ingrese el valor b "))
c=float(input("ingrese el valor c "))
d=(b**2)-4*a*c
if (d==0):
  x1=-b/(2*a)
  x2=x1
  print ("el valor de x1 y x2 es: ",x1)
elif (d>0):
    x1=(-b + (((b**2)-4*a*c)**(1/2))/(2*a)
    x2=(-b - (((b**2)-4*a*c)**(1/2))/(2*a)
   print ("el valor de x1 es: ",x1)
   print ("el valor de x2 es: ",x2)
elif (d<0):
    print ("no se puede resolver con numeros reales")
        
  
     