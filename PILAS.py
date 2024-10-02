class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

    def ver_tope(self):
        return self.items[-1]

    def tamano(self):
        return len(self.items)


pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print("Tope de la pila:", pila.ver_tope())  
print("Tamaño de la pila:", pila.tamano())  
print("Desapilando:", pila.desapilar())     
print("Tamaño de la pila:", pila.tamano())  
