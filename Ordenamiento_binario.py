class numero:
    def __init__(self):
        self.lista=[]
    def agregar_numero(self): 
        n= int(input("ingrese cantidad de número en la lista \n"))
        for x in range(n):
            m= int(input(f"ingrese número {x+1} :"))
            self.lista.append(m)         
    def mostrar_numero(self):
        print(" Esta es tu lista : ")
        print(self.lista)
    def busqueda_binaria(self):
        a=self.lista
        mitad= len(a)//2

p=numero()
p.agregar_numero()
p.mostrar_numero()


num =input("Ingrese un numero")
lista=[1,2,3,4,5]
for x in lista:
    if x==num:
        print ("numero encontrado")



