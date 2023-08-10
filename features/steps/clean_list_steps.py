from behave import *
from src.funciones_tareas import Tarea, borrar_todas_las_tareas

def before_scenario(context, scenario):
    context = {}

@given("lista con tareas")
def step_impl(context):
    tareas = [Tarea("Comprar Pan"), Tarea("Comprar Leche")]
    context.tasks = tareas

@when("el usuario elimina todas las tareas")
def step_impl(context):
    borrar_todas_las_tareas(context.tasks)

@then("la lista queda vacia")
def step_impl(context):
    assert len(context.tasks) == 0