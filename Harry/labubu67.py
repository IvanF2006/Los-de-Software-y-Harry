print("Bienvenido a ahorcados")
#Que la persona ponga la palabra a adivinar
palabrareal = input("Ingrese la palabra a adivinar: ")
palabra = palabrareal.lower()
#Convertimos la palabra en una lista
palabra_lista = list(palabra)
#Creamos una lista con guiones bajos del mismo tamaño que la palabra
guiones = ["_"] * len(palabra_lista)
#Creamos una variable para contar los intentos
intentos = 6
#Creamos una lista para guardar las letras ya usadas
letras_usadas = []
#Creamos un bucle 
print("""
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      """)
for intento in range(intentos):
     print(" ".join(guiones))
     print(f"Tienes {intentos - intento} intentos")
     print(f"Letras usadas: {', '.join(letras_usadas)}")
     letra = input("Ingrese una letra: ").lower()
     #Verificamos que la letra no haya sido usada
     if letra in letras_usadas:
          print("Ya usaste esa letra, intenta con otra")
          continue
     #Agregamos la letra a la lista de letras usadas
     letras_usadas.append(letra)
     #Verificamos si la letra está en la palabra
     if letra in palabra_lista:
          print("La letra está en la palabra")
          #Reemplazamos los guiones bajos por la letra en la posición correcta
          for i in range(len(palabra_lista)):
               if palabra_lista[i] == letra:
                    guiones[i] = letra
          #Verificamos si la persona ha adivinado la palabra
          if "_" not in guiones:
               print("Has adivinado la palabra:", palabra)
               break
     else:
          print("La letra no está en la palabra")
if "_" in guiones:
     print("no eres un verdadero 67 ", palabra, " era la palabra")