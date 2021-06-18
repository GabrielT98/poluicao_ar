from datetime import datetime
class Detector():
    def __init__(self) :
        self.__id = None
        self.__data = None
        self.__valor_ozonio = None
        self.__valor_material_particulado = None
        self.__valor_monoxido_carbono = None
        self.__valor_dioxido_enxofre = None
        self.__valor_oxido_nitroso = None

    def set_id(self,id: int):
        self.__id = id
    
    def set_data(self,data: datetime):
        self.__data = data

    def set_valor_oxonio(self,valor: float):
        self.__valor_ozonio = valor

    def set_valor_material_particulado(self,valor: float):
        self.__valor_material_particulado = valor
    def set_valor_dioxido_enxofre(self,valor: float):
        self.__valor_dioxido_enxofre = valor

    def set_valor_oxido_nitroso(self,valor: float):
        self.__valor_oxido_nitroso = valor

           
    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data
    def get_valor_oxonio(self):
        return self.__valor_ozonio
    def get_valor_material_particulado(self):
        return self.__valor_material_particulado
    def get_valor_monoxido_carbono(self):
        return self.__valor_monoxido_carbono
    def get_valor_dioxido_enxofre(self):
        return self.__valor_dioxido_enxofre
    def get_valor_oxido_nitroso(self):
        return self.__valor_oxido_nitroso


    def to_dict(self):
        return{
            "id": self.__id,
            "data": self.__data.strftime('%d/%m/%Y %H:%M'),
            "ozonio": self.__valor_ozonio,
            "material_particulado":self.__valor_material_particulado,
            "monoxido_carbono": self.__valor_monoxido_carbono,
            "dioxido_enxofre": self.__valor_dioxido_enxofre,
            "oxido_nitroso": self.__valor_oxido_nitroso
        }
