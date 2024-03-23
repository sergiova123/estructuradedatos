class Pruebas():
    nombre: str # Nombre de la prueba tecnica
    resultado: bool # Resultado de la prueba tecnica True si paso, False si no paso

class Vehiculo():
    tipo: str # Tipo de vehiculo (moto, carro, camion, etc)
    matricula: str # Matricula o placa del vehiculo
    color: str # Color del vehiculo
    marca: str # Marca del vehiculo
    kilometraje: int # Kilometraje del vehiculo
    pruebas= []  # Arreglo de pruebas tecnicas

    def __init__(self, tipo: str, matricula: str, color: str, marca: str, kilometraje: int):
        self.tipo = tipo
        self.matricula = matricula
        self.color = color
        self.marca = marca
        self.kilometraje = kilometraje
        self.pruebas = []
    