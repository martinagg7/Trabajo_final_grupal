import animal
class stock():
    def __init__(self,producto,cantidad):
        self.producto=producto
        self.cantidad=cantidad
    
    def pedir_comida_animal(self,dieta,cantidad):
        self.dieta=dieta
        if dieta=="carnivoro":
            self.producto="carne"
        elif dieta=="herbivoro":
            self.producto="carne y verdura"
        elif dieta=="omnivoro":
            self.producto="insectos"
        self.cantidad=cantidad

        print("Se han pedido",self.cantidad,"kg","de",self.producto,"para el animal",self.dieta)
    
animal_1=animal.Animal(1,"Leon","carnivoro","Juan")
print(animal_1.dieta)
stock_1=stock("carne",0)
print(stock_1.pedir_comida_animal(animal_1.dieta,10))
