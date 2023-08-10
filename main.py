from src.funciones_tareas import *

if __name__ == "__main__":
    tareas = []

    while True:
        print("                ****** Bienvenidos al sistemas de administración de tareas ******")
        print("Estas son las opciones disponibles:")
        print(" 1. Agregar Tarea")
        print(" 2. Listar Tareas")
        print(" 3. Marcar Tarea como Completada")
        print(" 4. Borrar Tarea seleccionada")
        print(" 5. Borrar Todas las Tareas")
        print(" 6. Salir del sistema")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Ingresa el título de la tarea: ")
            agregar_tarea(tareas,titulo)
            print("***** SE HA AGREGADO UNA TAREA *****")
        elif opcion == "2":
            formato_tareas = listar_tareas(tareas)
            for t in formato_tareas:
                print(t)
        elif opcion == "3":
            indice_tarea = int(input("Ingresa el número de tarea para marcar como completada: "))
            if 1 <= indice_tarea <= len(tareas):
                marcar_tarea_completada(tareas,indice_tarea)
                print(f"Se marco '{tareas[indice_tarea - 1].titulo}' como completada.")
            else:
                print("Índice de tarea no válido.")

        elif opcion == "4":
            indice_tarea = int(input("Ingresa el número de tarea para borrar: "))
            if 1 <= indice_tarea <= len(tareas):
                tarea_eliminada = borrar_tarea(tareas,indice_tarea)
                print(f"Se eliminó la tarea '{tarea_eliminada.titulo}'.")
            else:
                print("Índice de tarea no válido.")

        elif opcion == "5":
            borrar_todas_las_tareas(tareas)
            print("***** SE BORRARON TODAS LAS TAREAS *****")

        elif opcion == "6":
            print("***** SALIENDO DEL SISTEMA *****")
            break

        else:
            print("ERROR por favor ingrese una opción válida del sistema")
