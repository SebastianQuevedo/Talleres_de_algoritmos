usuario = { "iperurena": {"nombre": "Iñaki", "apellido": "Perurena", "password": "123123" } , "fmuguruza": { "nombre": "Fermín", "apellido": "Muguruza", "password": "654321" }, "aolaizola": { "nombre": "Aimar", "apellido": "Olaizola", "password": "123456" } }

for i in range(0,3):
 n_usuario=input("Escriba su usuario: ")
 contrasena = input("Escriba su password: ")
 if n_usuario in usuario and contrasena == usuario[n_usuario] ['password']:
  print(usuario[n_usuario]['nombre'])
  print(usuario[n_usuario]['apellido'])
  break
 else:
  print("Incorrecto")