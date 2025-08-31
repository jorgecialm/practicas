import json
import os

# Nombre del archivo para guardar las tareas
ARCHIVO_TAREAS = "tareas.json"

def cargar_tareas():
    """
    Carga las tareas desde el archivo JSON.
    Retorna una lista de tareas.
    """
    if os.path.exists(ARCHIVO_TAREAS):
        try:
            with open(ARCHIVO_TAREAS, 'r') as archivo:
                return json.load(archivo)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def guardar_tareas(lista):
    """
    Guarda la lista de tareas en el archivo JSON.
    """
    with open(ARCHIVO_TAREAS, 'w') as archivo:
        json.dump(lista, archivo, indent=4)

def agregar_tarea(lista, tarea):
    """
    Añade una nueva tarea a la lista y guarda los cambios.
    Retorna la lista actualizada.
    """
    lista.append(tarea)
    guardar_tareas(lista)
    return lista

def obtener_tareas(lista):
    """
    Retorna la lista de tareas actual.
    """
    return lista

def marcar_completada(lista, indice):
    """
    Marca una tarea como completada.
    Retorna True si tuvo éxito, False en caso contrario.
    """
    if 0 <= indice < len(lista):
        if "(Completada)" not in lista[indice]:
            lista[indice] = "(Completada) " + lista[indice].replace("(Completada)", "").strip()
            guardar_tareas(lista)
            return True
    return False

def eliminar_tarea(lista, indice):
    """
    Elimina una tarea de la lista.
    Retorna la tarea eliminada si tuvo éxito, None en caso contrario.
    """
    if 0 <= indice < len(lista):
        tarea_eliminada = lista.pop(indice)
        guardar_tareas(lista)
        return tarea_eliminada
    return None

def formatear_tarea(tarea):
    """
    Formatea una tarea para mostrarla.
    Retorna una tupla con (estado, nombre_formateado)
    """
    estado = "✓ " if "(Completada)" in tarea else "□ "
    nombre_tarea = tarea.replace("(Completada)", "").strip()
    return (estado, nombre_tarea)