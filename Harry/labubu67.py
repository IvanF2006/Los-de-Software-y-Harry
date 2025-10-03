x = 1
while 0 < x: 
 print("Bienvenido a ahorcados")
 #Que la persona ponga la palabra a adivinar
 palabrareal = input("Ingrese la palabra a adivinar: ")
 palabra = palabrareal.lower()
 palabra_lista = list(palabra)
 #Convertimos la palabra en una lista
 #palabra_lista = list(palabra)
 #Creamos una lista con guiones bajos del mismo tamaño que la palabra
 guiones = [" " if c == " " else "_" for c in palabra]
 #Creamos una variable para contar los intentos
 intentos = 6
 #Creamos una lista para guardar las letras ya usadas
 letras_usadas = []
 letra_erronea = []
 palabra_usada = []
 palabra_erronea = []
 #Creamos un bucle 
 print("""
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       """)
 while intentos > 0:
      if intentos == 6:
       print(r"""
               +---+
               |   |
                   |
                   |
                   |
                   |
            ==-======           """)
      elif intentos == 5:
       print(r"""
             +---+
             |   |
             O   |
                 |
                 |
                 |
          ==-======           """)
      elif intentos == 4:
       print(r"""
             +---+
             |   |
             O   |
             |   |
                 |
                 |
         ==-======       """)
      elif intentos == 3:
            print(r"""
             +---+
             |   |
             O   |
             |\  |
                 |
                 |
          ==-======          """)
      elif intentos == 2:
           print(r"""
               +---+
               |   |
               O   |
              /|\  |
                   |
                   |
            ==-======      """)
      elif intentos == 1:
           print(r"""
               +---+
               |   |
               O   |
              /|\  |
              /    |
                   |
            ==-======           """)
      print(" ".join(guiones))
      print(f"Tienes {intentos} intentos")
      print("Ya has usado estas palabras: ", palabra_erronea)
      print("Ya has usado estas letras: ", letras_usadas)
      #Pedimos una letra o palabra
      palabra_o_letra = input("¿Quieres adivinar una letra o la palabra o comenzar de vuelta? (l/p/e): ").lower()
      if palabra_o_letra == "p":
           palabrapuesta = input("Ingrese la palabra: ").lower()
           if 1 > len(palabrapuesta):
                print("Ingrese una palabra de mas de 1 letra")
                continue
           if palabrapuesta == palabra:
                print("Has adivinado la palabra:", palabra)
                break
           elif palabrapuesta != palabra and len(palabrapuesta) > 1:
                print("La palabra no es correcta")
                palabra_erronea.append(palabrapuesta)
                intentos -= 1
                continue
      elif palabra_o_letra == "l":
       letra = input("Ingrese una letra: ").lower()
       if len(letra) != 1:
           print("Ingrese solo una letra")
           continue
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
       if letra not in palabra_lista:
         letra_erronea.append(letra)   
         intentos -= 1
         print("La letra no está en la palabra")
         continue
      elif palabra_o_letra == "e":
           break
 if intentos == 0:
      print("Has perdido broder, la palabra era:", palabra)
      print(r"""
               +---+
               |   |
               O   |
              /|\  |
              / \  |
                   |
            ==-======          """)
 print("Queres jugar de nuevo?")
 jgr = input("s/n: ").lower()
 if jgr == "s":
      continue
 elif jgr == "n":
      break