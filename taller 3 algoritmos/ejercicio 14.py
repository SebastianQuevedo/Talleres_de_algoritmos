a=float(input("ingrese la lectura anterior "))
b=float(input("ingrese la lectura actual "))
if (b-a<=100):
  c=4600
elif (b-a<=300):
  c=8000
elif (b-a<=500):
  c=1000000
elif (b-a>=501):
  c=120000
print ("el consumo es: ",b-a)
print ("el valor a pagar es: ",(b-a)*c)