#para llamar las fechas
from datetime import date
#determinar dia actual,mes y año
today=date.today()#capturar la fecha del sistema
dia=today.day
mes=today.month
año=today.year
fecha_nacimiento=input("digite en este formato año/mes/dia ")
(año_n,mes_n,dia_n)=fecha_nacimiento.split("/")
año_n= int(año_n)
mes_n= int(mes_n)
dia_n= int(dia_n)
edad=0
#edad
if (mes==mes_n):
   if (dia_n>=dia):
     edad=edad+(año-año_n)-1
     
   else:
     edad=edad+(año-año_n)
elif (mes>mes_n):
    edad=edad+(año-año_n)
else :
  edad=edad+(año-año_n)-1
    
print ("su edad es: ",edad)

#signo
signo=""
if((dia_n>=22 and mes_n==11) or (dia_n<=21 and mes_n==12)):
    signo+="Sagitario"
elif((dia_n>=22 and mes_n==12) or (dia_n<=20 and mes_n==1)):
  signo+="capricornio"
elif((dia_n>=21 and mes_n==1) or (dia_n<=19 and mes_n==2)):
  signo+="acuario"
elif((dia_n>=20 and mes_n==2) or (dia_n<=19 and mes_n==3)):
  signo+="piscis"
elif((dia_n>=20 and mes_n==3) or (dia_n<=20 and mes_n==4)):
  signo+="aries"
elif((dia_n>=21 and mes_n==4) or (dia_n<=21 and mes_n==5)):
  signo+="Tauro"
elif((dia_n>=22 and mes_n==5) or (dia_n<=21 and mes_n==6)):
  signo+="geminis"
elif((dia_n>=22 and mes_n==6) or (dia_n<=22 and mes_n==7)):
  signo+="cancer"
elif((dia_n>=23 and mes_n==7) or (dia_n<=23 and mes_n==8)):
  signo+="Leo"
elif((dia_n>=24 and mes_n==8) or (dia_n<=22 and mes_n==9)):
  signo+="virgo"
elif((dia_n>=23 and mes_n==9) or (dia_n<=22 and mes_n==10)):
  signo+="libra"
elif((dia_n>=23 and mes_n==10) or (dia_n<=21 and mes_n==11)):
  signo+="escorpio"
print("su signo es: ",signo)