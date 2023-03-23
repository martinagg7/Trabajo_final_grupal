import animal
import cuidador
import dieta
import stock

class Zoo():
    def __init__(self,nombre):
        self.nombre=nombre
        self.lista_animales=[]
        self.lista_cuidadores=[]
        self.lista_stock=[]
    
    def asignar_cuidador(self,animal,cuidador):
        self.animal=animal
        self.cuidador=cuidador
        self.lista_animales.append(animal)
        self.lista_cuidadores.append(cuidador)
        print("El cuidador",self.cuidador,"se encarga del animal",self.animal)

    def asignar_stock(self,stock):
        self.stock=stock
        self.lista_stock.append(stock)
        print("El stock de",self.stock,"se ha añadido")
        print("El stock es",self.lista_stock)

    def asignar_dieta(self,animal,dieta):
        self.animal=animal
        self.dieta=dieta
        print("El animal",self.animal,"tiene una dieta",self.dieta)
    
    def asignar_vaciones(self,cuidador,inicio,final):
        self.cuidador=cuidador
        self.inicio=inicio
        self.final=final
        print("El cuidador",self.cuidador,"se va de vacaciones del",self.inicio,"al",self.final)


Zoo_1=Zoo("Zoo de Madrid")
print(Zoo_1.asignar_cuidador("Leon","Juan"))
print(Zoo_1.asignar_stock("comida"))
print(Zoo_1.asignar_dieta("Leon","carnivoro"))
print(Zoo_1.asignar_vaciones("Juan","8/1/2023","18/1/2023"))

