def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def main():
    print("Calculadora sencilla")
    print("Operaciones disponibles: suma, resta, multiplicacion, division")
    op = input("Ingrese la operación: ").strip().lower()
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    if op == "suma":
        print("Resultado:", suma(a, b))
    elif op == "resta":
        print("Resultado:", resta(a, b))
    elif op == "multiplicacion":
        print("Resultado:", multiplicacion(a, b))
    elif op == "division":
        print("Resultado:", division(a, b))
    else:
        print("Operación no válida.")

if __name__ == "__main__":
    main()