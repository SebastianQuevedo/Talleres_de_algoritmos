a=str(input("ingrese a "))
b=str(input("ingrese b "))
c=str(input("ingrese c "))
d=str(input("ingrese d "))
total=a+b+c+d
total=int(total)
e=b+c+d
e=int(e)
print ("su numero es ",total)
if ( total%100==0):
  print (total)
elif (e<=500):
  f=total//100
  print (f*100)
elif (e>=500):
  f=total//100
  while (f%10!=0):
    f=f+1
  print ((f)*100)