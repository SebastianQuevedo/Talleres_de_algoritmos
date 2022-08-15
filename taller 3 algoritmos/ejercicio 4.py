a=float(input("ingrese el monto total de la compra "))
if (a<=5000000):
  b=a*0.7
  c=((a*0.3))
  d=((c*0.2)+c)
  e=0
else:
  b=a*0.55
  c=((a*0.15))
  d=((c*0.2)+c)
  e=((a*0.3))
print ("el valor a pagar por la empresa es: ",b)
print ("el valor a cubrir por el credito del fabricante es: ",c, "y los intereses seran: ",d)
if (e!=0):
  print (" se le pediran prestados al banco: ",e)