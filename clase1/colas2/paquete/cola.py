from .tipos import Vehiculo, Pruebas

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def esta_vacia(self):
        return self.primero is None

    def encolar(self, valor):
        nuevo_nodo = Nodo(valor) #Esto crea un nuevo nodo que contendrá el valor pasado como argumento.
        print(nuevo_nodo)
        #nuevo_nodo.valor.pruebas = self.agregar_pruebas_tecnicas(nuevo_nodo.valor.tipo)

        if self.esta_vacia(): #Si la cola está vacía, significa que este será el primer nodo en la cola.
            self.primero = nuevo_nodo #Si la cola está vacía, se asigna el nuevo nodo como el primer nodo
        else: #Si la cola no está vacía, significa que ya hay al menos un nodo en la cola.
            self.ultimo.siguiente = nuevo_nodo #En este caso, el nuevo nodo se añade al final de la cola. La referencia
        self.ultimo = nuevo_nodo #Se actualiza la referencia ultimo para que apunte al nuevo nodo,
    
    def desencolar(self):
        if self.esta_vacia():
            return None # None), el método devuelve None, indicando que no hay nada que desencolar.
        valor = self.primero.valor 
        self.primero = self.primero.siguiente #esto es necesario porque el método devolverá este valor después de desencolarlo.
        if self.primero is None:
            self.ultimo = None
        return valor
    
    def agregar_pruebas_tecnicas(self, tipo: str):
        tipos_prueba = {
            'moto': ['frenos', 'luces', 'gases', 'llantas'],
            'carro': ['frenos', 'luces', 'gases', 'llantas'],
            'camion': ['frenos', 'luces', 'aceite', 'aire', 'frenos_de_aire']
        }
        pruebas = []
        for prueba in tipos_prueba[tipo]:
            pruebas.append(Pruebas(nombre=prueba, resultado=False))
        return pruebas
    
    def ver_listado(self):
        elementos = []
        if self.esta_vacia():
            return None
        else:
            current = self.primero
            while current:
                elementos.append(current.valor)
                current = current.siguiente
            return elementos    

    def ver_primero(self):
        if self.esta_vacia():
            print("La cola está vacía")
        else:
            print("Primer elemento:", self.primero.valor)

    def ver_ultimo(self):
        if self.esta_vacia():
            print("La cola está vacía")
        else:
            print("Último elemento:", self.ultimo.valor)

    def contar(self) -> int:
        count = 0
        current = self.primero
        while current:
            count += 1
            current = current.siguiente
        return count