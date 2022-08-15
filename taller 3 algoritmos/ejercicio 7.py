a=float(input("ingrese la distancia recorrida, en Km "))
if (a>=300 and a<=1000):
  b=a-300
  print ("el total a pagar es ",(70000+(b*30000))," COP")
elif (a>=300 and a>=1000):
  b=a-1000
  print ("el total a pagar es ",(150000+(b*9000))," COP")
else :
  print ("el total a pagar es $50000 COP")

    