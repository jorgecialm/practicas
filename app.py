from funciones import *


# Bucle principal

while True:

    print("\n ***** Gestor de Tareas ****** \n")
    print("1. Añadir tareas")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

    print("\n ****************************** \n")

    opcion = input("Seleccione una opción (1-5): ")

    # Menu de opciones

    match opcion:
        case "1":  # añadir tareas
            agregar_tarea(tareas)
        case "2":  # ver tareas
            ver_tarea(tareas)
        case "3":  # completar tareas
            completar_tarea(tareas)
        case "4":  # eliminar tareas
            eliminar_tarea(tareas)
        case "5":  # salir
            print("Gracias por utilizar el programa de gestion de tareas")
            break
        case _:  # casos no validos
            print("opcion invalida ingrese entre 1-5")
    print("\n")
