


# Añadir tareas
def agregar_tarea(tareas):
    tarea= input("ingrese su tareas : ")
    tareas.append(tarea)
    print(f"Fue añadida la suguiente tarea {tarea} \n")
    print(f"Es la tarea numero {len(tareas)} \n")
    

# Ver tareas
def ver_tarea(tareas):
    contador=0
    if len(tareas) == 0:
        print("La lista esta vacia")
    else:
        for tarea in tareas:
            contador += 1
            print(f"tarea {(contador)} : {tarea}")
            

# Completar tareas
def completar_tarea(tareas):
    print("\nCompletado\n")

# Eliminar tareas
def eliminar_tarea(tareas):
    print("\nEliminado\n")