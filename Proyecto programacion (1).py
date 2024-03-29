tareas = {}

def agregar_tarea():
    nombre = input("¿Qué tarea desea hacer?: ")
    tareas[nombre] = False

def editar_tarea():
    nombre = input("Ingrese el nombre de la tarea que quiere editar: ")
    if nombre in tareas:
        tareas[nombre] = not tareas[nombre]
    else:
        print("Tarea no existe.")

def borrar_tarea():
    nombre = input("Ingrese el nombre de la tarea que quiere borrar: ")
    if nombre in tareas:
        del tareas[nombre]
    else:
        print("Tarea no existe.")

def ver_tareas_pendientes():
    pendientes = [nombre for nombre, completada in tareas.items() if not completada]
    print("Tareas pendientes:")
    for tarea in pendientes:
        print(tarea)

def ver_tareas_completadas():
    completadas = [nombre for nombre, completada in tareas.items() if completada]
    print("Tareas completadas:")
    for tarea in completadas:
        print(tarea)

def marcar_completada():
    nombre = input("Tarea que desea marcar como completada: ")
    if nombre in tareas:
        tareas[nombre] = True
    else:
        print("Tarea no existe.")

def numero_total_tareas():
    return len(tareas)

def numero_tareas_pendientes():
    return sum(1 for completada in tareas.values() if not completada)

def numero_tareas_completadas():
    return sum(1 for completada in tareas.values() if completada)

while True:
    print("\nSeleccione una opción:")
    print("1. Agregar tarea")
    print("2. Editar tarea")
    print("3. Borrar tarea")
    print("4. Ver tareas pendientes")
    print("5. Ver tareas completadas")
    print("6. Marcar tarea como completada")
    print("7. Número total de tareas")
    print("8. Número total de tareas pendientes")
    print("9. Número total de tareas completadas")
    print("10. Guardar tareas")
    print("11. Cargar tareas")
    print("12. Salir")
    opcion = int(input("Ingrese el número de la opción que desea: "))
    if opcion == 1:
        agregar_tarea()
    elif opcion == 2:
        editar_tarea()
    elif opcion == 3:
        borrar_tarea()
    elif opcion == 4:
        ver_tareas_pendientes()
    elif opcion == 5:
        ver_tareas_completadas()
    elif opcion == 6:
        marcar_completada()
    elif opcion == 7:
        print("Número total de tareas:", numero_total_tareas())
    elif opcion == 8:
        print("Número total de tareas pendientes:", numero_tareas_pendientes())
    elif opcion == 9:
        print("Número total de tareas completadas:", numero_tareas_completadas())
    elif opcion == 10:
        guardar_tareas()
    elif opcion == 11:
        cargar_tareas()
    elif opcion == 12:
        break
    else:
        print("Opción inválida.")
