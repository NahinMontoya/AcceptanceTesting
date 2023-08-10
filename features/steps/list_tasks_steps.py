from behave import *
from src.funciones_tareas import Tarea, listar_tareas

def before_scenario(context, scenario):
    context = {}

@given("lista con una tarea")
def step_impl(context):
    tareas = [Tarea("Comprar Pan")]
    context.tasks = tareas

@when("el usuario desea ver todas las tareas")
def step_impl(context):
    form_lista = listar_tareas(context.tasks)
    context.lista_tareas = form_lista

@then("la lista con tiene un elemento igual a {resultado}")
def step_impl(context, resultado):
    assert context.lista_tareas[0] == resultado