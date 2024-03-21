#Cola de prioridad con edades
import heapq

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __lt__(self, other):
        return self.edad > other.edad  # Definimos la comparación para que la persona de mayor edad tenga mayor prioridad

class ColaPrioridadPersonas:
    def __init__(self):
        self.personas = []
    
    def is_empty(self):
        return len(self.personas) == 0
    
    def put(self, persona):
        heapq.heappush(self.personas, persona)
    
    def get(self):
        return heapq.heappop(self.personas)

# Ejemplo de uso
cola = ColaPrioridadPersonas()
cola.put(Persona("Juan", 25))
cola.put(Persona("María", 30))
cola.put(Persona("Pedro", 20))

while not cola.is_empty():
    persona = cola.get()
    print(f"{persona.nombre}: {persona.edad} años")

#Implementacion de una cola basica
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Ejemplo de uso
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Salida: 1
print(q.dequeue())  # Salida: 2

#Operaciones básicas de una cola(queue,dequeue,etc)
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Ejemplo de uso
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.size())  # Salida: 3
print(q.dequeue())  # Salida: 1
print(q.dequeue())  # Salida: 2

#Inversion de una cola
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def reverse_queue(queue):
    stack = []
    while not queue.is_empty():
        stack.append(queue.dequeue())
    while stack:
        queue.enqueue(stack.pop())

# Ejemplo de uso
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
reverse_queue(q)
print(q.dequeue())  # Salida: 3
print(q.dequeue())  # Salida: 2

#Cola con capacidad limitada
class QueueWithCapacity:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity

    def enqueue(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            raise Exception("La cola ha alcanzado su capacidad máxima")

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Ejemplo de uso
q = QueueWithCapacity(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Salida: 1
q.enqueue(4)  # Lanza una excepción

#Cola de prioridad
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

# Ejemplo de uso
pq = PriorityQueue()
pq.put('Tarea 1', 3)
pq.put('Tarea 2', 1)
pq.put('Tarea 3', 2)
while not pq.is_empty():
    print(pq.get())

#Ordenar colas con colas
def sort_queue(queue):
    temp_queue = Queue()
    while not queue.is_empty():
        item = queue.dequeue()
        while not temp_queue.is_empty() and temp_queue.items[-1] > item:
            queue.enqueue(temp_queue.dequeue())
        temp_queue.enqueue(item)
    while not temp_queue.is_empty():
        queue.enqueue(temp_queue.dequeue())

# Ejemplo de uso
q = Queue()
q.enqueue(3)
q.enqueue(1)
q.enqueue(4)
q.enqueue(2)
sort_queue(q)
while not q.is_empty():
    print(q.dequeue(), end=' ')  # Salida: 1 2 3 4

#Cola de espera
class Cliente:
    def __init__(self, nombre, tiempo_servicio):
        self.nombre = nombre
        self.tiempo_servicio = tiempo_servicio

def simulacion_cola():
    clientes = [
        Cliente("Cliente 1", 5),
        Cliente("Cliente 2", 3),
        Cliente("Cliente 3", 7),
        Cliente("Cliente 4", 2)
    ]
    cola = Queue()
    tiempo_total = 0

    for cliente in clientes:
        cola.enqueue(cliente)

    while not cola.is_empty():
        cliente_actual = cola.dequeue()
        print(f"Atendiendo a {cliente_actual.nombre}")
        tiempo_total += cliente_actual.tiempo_servicio

    print(f"Tiempo total de espera: {tiempo_total}")

# Ejemplo de uso
simulacion_cola()