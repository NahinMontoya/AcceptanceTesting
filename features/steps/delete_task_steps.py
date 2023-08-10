from behave import *
from src.funciones_tareas import Tarea, borrar_tarea

def before_scenario(context, scenario):
    context = {}

@given("lista con varias tareas")
def step_impl(context):
    tareas = [Tarea("Comprar Pan"), Tarea("Comprar Leche"), Tarea("Comprar huevos")]
    context.tasks = tareas

@given("indice {indice} ingresado por el usuario")
def step_impl(contexto, indice):
    contexto.indice = int(indice)

@when("el usuario elimina esa tarea")
def step_impl(context):
    tarea_eliminada = borrar_tarea(context.tasks,context.indice)
    context.tarea_elim = tarea_eliminada
@then("el nombre de la tarea es {nombre}")
def step_impl(context,nombre):
    assert context.tarea_elim.titulo == nombre