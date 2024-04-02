#Escriba un función que reciba un string y devuelva true si la cadena esta balanceada o false en caso contrario
def esta_balanceada(cadena):
    

    pila = []
    for caracter in cadena:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila or pila[-1] != '(':
                return False
            else:
                pila.pop()  

    return not pila

cadena_balanceada = "(())()()"
cadena_no_balanceada = "(()))("

print("La cadena balanceada es balanceada:", esta_balanceada(cadena_balanceada))
print("La cadena no balanceada es balanceada:", esta_balanceada(cadena_no_balanceada))

#Utilizando la clase Cola, escriba una función llamada que reciba 2 Colas con números enteros y devuelva una nueva Cola con sus elementos sumados uno a uno.
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0, item)

    def quitar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def tamano(self):
        return len(self.items)

def sumar_colas(cola1, cola2):
    resultado = Cola()
    while not cola1.esta_vacia() and not cola2.esta_vacia():
        suma = cola1.quitar() + cola2.quitar()
        resultado.agregar(suma)

    while not cola1.esta_vacia():
        resultado.agregar(cola1.quitar())
    while not cola2.esta_vacia():
        resultado.agregar(cola2.quitar())

    return resultado

cola1 = Cola()
cola2 = Cola()

cola1.agregar(1)
cola1.agregar(2)
cola1.agregar(3)

cola2.agregar(4)
cola2.agregar(5)
cola2.agregar(6)

resultado = sumar_colas(cola1, cola2)
print("Elementos de la cola resultante:")
while not resultado.esta_vacia():
    print(resultado.quitar())

