#Pila basica
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Ejemplo de uso
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())  # Salida: 3

#operaciones pila
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Ejemplo de uso
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.size())  # Salida: 3
print(s.pop())   # Salida: 3

#con capacidad limitada
class StackWithCapacity:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity

    def push(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            raise Exception("La pila ha alcanzado su capacidad máxima")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Ejemplo de uso
s = StackWithCapacity(3)
s.push(1)
s.push(2)
s.push(3)
print(s.pop())  # Salida: 3

#pila de 2 colas
class StackWithTwoQueues:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, item):
        self.queue1.append(item)

    def pop(self):
        if not self.is_empty():
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue1) == 0

# Ejemplo de uso
s = StackWithTwoQueues()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())  # Salida: 3

#pila que admite opcion minima
class MinStack:
    def __init__(self):
        self.items = []
        self.min_values = []

    def push(self, item):
        self.items.append(item)
        if not self.min_values or item <= self.min_values[-1]:
            self.min_values.append(item)

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            if popped_item == self.min_values[-1]:
                self.min_values.pop()
            return popped_item
        else:
            return None

    def get_min(self):
        if not self.is_empty():
            return self.min_values[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Ejemplo de uso
s = MinStack()
s.push(3)
s.push(5)
s.push(2)
print(s.get_min())  # Salida: 2
s.pop()
print(s.get_min())  # Salida: 3

#reversion de una cadena con pila
def reverse_string(string):
    stack = Stack()
    reversed_string = ''
    for char in string:
        stack.push(char)
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string

# Ejemplo de uso
print(reverse_string("hello"))  # Salida: olleh

#Lista de none
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.size = 0
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            # Si la cola está llena, eliminar el primer elemento
            self.dequeue()
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def display(self):
        print("Cola actual:", end=' ')
        i = self.front
        for _ in range(self.size):
            print(self.queue[i], end=' ')
            i = (i + 1) % self.capacity
        print()

# Ejemplo de uso
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.display()  # Salida: Cola actual: 1 2 3 4 5
cq.enqueue(6)
cq.display()  # Salida: Cola actual: 2 3 4 5 6
cq.dequeue()
cq.dequeue()
cq.display()