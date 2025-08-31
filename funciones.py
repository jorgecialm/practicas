
# lista de tareas
tareas=["tarea1","tarea2"]

# Añadir tareas
def agregar_tarea(lista):
    tarea= input("ingrese su tareas : ")
    tareas.append(tarea)
    print(f"Fue añadida la suguiente tarea {tarea} \n")
    print(f"Es la tarea numero {len(tareas)} \n")
    

# Ver tareas
def ver_tarea(lista):
    contador=0
    if len(tareas) == 0:
        print("La lista de tareas esta vacia")
    else:
        for tarea in tareas:
            contador += 1
            print(f"tarea {(contador)} : {tarea}")
    print("\n---------Fin de la lista ---------")      

# Completar tareas
def completar_tarea(lista):
    # llamamos a la funcion ver tareas 
    ver_tarea(lista)
    # entrada para que el usuario introduzca una tarea
    completada=int(input("ingrese la tarea que desea completar : "))
    # condicional para marcar tareas como completadas 
    if completada > 0  and completada <= len(lista):
        if "(Completada)" in lista[completada-1]:
            print("La tarea ya estaba marcada como completada ")
        else:
            lista[completada - 1] = "(Completada)" + lista[completada - 1]
            print("Se marco la tarea como completada")
    else:
        print("Opción invalida ")
# Eliminar tareas
def eliminar_tarea(lista):
    if lista:
        ver_tarea(lista)
        tarea=int(input("]Introduzca el numero de la tarea a eliminar "))
        
        if tarea <=0 or tarea > len(lista):
            print("Opcion invalida ")
        else:
            del lista[tarea-1]  
            print(" Se elimino la tarea ")
    else:
        print("No hay tareas ")        
        
            