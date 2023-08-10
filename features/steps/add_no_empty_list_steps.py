from behave import *
from src.funciones_tareas import *

def before_scenario(context, scenario):
    context = {}

@given("la lista tiene 1 elemento")
def step_impl(context):
     context.tasks = [Tarea("Desayunar")]


@when('Agrega una nueva tarea {nombre_1}')
def step_impl(context, nombre_1):
    tarea = Tarea(nombre_1)
    context.tarea = tarea
    agregar_tarea(context.tasks,nombre_1)

@then('la lista debe contener {cantidad} elementos')
def step_impl(context,cantidad):
    assert int(cantidad) == len(context.tasks)