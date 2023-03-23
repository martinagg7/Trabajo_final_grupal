class Cuidador() :
    #atributos
    def __init__(self,nombre,apellido,animal):
        self.nombre=nombre
        self.apellido=apellido
        self.animal=animal
    #metodos
    def asignar_animal(self,animal):
        self.animal=animal
        print("El cuidador",self.nombre,"se encarga del animal",self.animal)

    def identificar(self):
        print("El cuidador es",self.nombre,self.apellido)

    def coger_vaciones(self,inicio,final):
            self.inicio=inicio
            self.final=final
            print("El cuidador",self.nombre,"se va de vacaciones del",inicio,"al",final)

Cuidador_1=Cuidador("Juan","Perez","Leon")
print(Cuidador_1.identificar())
print(Cuidador_1.asignar_animal("Leon"))
print(Cuidador_1.coger_vaciones("8/1/2023","18/1/2023"))


