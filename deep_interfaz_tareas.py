from deep_gestor_tareas import *

# Cargar tareas al iniciar
tareas = cargar_tareas()

def mostrar_menu():
    """
    Muestra el menú principal de la aplicación.
    """
    print("\n" + "="*50)
    print("           GESTOR DE TAREAS")
    print("="*50)
    print("1. 📝 Agregar tarea")
    print("2. 👀 Ver tareas")
    print("3. ✅ Completar tarea")
    print("4. 🗑️ Eliminar tarea")
    print("5. 💾 Guardar y salir")
    print("="*50)

def mostrar_tareas():
    """
    Muestra todas las tareas de la lista.
    """
    lista_tareas = obtener_tareas(tareas)
    
    if len(lista_tareas) == 0:
        print("📭 La lista de tareas está vacía")
    else:
        print("\n📋 LISTA DE TAREAS:")
        print("-" * 40)
        for i, tarea in enumerate(lista_tareas, 1):
            estado, nombre_tarea = formatear_tarea(tarea)
            print(f"{i:2d}. {estado}{nombre_tarea}")
    print("-" * 40)
    print(f"Total: {len(lista_tareas)} tarea(s)")
    print()

def agregar_tarea_interfaz():
    """
    Interfaz para agregar una nueva tarea.
    """
    tarea = input("Ingrese su tarea: ")
    agregar_tarea(tareas, tarea)
    print(f"✓ Fue añadida la siguiente tarea: '{tarea}'")
    print(f"📋 Es la tarea número {len(tareas)}")
    print()

def completar_tarea_interfaz():
    """
    Interfaz para marcar una tarea como completada.
    """
    if not tareas:
        print("📭 No hay tareas para completar")
        return
    
    mostrar_tareas()
    
    try:
        completada = int(input("Ingrese el número de la tarea que desea completar: "))
        
        if 1 <= completada <= len(tareas):
            if marcar_completada(tareas, completada-1):
                print("✅ Se marcó la tarea como completada")
            else:
                print("ℹ️ La tarea ya estaba marcada como completada")
        else:
            print("❌ Opción inválida")
    except ValueError:
        print("❌ Por favor, ingrese un número válido")

def eliminar_tarea_interfaz():
    """
    Interfaz para eliminar una tarea.
    """
    if not tareas:
        print("📭 No hay tareas para eliminar")
        return
    
    mostrar_tareas()
    
    try:
        numero_tarea = int(input("Introduzca el número de la tarea a eliminar: "))
        
        if 1 <= numero_tarea <= len(tareas):
            tarea_eliminada = eliminar_tarea(tareas, numero_tarea-1)
            if tarea_eliminada:
                nombre_tarea = tarea_eliminada.replace("(Completada)", "").strip()
                print(f"🗑️ Se eliminó la tarea: '{nombre_tarea}'")
        else:
            print("❌ Opción inválida")
    except ValueError:
        print("❌ Por favor, ingrese un número válido")

def main():
    """
    Función principal que ejecuta el menú de la aplicación.
    """
    print("📂 Cargando tareas desde el archivo...")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            
            if opcion == 1:
                agregar_tarea_interfaz()
            elif opcion == 2:
                mostrar_tareas()
            elif opcion == 3:
                completar_tarea_interfaz()
            elif opcion == 4:
                eliminar_tarea_interfaz()
            elif opcion == 5:
                guardar_tareas(tareas)
                print("💾 Datos guardados correctamente")
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción inválida. Por favor, elija 1-5")
                
        except ValueError:
            print("❌ Por favor, ingrese un número válido")

# Ejecutar el programa
if __name__ == "__main__":
    main()