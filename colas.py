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
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
        self.ultimo = nuevo_nodo
    
    def desencolar(self):
        if self.esta_vacia():
            return None
        valor = self.primero.valor
        self.primero = self.primero.siguiente
        if self.primero is None:
            self.ultimo = None
        return valor
    
    def mostrar(self):
        if self.esta_vacia():
            return
        current = self.primero
        while current:
            print(current.valor, end="->")
            current = current.siguiente
        print()


cola = Cola()
cola.encolar(5)
cola.encolar(6)
cola.encolar(7)
cola.encolar(8)

cola.mostrar()

cola.desencolar()
cola.desencolar()

cola.mostrar()