Feature: Enlistar tareas segun un formato
  Scenario: Se genera una listas con el formato a mostrar por pantalla
    Given lista con una tarea
    When  el usuario desea ver todas las tareas
    Then la lista con tiene un elemento igual a 1. [Pendiente] Comprar Pan