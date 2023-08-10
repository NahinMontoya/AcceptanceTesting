from behave import *
from src.funciones_tareas import Tarea, agregar_tarea

def before_scenario(context, scenario):
    context = {}

@given("la lista esta vacia")
def step_impl(context):
    tareas = []
    context.tasks = tareas

@when('el usuario agrega una tarea {nombre}')
def step_impl(context, nombre):
    tarea = Tarea(nombre)
    context.tarea = tarea
    agregar_tarea(context.tasks, nombre)

@then('la lista contiene {cantidad_1} tarea')
def step_impl(context,cantidad_1):
    assert int(cantidad_1) == len(context.tasks)