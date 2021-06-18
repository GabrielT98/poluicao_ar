from application.model.entily.detector import Detector

class DetectorDAO():
    def __init__(self):
        self.__lista_de_medicoes = []
    
    def adicionar_medida(self,detector:Detector):
        self.__lista_de_medicoes.append(detector)
    
    def listar_medidas(self):
        return self.__lista_de_medicoes




