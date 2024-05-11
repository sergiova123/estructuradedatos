class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar_opinion(self, opinion, sentimiento):
        if self.raiz is None:
            self.raiz = NodoArbol((opinion, sentimiento))
        else:
            self._agregar_opinion(opinion, sentimiento, self.raiz)

    def _agregar_opinion(self, opinion, sentimiento, nodo_actual):
        if sentimiento < nodo_actual.valor[1]:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = NodoArbol((opinion, sentimiento))
            else:
                self._agregar_opinion(opinion, sentimiento, nodo_actual.izquierda)
        elif sentimiento > nodo_actual.valor[1]:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = NodoArbol((opinion, sentimiento))
            else:
                self._agregar_opinion(opinion, sentimiento, nodo_actual.derecha)

    def buscar_opinion(self, opinion, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz

        if nodo_actual is None or nodo_actual.valor[0] == opinion:
            return nodo_actual.valor
        elif opinion < nodo_actual.valor[0]:
            return self.buscar_opinion(opinion, nodo_actual.izquierda)
        else:
            return self.buscar_opinion(opinion, nodo_actual.derecha)

    def recorrer_inorden(self, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz
        
        if nodo_actual is not None:
            self.recorrer_inorden(nodo_actual.izquierda)
            print(nodo_actual.valor)
            self.recorrer_inorden(nodo_actual.derecha)

# Crear el árbol binario
arbol = ArbolBinario()

# Cargar datos de opiniones positivas y negativas
# Aquí debes leer tus archivos de texto y procesarlos
# Supongamos que tenemos una lista de tuplas donde el primer elemento es la opinión y el segundo es el sentimiento
opiniones_positivas = [("Me encantó esta película", "positivo"), ("Gran película", "positivo")]
opiniones_negativas = [("No me gustó nada", "negativo"), ("Pésima película", "negativo")]

# Agregar opiniones al árbol
for opinion, sentimiento in opiniones_positivas:
    arbol.agregar_opinion(opinion, sentimiento)

for opinion, sentimiento in opiniones_negativas:
    arbol.agregar_opinion(opinion, sentimiento)

# Recorrer el árbol en orden
arbol.recorrer_inorden()

# Clasificar nuevas opiniones
nueva_opinion = "Esta película es increíble"
sentimiento = arbol.buscar_opinion(nueva_opinion)

if sentimiento is not None:
    print(f"Sentimiento de la opinión '{nueva_opinion}': {sentimiento}")
else:
    print(f"No se encontró una clasificación para la opinión '{nueva_opinion}'")
