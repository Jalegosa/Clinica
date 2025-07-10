from collections import deque
cola_pacientes = deque()


def menu_principal():
    while True:
        print("\nBIENVENIDO AL MENÚ PRINCIPAL CLÍNICA\n  ")
        print("1. Pacientes en recepción")
        print("2. Farmacia")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print(" menu pacientes")
        elif opcion == '2':
          print(" menu_farmacia()")
        elif opcion == '3':
            print("Vuelva Pronto")
            break
        else:
            print("Esta opción no es válida.  Intente nuevamente.")


menu_principal()
