class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
def imprimir_arbol(raiz, espacio='', es_ultima=True):
    if raiz is None:
        return
    sufijo = '' if es_ultima else '|'
    print(espacio + sufijo + '--', raiz.valor)
    if es_ultima:
        espacio += '   '
    else:
        espacio += '|  '
    if raiz.izquierda is not None:
        imprimir_arbol(raiz.izquierda, espacio, raiz.derecha is None)
    if raiz.derecha is not None:
        imprimir_arbol(raiz.derecha, espacio, True)
def inorder(raiz):
    if raiz is None:
        return
    inorder(raiz.izquierda)
    print(raiz.valor, end=' ')
    inorder(raiz.derecha)
def preorder(raiz):
    if raiz is None:
        return
    print(raiz.valor, end=' ')
    preorder(raiz.izquierda)
    preorder(raiz.derecha)
def postorder(raiz):
    if raiz is None:
        return
    postorder(raiz.izquierda)
    postorder(raiz.derecha)
    print(raiz.valor, end=' ')
# Crear el arbol binario
raiz = Nodo('A')
raiz.izquierda = Nodo('B')
raiz.derecha = Nodo('C')
raiz.izquierda.izquierda = Nodo('D')
raiz.izquierda.izquierda.derecha = Nodo('I')
raiz.izquierda.derecha = Nodo('E')
raiz.derecha.izquierda = Nodo('F')
raiz.derecha.derecha = Nodo('G')
raiz.izquierda.izquierda.izquierda = Nodo('H')
raiz.derecha.izquierda.izquierda = Nodo('J')
raiz.derecha.derecha.izquierda = Nodo('k')
raiz.derecha.derecha.derecha = Nodo('j')
raiz.derecha.derecha.derecha = Nodo('L')
# Imprimir el arbol
print("Grafica del arbol:")
imprimir_arbol(raiz)
# Realizar recorridos
print("\nPreorder :")
preorder(raiz)
print("\nInorder :")
inorder(raiz)
print("\nPostorder :")
postorder(raiz)
