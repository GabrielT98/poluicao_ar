from application.model.entily.detector import Detector
class DetectorDAO():
    def __init__(self):
        self.__medidas_list = []
    
    def adicionar_medida(self,detector: Detector):
        self.__medidas_list.append(detector)
    
    def listar_medidas(self):
        return self.__medidas_list




