from flask import Flask

app = Flask(__name__)

from application.controller import detector_controller