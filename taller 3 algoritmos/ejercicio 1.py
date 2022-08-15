a=float(input("cuanto dinero ingrso al banco "))
b=float(input("cual es la tasa de interes mensual "))
c=float(input("cuantos meses duro la inversion "))
d=(a*(b*c))
d=d/100
f=a+d
if (d>=100000):
  print ("sus ganancias son: $",d)
  print ("el total en su cuenta es: $",f)
else:
  print ("sus ganancias son inferiores a $100.000")
  
