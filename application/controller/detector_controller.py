
from datetime import date, datetime
from datetime import date
from application.model.entily.detector import Detector
from application.model.dao.detectorDAO import DetectorDAO
from application import app
from flask import  json, request,jsonify

detectordao = DetectorDAO()


@app.route("/")
def index():
    return ' <h1>Web service</h1>'

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

    return detector.to_dict(),201




@app.route("/buscar/<id>" ,methods=["GET"])
def buscar_id(id):
    result = detectordao.listar_medidas()
    detector_dict_list = []
    for detector in result:
        if detector.get_id() == int(id):
            detector_dict_list.append(detector.to_dict())
    return jsonify(detector_dict_list)

    #return jsonify({"error": "Detector não encontrada"}), 404
@app.route("/buscar/<dia>/<mes>/<ano>", methods=["GET"])
def buscar_data(dia,mes,ano):
    result = detectordao.listar_medidas()
    detector_dict_list = []
    
    data = "{dia}/{mes}/{ano}".format(dia = dia,mes = mes,ano = ano)
    print(data)

    for detector in result:
        dt = detector.get_data()
        dtt = datetime.strftime(dt,'%d/%m/%Y')
        if dtt == data:
            detector_dict_list.append(detector.to_dict())
    
    return jsonify(detector_dict_list)