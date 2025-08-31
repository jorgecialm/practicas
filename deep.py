# Lista de tareas
tareas = ["tarea1", "tarea2"]

# Añadir tareas
def agregar_tarea(lista):
    tarea = input("Ingrese su tarea: ")
    lista.append(tarea)
    print(f"✓ Fue añadida la siguiente tarea: '{tarea}'")
    print(f"📋 Es la tarea número {len(lista)}")
    print()

# Ver tareas
def ver_tarea(lista):
    if len(lista) == 0:
        print("📭 La lista de tareas está vacía")
    else:
        print("\n📋 LISTA DE TAREAS:")
        print("-" * 30)
        for i, tarea in enumerate(lista, 1):
            estado = "✓ " if "(Completada)" in tarea else "□ "
            nombre_tarea = tarea.replace("(Completada)", "").strip()
            print(f"{i:2d}. {estado}{nombre_tarea}")
    print("-" * 30)
    print(f"Total: {len(lista)} tarea(s)")
    print()

# Completar tareas
def completar_tarea(lista):
    if not lista:
        print("📭 No hay tareas para completar")
        return
    
    ver_tarea(lista)
    
    try:
        completada = int(input("Ingrese el número de la tarea que desea completar: "))
        
        if 1 <= completada <= len(lista):
            if "(Completada)" in lista[completada-1]:
                print("ℹ️ La tarea ya estaba marcada como completada")
            else:
                lista[completada-1] = "(Completada) " + lista[completada-1].replace("(Completada)", "").strip()
                print("✅ Se marcó la tarea como completada")
        else:
            print("❌ Opción inválida")
    except ValueError:
        print("❌ Por favor, ingrese un número válido")

# Eliminar tareas
def eliminar_tarea(lista):
    if not lista:
        print("📭 No hay tareas para eliminar")
        return
    
    ver_tarea(lista)
    
    try:
        tarea = int(input("Introduzca el número de la tarea a eliminar: "))
        
        if 1 <= tarea <= len(lista):
            tarea_eliminada = lista[tarea-1].replace("(Completada)", "").strip()
            del lista[tarea-1]
            print(f"🗑️ Se eliminó la tarea: '{tarea_eliminada}'")
        else:
            print("❌ Opción inválida")
    except ValueError:
        print("❌ Por favor, ingrese un número válido")

# Menú principal
def menu_principal():
    while True:
        print("\n" + "="*40)
        print("        GESTOR DE TAREAS")
        print("="*40)
        print("1. 📝 Agregar tarea")
        print("2. 👀 Ver tareas")
        print("3. ✅ Completar tarea")
        print("4. 🗑️ Eliminar tarea")
        print("5. 🚪 Salir")
        print("="*40)
        
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            
            if opcion == 1:
                agregar_tarea(tareas)
            elif opcion == 2:
                ver_tarea(tareas)
            elif opcion == 3:
                completar_tarea(tareas)
            elif opcion == 4:
                eliminar_tarea(tareas)
            elif opcion == 5:
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción inválida. Por favor, elija 1-5")
                
        except ValueError:
            print("❌ Por favor, ingrese un número válido")

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()