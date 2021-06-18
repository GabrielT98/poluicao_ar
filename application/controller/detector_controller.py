from application import app
from application.model.entily.detector import Detector
from application.model.dao.detectorDAO import DetectorDAO

@app.route('/')
def index():
    return ' <h1>ihiiihi</h1>'
@app.route('/adicionar', methods=["POST"])
def adicionar_medida():
    pass
