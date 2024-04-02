#Escribir una función Reemplazar que tenga como argumentos una pila con tipo de elemento int y dos valores int: nuevo y viejo de forma que si el segundo valor aparece en algún lugar de la pila,sea reemplazado por el segundo.
def reemplazar(pila, nuevo, viejo):
    
    pila_auxiliar = []

    while pila:
        elemento = pila.pop()
        if elemento == viejo:
            elemento = nuevo
        pila_auxiliar.append(elemento)

    while pila_auxiliar:
        pila.append(pila_auxiliar.pop())


pila = [1, 2, 3, 4, 5, 4, 6, 7]
viejo = 4
nuevo = 8
reemplazar(pila, nuevo, viejo)
print(pila) 

#Implementar una función Mezcla2 que tenga como parámetros dos listas de enteros ordenados de menor a mayor y que devuelva una nueva lista como unión de ambas con sus elementos ordenados de la misma forma
def mezcla2(lista1, lista2):
    i = 0
    j = 0
    resultante = []

    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultante.append(lista1[i])
            i += 1
        else:
            resultante.append(lista2[j])
            j += 1

    resultante.extend(lista1[i:])
    resultante.extend(lista2[j:])

    return resultante

lista1 = [1, 3, 5, 7, 9]
lista2 = [2, 4, 6, 8, 10]
resultado = mezcla2(lista1, lista2)
print(resultado)

#Construir una función que sume los elementos de una lista de enteros recursivamente.
def suma_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + suma_recursiva(lista[1:])

lista = [1, 2, 3, 4, 5]
resultado = suma_recursiva(lista)
print(resultado)

#Construir una función imprimeInverso que imprima los elementos de una lista enlazada de enteros en orden inverso a partir de una posición p
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_elemento(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprime_inverso(self, posicion):
         def imprimir_reversa(nodo, pos):
            if not nodo:
                return
            if pos >= posicion:
                imprimir_reversa(nodo.siguiente, pos + 1)
                print(nodo.valor)

            imprimir_reversa(self.cabeza, 1)

lista = ListaEnlazada()
lista.agregar_elemento(1)
lista.agregar_elemento(2)
lista.agregar_elemento(3)
lista.agregar_elemento(4)
lista.agregar_elemento(5)

posicion = 3 
print("Elementos en orden inverso a partir de la posición", posicion)
lista.imprime_inverso(posicion)

#Escriba una función que reciba una string y devuelve el string inviertido utilizando una Pila. 
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()


def invertir_cadena(cadena):
    pila = Pila()
    for caracter in cadena:
        pila.apilar(caracter)

    cadena_invertida = ''
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()

    return cadena_invertida

cadena = "Hola mundo!"
cadena_invertida = invertir_cadena(cadena)
print("Cadena original:", cadena)
print("Cadena invertida:", cadena_invertida)
