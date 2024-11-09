class Estudiante: 
    nombre = ""
    apellido = ""
    matricula = 0

    def __init__(self, matricula, nombre, apellido):
        self.matricula = matricula
        self.nombre = nombre
        self.apellido = apellido


    
est_a = Estudiante (485204, "Miguel", "Cortez")
est_b = Estudiante (485208, "Oracio", "Pereira")
est_c = Estudiante (485212, "Itzel", "Sanchez")
est_d = Estudiante (485213, "Paola", "Ramirez")
est_e = Estudiante (485219, "Jorge", "Patiño")

est_a.nombre = "Miguel"
est_a.apellido = "Cortez"
est_a.matricula = "485248"

print(F"{est_a.matricula} {est_a.nombre} {est_a.apellido}")
print(F"{est_a.matricula} {est_b.nombre} {est_b.apellido}")
print(F"{est_a.matricula} {est_c.nombre} {est_c.apellido}")
print(F"{est_a.matricula} {est_d.nombre} {est_d.apellido}")
print(F"{est_a.matricula} {est_e.nombre} {est_e.apellido}")
