class Animal():
    # Atributos
    def __init__(self,id,especie,dieta,cuidador):
        self.id=id
        self.especie=especie
        self.dieta=dieta
        self.cuidador=cuidador
    # Métodos
    def identificar(self):
        print("El animal es un",self.especie ,"y tiene una dieta",self.dieta)
    def asignar_cuidador(self,cuidador):
        self.cuidador=cuidador
        print("El cuidador del animal es",self.cuidador)
    
    
Animal_1=Animal(1,"Leon","Carnivoro","Juan")
print(Animal_1.identificar())