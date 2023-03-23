import cuidador
class Vaciones():
    def __init__(self,inicio,final):
        self.inicio=inicio
        self.final=final
    def coger_vaciones(self,inicio,final):
        self.inicio=inicio
        self.final=final
        print("El cuidador",self.nombre,"se va de vacaciones del",inicio,"al",final)

Cuidador_1=cuidador.Cuidador("Juan","Perez","Leon")
print(Cuidador_1.coger_vaciones("8/1/2023","10/1/2023"))