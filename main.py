import os

from flask import Flask
from flask_restful import Resource, Api, reqparse

from datetime import datetime

# from vision import VisionNew
from visionold import Vision
from template import MapTemplate
from visionAll import VisionAll
from visionAPI import VisionAPI
from GetOCRResults_Template_Manual import MapTemplateManual

APPVersion = "1.0.0"

app = Flask(__name__)
api = Api(app)

api.add_resource(Vision, '/visionold')
# api.add_resource(VisionNew, '/vision')
api.add_resource(MapTemplate, '/template')
api.add_resource(VisionAll, '/vision')
api.add_resource(VisionAPI, '/visionAPI')
api.add_resource(MapTemplateManual, '/GetOCRResults_Template_Manual')

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=7000)
