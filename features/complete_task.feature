Feature: Cambiar el estado de una tarea

  Scenario: Cambio de estado de una tarea por el indice
  Given una lista con tareas
  Given usuario ingresa indice 1
  When el usuario marca como Completada la tarea
  Then el estado de la tarea 1 es Completada
    # Enter steps here