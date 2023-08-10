Feature: Eliminar una tarea por indice

  Scenario: Eliminar una tarea por el indice ingresado
    Given lista con varias tareas
    Given indice 3 ingresado por el usuario
    When el usuario elimina esa tarea
    Then el nombre de la tarea es Comprar huevos