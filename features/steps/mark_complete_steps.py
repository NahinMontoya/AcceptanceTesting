from behave import *
from src.funciones_tareas import Tarea, marcar_tarea_completada

def before_scenario(context, scenario):
    context = {}

@given("una lista con tareas")
def step_impl(context):
    tareas = [Tarea("Comprar Pan"), Tarea("Comprar Leche")]
    context.tasks = tareas

@given("usuario ingresa indice {indice}")
def step_impl(contexto, indice):
    contexto.indice = int(indice)

@when("el usuario marca como Completada la tarea")
def step_impl(context):
    marcar_tarea_completada(context.tasks,context.indice)

@then("el estado de la tarea 1 es {estado}")
def step_impl(context,estado):
    assert context.tasks[context.indice-1].estado == estado