a=int(input("su paciente tiene mas de 1 año. responda 1.si o 2.no "))
if (a==1):
  b=int(input("ingrese la edad de su paciente "))
  c=float(input("ingrese su nivel de hemoglobina "))
  if (b>=1 and b<=5):
    if (c>=11.5 and c<=15):
      d=True
    else:
      d=False
  elif (b>=5 and b<=10):
     if (c>=12.6 and c<=15.5):
      d=True
     else: 
      d=False
  elif (b>=10 and b<=15):
     if (c>=13 and c<=15.5):
      d=True
     else:
      d=False
  elif (b>=15):
    d=str(input("su paciente es 1.hombre o 2.mujer"))
    if (d==1):
      if (c>=14 and c<=18):
       d=True
      else:
       d=False
    else:
     if (c>=12 and c<=16):
      d=True
     else:
      d=False
else:
  f=int(input("cuantos meses tiene su paciente "))
  c=float(input("ingrese su nivel de hemoglobina "))
  if (f>=0 and f<=1):
     if (c>=13 and c<=26):
      d=True
     else:
      d=False
  elif (f>=1 and f<=6):
    if (c>=10 and c<=18):
      d=True
    else:
      d=False
  elif (f>=6 and f<=12):
    if (c>=11 and c<=15):
      d=True
    else:
      d=False
if (d==True):
  print ("su paciente esta sano")
else:
  print ("su paciente tiene anemia")
      