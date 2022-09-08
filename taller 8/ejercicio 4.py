estudiantes = {"1": {"nombre": "Lorea","nota": 8},"2": { "nombre": "Markel","nota": "4.2"}, "3": {"nombre": "Julen", "nota": 6.5}}
a=1
promedio=[]
promedio_final=0
while a<10:
  b=input("ingrese el numero del estudiante")
  c=input("ingrese el nombre")
  d=int(input("ingrese la nota"))
  estudiantes.update({b:{"nombre":c,"nota":d}})
  e=input("¿desea continuar?")
  if e=="no" or e=="No":
    break
  elif e=="si" or e=="Si":
    a+=1
  else:
    print ("la opcion ingresada no es valida, asi que se asume que desea continuar")
for key in estudiantes:
  promedio.append(int (estudiantes[key]["nota"]))

promedio_final=((sum(promedio))/len(promedio))
print (promedio_final)