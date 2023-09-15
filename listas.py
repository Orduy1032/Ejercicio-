

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato) 
        if not self.cabeza:
            self.cabeza = nuevo_nodo.get
            print ("la cabeza es", self.cabeza.dato )
        else: 
            actual = self.cabeza
            while actual.siguiente: 
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            print("la actual es", actual.dato)
    
    def imprimir (self): 
        actual = self.cabeza
        while actual: 
            print (actual.dato, end= " -> ")
            actual = actual.siguiente
        
        print("None")
        
class Main (): 
    def __init__(self): 
        self.listaEnlazada = ListaEnlazada ()
        self.run()
    def run(self): 
        while True: 
            numero = input("¿Que numero entero desea agregar a la lista?  ")
            self.listaEnlazada.append(numero)
            desicion = input("¿desea imprimir la lista enlazada? S/N ")
            if desicion == "S": 
                self.listaEnlazada.print()
            else: 
                print ("error")

