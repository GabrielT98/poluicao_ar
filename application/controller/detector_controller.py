
from datetime import datetime
from application.model.entily.detector import Detector
from application.model.dao.detectorDAO import DetectorDAO
from application import app
from flask import  json, request,jsonify

detectordao = DetectorDAO()


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

    detectordao.adicionar_medida(detector)

    #with open('medicoes.json','w') as outfile:
     #   json.dump(detector.to_dict(),outfile)

    return detector.to_dict(),201




@app.route("/buscar/<id>" ,methods=["GET"])
def buscar_id(id):
    result = detectordao.listar_medidas()
    detector_dict_list = []
    for detector in result:
        if detector.get_id() == int(id):
            detector_dict_list.append(detector.to_dict())
    return jsonify(detector_dict_list)

    return jsonify({"error": "Detector não encontrada"}), 404