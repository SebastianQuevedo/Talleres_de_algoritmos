a=float(input("ingrese la categoria del salario "))
if(a==1):
  b=5000000+(5000000*0.1)
elif (a==2):
  b=4300000+(4300000*0.15)
elif (a==3):
  b=3600000+(3600000*0.2)
elif (a==4):
  b=2000000+(2000000*0.4)
elif (a==5):
  b=900000+(900000*0.6)
print ("la categoria del empleado es: ",a)
print ("el nuevo salario del empleado es: ",b)