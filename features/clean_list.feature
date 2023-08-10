Feature: Borrar todas las tareas
  Scenario: Borrar todas las tareas que estan en la lista
    Given lista con tareas
    When el usuario elimina todas las tareas
    Then la lista queda vacia