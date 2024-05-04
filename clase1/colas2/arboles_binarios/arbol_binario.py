"""Se importa el modulo random para generar numeros aleatorios"""
import random
"""Se importa el modulo time para medir el tiempo de ejecucion"""
import time

class Nodo:
    """Se crea la clase Nodo, la cual contiene un valor, un hijo izquierdo y un hijo derecho"""
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

    def __str__(self):
        return str(self.valor)

class ArbolBinario:
    """Se crea la clase ArbolBinario, la cual contiene un nodo raiz"""
    def __init__(self, raiz=None):
        self.raiz = raiz

    def insertar(self, valor):
        """Se crea el metodo insertar, el cual recibe un valor y lo inserta en el arbol"""
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar(valor, nodo.izq)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar(valor, nodo.der)

    def buscar(self, valor):
        """Se crea el metodo buscar, el cual recibe un valor y retorna True si lo encuentra y False si no"""
        if self.raiz is None:
            return False
        else:
            return self._buscar(valor, self.raiz)

    def _buscar(self, valor, nodo):
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor and nodo.izq is not None:
            return self._buscar(valor, nodo.izq)
        elif valor > nodo.valor and nodo.der is not None:
            return self._buscar(valor, nodo.der)
        return False

    def eliminar(self, valor):
        """Se crea el metodo eliminar, el cual recibe un valor y lo elimina del arbol"""
        if self.raiz is None:
            return False
        else:
            return self._eliminar(valor, self.raiz)

    def _eliminar(self, valor, nodo):
        if valor == nodo.valor:
            if nodo.izq is None and nodo.der is None:
                nodo = None
            elif nodo.izq is None:
                nodo = nodo.der
            elif nodo.der is None:
                nodo = nodo.izq
            else:
                nodo.valor = self._buscarMin(nodo.der)
                nodo.der = self._eliminar(nodo.valor, nodo.der)
        elif valor < nodo.valor and nodo.izq is not None:
            nodo.izq = self._eliminar(valor, nodo.izq)
        elif valor > nodo.valor and nodo.der is not None:
            nodo.der = self._eliminar(valor, nodo.der)
        return nodo

    def _buscarMin(self, nodo):
        """Se crea el metodo buscarMin, el cual recibe un nodo y retorna el valor minimo del arbol"""
        if nodo.izq is None:
            return nodo.valor
        else:
            return self._buscarMin(nodo.izq)

    def preorden(self):
        """Se crea el metodo preorden, el cual imprime los valores del arbol en preorden"""
        if self.raiz is not None:
            self._preorden(self.raiz)

    def _preorden(self, nodo):
        print(nodo.valor)
        if nodo.izq is not None:
            self._preorden(nodo.izq)
        if nodo.der is not None:
            self._preorden(nodo.der)

    def inorden(self):
        """Se crea el metodo inorden, el cual imprime los valores del arbol en inorden"""
        if self.raiz is not None:
            self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo.izq is not None:
            self._inorden(nodo.izq)
        print(nodo.valor)
        if nodo.der is not None:
            self._inorden(nodo.der)

    def postorden(self):
        """Se crea el metodo postorden, el cual imprime los valores del arbol en postorden"""
        if self.raiz is not None:
            self._postorden(self.raiz)

    def _postorden(self, nodo):
        if nodo.izq is not None:
            self._postorden(nodo.izq)
        if nodo.der is not None:
            self._postorden(nodo.der)
        print(nodo.valor)

    def imprimir(self):
        """Se crea el metodo imprimir, el cual imprime el arbol"""
        if self.raiz is not None:
            self._imprimir(self.raiz, 0)

    def _imprimir(self, nodo, nivel):
        if nodo is not None:
            self._imprimir(nodo.der, nivel+1)
            print('   '*nivel, nodo.valor)
            self._imprimir(nodo.izq, nivel+1)

# Path: clase-Arboles/main.py
arbol = ArbolBinario()

inicio = time.time()
random.seed(10)
for i in range(5000):
    arbol.insertar(random.randint(1, 10000))

arbol.inorden()
fin = time.time()
print("Tiempo de ejecucion: ", fin-inicio)