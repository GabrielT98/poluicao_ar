
from datetime import datetime
from types import resolve_bases
from application.model.entily.detector import Detector
from application.model.dao.detectorDAO import DetectorDAO
from application import app
from flask import  request

@app.route("/")
def index():
    return ' <h1>ihiiihi</h1>'

@app.route("/adicionar", methods=["POST"])
def adicionar_medida():
    id = int(request.json['id'])
    data = datetime.strptime(request.json['data'],'%d/%m/%Y %H:%M')
    valor_ozonio = float(request.json['ozonio'])
    valor_material_particulado = float(request.json['material_particulado'])
    valor_monoxido_carbono = float(request.json['monoxido_carbono'])
    valor_dioxido_enxofre = float(request.json['dioxido_enxofre'])
    valor_oxido_nitroso = float(request.json['oxido_nitroso'])
    detector = Detector()
    detector.set_id(id)
    detector.set_data(data)
    detector.set_valor_oxonio(valor_ozonio)
    detector.set_valor_material_particulado(valor_material_particulado)
    detector.set_valor_monoxido_carbono(valor_monoxido_carbono)
    detector.set_valor_dioxido_enxofre(valor_dioxido_enxofre)
    detector.set_valor_oxido_nitroso(valor_oxido_nitroso)
    detectorDao = DetectorDAO().adicionar_medida(detector)

    return detector.to_dict(),201
    
