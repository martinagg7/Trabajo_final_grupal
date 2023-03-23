import animal
import cuidador

class Dieta():
    def __init__(self,tipo_alimentacion):
        if tipo_alimentacion=="carnivoro":
            self.dieta="carnivoro"
        elif tipo_alimentacion=="herbivoro":
            self.dieta="carne y verdura"
        elif tipo_alimentacion=="omnivoro":
            self.dieta="insectos"


animal_1=animal.Animal(1,"Leon","carnivoro","Juan")
print(animal_1.dieta)