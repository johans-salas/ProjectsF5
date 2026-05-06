def calculadora():
  print("Bienvenido(a) a la calculadora:\n")
  print("Operaciones disponibles: \n\t1. Suma \n\t2. Resta \n\t3. Multiplicación \n\t4. División\n")
  
  while True:
    opcion = input("Por favor ingrese la opción que desee realizar o 'q' para salir: \n")
    if opcion == "q":
      print("Gracias por usar la calculadora\n")
      break

    if opcion not in ["1", "2", "3", "4"]:
      print("Opción no válida")
      continue

    num1 = float(input("\nIngrese el primer número: "))
    num2 = float(input("\nIngrese el segundo número: "))

    if opcion == "1":
      print(f"\nLa suma de {num1} y {num2} es {num1 + num2}")
    elif opcion == "2":
      print(f"\nLa resta de {num1} y {num2} es {num1 - num2}")
    elif opcion == "3":
      print(f"\nLa multiplicacion de {num1} y {num2} es {num1 * num2}")
    elif opcion == "4" and num2 != 0:
      print(f"\nLa división de {num1} y {num2} es {num1 / num2}")
    else:
      print("\nError: no se puede dividir entre cero, por favor inténtelo nuevamente\n")

if __name__ == "__main__":
  calculadora()
