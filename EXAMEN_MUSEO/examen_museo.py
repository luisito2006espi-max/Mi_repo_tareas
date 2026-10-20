class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        # TODO 1: agrega el nodo al final sin perder los anteriores
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(f"Código: {actual.codigo} | Descripción: {actual.descripcion}")
            actual = actual.siguiente


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2: agrega el elemento a la cima
        self.items.append(elemento)

    def desapilar(self):
        # TODO 3: devuelve y elimina el último elemento;
        # controla el caso de pila vacía
        if not self.items:
            return None
        return self.items.pop()


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4: agrega el elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # TODO 5: devuelve y elimina el primer elemento;
        # controla el caso de cola vacía
        if not self.items:
            return None
        return self.items.pop(0)


# ==========================================
# Pruebas y Reto Individual
# ==========================================
if __name__ == "__main__":
    # 0. Datos de prueba asignados
    datos_museo = [
        ("MU01", "Máscara"),
        ("MU02", "Cerámica"),
        ("MU03", "Tejido")
    ]

    # Instanciamos las estructuras
    inventario_lista = ListaEnlazada()
    solicitudes_cola = Cola()
    historial_pila = Pila()

    # Registramos los elementos en las 3 estructuras
    for cod, desc in datos_museo:
        inventario_lista.agregar(cod, desc)
        solicitudes_cola.encolar(f"{cod} - {desc}")
        historial_pila.apilar(f"{cod} - {desc}")

    # 1. Mostrar la lista enlazada (inventario secuencial)
    print("--- 1. LISTA ENLAZADA (Elementos Registrados) ---")
    inventario_lista.mostrar()

    # 2. Reto individual: Comprobar que el último nodo apunte a None
    print("\n--- 2. RETO INDIVIDUAL: Puntero del último nodo ---")
    if inventario_lista.cabeza is not None:
        actual = inventario_lista.cabeza
        # Recorremos hasta llegar exactamente al último nodo
        while actual.siguiente is not None:
            actual = actual.siguiente

        es_none = (actual.siguiente is None)
        print(f"El último elemento insertado es: {actual.codigo}")
        print(f"¿El puntero 'siguiente' del último nodo es None?: {es_none}")
    else:
        print("La lista está vacía.")

    # 3. Prueba LIFO: Desapilar de la Pila (Último en entrar, Primero en salir)
    print("\n--- 3. PRUEBA DE PILA (LIFO) ---")
    item_pila = historial_pila.desapilar()
    while item_pila is not None:
        print(f"Desapilando: {item_pila}")
        item_pila = historial_pila.desapilar()
    print("Estado: La pila está vacía.")

    # 4. Prueba FIFO: Desencolar de la Cola (Primero en entrar, Primero en salir)
    print("\n--- 4. PRUEBA DE COLA (FIFO) ---")
    item_cola = solicitudes_cola.desencolar()
    while item_cola is not None:
        print(f"Atendiendo solicitud: {item_cola}")
        item_cola = solicitudes_cola.desencolar()
    print("Estado: La cola está vacía.")