print("""
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      """)
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
palabra_usada = []
#Creamos un bucle 
print("""
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      """)
for intento in range(intentos):
     if intentos == 6:
      print("""
              +---+
              |   |
                  |
                  |
                  |
                  |
           ==-======           """)
     elif intentos == 5:
      print("""
            +---+
            |   |
            O   |
                |
                |
                |
         ==-======           """)
     elif intentos == 4:
      print("""
            +---+
            |   |
            O   |
            |   |
                |
                |
         ==-======       """)
     elif intentos == 3:
           print("""
            +---+
            |   |
            O   |
            |\  |
                |
                |
         ==-======          """)
     elif intentos == 2:
           print("""
             +---+
              |   |
              O   |
             /|\  |
                  |
                  |
           ==-======      """)
     elif intentos == 1:
          print("""
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
           ==-======           """)
     print(" ".join(guiones))
     print(f"Tienes {intentos} intentos")
     #Pedimos una letra o palabra
     palabra_o_letra = input("¿Quieres adivinar una letra o la palabra o comenzar de vuelta? (l/p/e): ").lower()
     if palabra_o_letra == "p":
          palabrapuesta = input("Ingrese la palabra: ").lower()
          if palabrapuesta == palabra:
               print("Has adivinado la palabra:", palabra)
               break
          else:
               print("La palabra no es correcta")
               palabra_usada.append(palabrapuesta)
               intentos -= 1
               continue
     elif palabra_o_letra == "l":
      letra = input("Ingrese una letra: ").lower()
      #Verificamos que la letra no haya sido usada
      if letra in letras_usadas:
          print("Ya usaste esa letra, intenta con otra")
          continue
      #Agregamos la letra a la lista de letras usadas
      letras_usadas.append(letra)
      #Verificamos si la letra está en la palabra
     elif letra in palabra_lista:
          print("La letra está en la palabra")
          #Reemplazamos los guiones bajos por la letra en la posición correcta
          for i in range(len(palabra_lista)):
               if palabra_lista[i] == letra:
                    guiones[i] = letra
          #Verificamos si la persona ha adivinado la palabra
     if letra not in palabra_lista:
        intentos -= 1
        print("La letra no está en la palabra")
        continue
     elif palabra_o_letra == "e":
          break
if intentos == 0:
     print("Has perdido broder, la palabra era:", palabra)
     print("""
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
           ==-======          """)