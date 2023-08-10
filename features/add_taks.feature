Feature: Agregar una tarea a la lista
  Scenario: Agregar una tarea a la lista no vacia
    Given la lista tiene 1 elemento
    When Agrega una nueva tarea "Comprar leche"
    Then la lista debe contener 2 elementos

  Scenario: Agregar una tarea a la lista vacia
    Given la lista esta vacia
    When el usuario agrega una tarea "Comprar pan"
    Then la lista contiene 1 tarea