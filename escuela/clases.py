class estudiante:
    def __init__(self, matricula, nombre, apellidos):
        self.matricula = matricula
        self.nombre = nombre
        self.apellidos = apellidos

    def __repr__(self):
        return f"{self.matricula} {self.nombre} {self.apellidos}"
    
    