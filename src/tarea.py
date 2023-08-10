class Tarea:


    def __init__(self, titulo):
        self.titulo = titulo
        self.estado = "Pendiente"


    def marcar_completada(self):
        self.estado = "Completada"
