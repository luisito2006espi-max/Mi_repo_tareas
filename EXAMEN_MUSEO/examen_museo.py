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
            print(f"[{actual.codigo}] {actual.descripcion}")
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
    # Datos de prueba asignados
    datos_prueba = [
        ("MU01", "Máscara"),
        ("MU02", "Cerámica"),
        ("MU03", "Tejido")
    ]

    # Inicialización de las estructuras
    lista_museo = ListaEnlazada()
    pila_museo = Pila()
    cola_museo = Cola()

    # Registro de elementos en las tres estructuras
    for codigo, descripcion in datos_prueba:
        elemento_formateado = f"{codigo}: {descripcion}"
        lista_museo.agregar(codigo, descripcion)
        pila_museo.apilar(elemento_formateado)
        cola_museo.encolar(elemento_formateado)

    # 1. Mostrar Lista Enlazada
    print("--- LISTA ENLAZADA (Inventario) ---")
    lista_museo.mostrar()

    # 2. Demostración Pila (LIFO)
    print("\n--- PILA (LIFO: Último en entrar, Primero en salir) ---")
    elemento = pila_museo.desapilar()
    while elemento is not None:
        print(f"Desapilando: {elemento}")
        elemento = pila_museo.desapilar()

    # 3. Demostración Cola (FIFO)
    print("\n--- COLA (FIFO: Primero en entrar, Primero en salir) ---")
    elemento = cola_museo.desencolar()
    while elemento is not None:
        print(f"Desencolando: {elemento}")
        elemento = cola_museo.desencolar()

    # 4. Reto individual: Comprobar que el último nodo apunte a None
    print("\n--- RETO INDIVIDUAL ---")
    if lista_museo.cabeza is not None:
        actual = lista_museo.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente

        apunta_a_none = actual.siguiente is None
        print(f"Último nodo encontrado: [{actual.codigo}] {actual.descripcion}")
        print(f"¿El puntero 'siguiente' del último nodo es None?: {apunta_a_none}")