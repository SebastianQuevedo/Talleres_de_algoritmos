nombre_cliente=input("ingrese el nombre del cliente ")
a=float(input("ingrese el monto de la compra "))
if(a<=50000):
  print ("no hay descuento")
elif (a>=50000 and a<=100000):
  b=a-(a*0.05)
  print ("nombre del cliente: ",nombre_cliente)
  print ("el valor de compra es: ",a)
  print ("el descuento es de 5%")
  print ("con el descuento el valor a pagar es ",b)
elif (a>=100000 and a<=700000):
  b=a-(a*0.11)
  print ("nombre del cliente: ",nombre_cliente)
  print ("el valor de compra es: ",a)
  print ("el descuento es de 11%")
  print ("con el descuento el valor a pagar es ",b)
elif (a>=700000 and a<=1500000):
   b=a-(a*0.18)
   print ("nombre del cliente: ",nombre_cliente)
   print ("el valor de compra es: ",a)
   print ("el descuento es de 18%")
   print ("con el descuento el valor a pagar es ",b)
elif (a>=1500000):
   b=a-(a*0.25)
  print ("nombre del cliente: ",nombre_cliente)
  print ("el valor de compra es: ",a)
  print ("el descuento es de 25%")
   print ("con el descuento el valor a pagar es ",b)