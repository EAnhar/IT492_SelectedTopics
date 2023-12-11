
from pymongo import MongoClient
import pymongo
from flask import Flask, request
from flask_restful import Resource, Api
from bson import ObjectId
import sys
import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import config

# CONFIG = config.configuration()
# Hostname = CONFIG.HOSTNAME
# DBname = CONFIG.DATABASE
# Collectionname = CONFIG.COLLECTION


client = MongoClient('brevets_mongodb', 27017)
DBname = 'brevetsDB'
Collectionname = 'brevetsCol'
db = client[DBname][Collectionname]

app = Flask(__name__)
api = Api(app)

# client = MongoClient('brevets_mongodb', 27017)
# DBname = 'brevetsDB'
# Collectionname = 'brevetsCol'
# db = client[DBname][Collectionname]

class All(Resource):
    def get(self):
        all_data = []
        brevet_documents = db.find()
        for document in brevet_documents:
            document['_id'] = str(document['_id'])
            all_data.append(document)
        return all_data

class listAll(Resource):
    def get(self):
        times = {"open": [], "close": []}
        brevet_documents = db.find()
        for document in brevet_documents:
            brevets = document.get("brevets", [])
            for brevet in brevets:
                controls = brevet.get("controls", [])
                for control in controls:
                    times["open"].append(control.get("open"))
                    times["close"].append(control.get("close"))
        return times

class listAlljson(listAll):
    pass

class listAllcsv(Resource):
    def get(self):
        csv = ""
        brevet_documents = db.find()
        for document in brevet_documents:
            brevets = document.get("brevets", [])
            for brevet in brevets:
                controls = brevet.get("controls", [])
                for control in controls:
                    csv += "{}, {}, ".format(control.get("open"), control.get("close"))
        return csv[:-2]

class listOpen(Resource):
    def get(self):
        times = {"open": []}
        brevet_documents = db.find()
        for document in brevet_documents:
            brevets = document.get("brevets", [])
            for brevet in brevets:
                controls = brevet.get("controls", [])
                for control in controls:
                    times["open"].append(control.get("open"))
        return times

# class listOpenjson(listOpen):
#     pass

# class listOpencsv(Resource):
#     def get(self):
#         csv = ""
#         brevet_documents = db.find()
#         for document in brevet_documents:
#             brevets = document.get("brevets", [])
#             for brevet in brevets:
#                 controls = brevet.get("controls", [])
#                 for control in controls:
#                     csv += "{},".format(control.get("open"))
#         return csv[:-1]

class listClose(Resource):
    def get(self):
        times = {"close": []}
        brevet_documents = db.find()
        for document in brevet_documents:
            brevets = document.get("brevets", [])
            for brevet in brevets:
                controls = brevet.get("controls", [])
                for control in controls:
                    times["close"].append(control.get("close"))
        return times

# class listClosejson(listClose):
#     pass

# class listClosecsv(Resource):
#     def get(self):
#         csv = ""
#         brevet_documents = db.find()
#         for document in brevet_documents:
#             brevets = document.get("brevets", [])
#             for brevet in brevets:
#                 controls = brevet.get("controls", [])
#                 for control in controls:
#                     csv += "{},".format(control.get("close"))
#         return csv[:-1]

class listOpenjson(listOpen):
    def get(self):
        top = request.args.get('top', type=int, default=None)
        open_times = super().get()["open"]
        open_times.sort()
        if top is not None and top > 0:
            open_times = open_times[:top]
        return {"open": open_times}

class listOpencsv(Resource):
    def get(self):
        top = request.args.get('top', type=int, default=None)
        open_times = []
        brevet_documents = db.find()
        for document in brevet_documents:
            brevets = document.get("brevets", [])
            for brevet in brevets:
                controls = brevet.get("controls", [])
                for control in controls:
                    open_times.append(control.get("open"))
        open_times.sort()
        if top is not None and top > 0:
            open_times = open_times[:top]
        csv = ",".join(map(str, open_times))
        return csv

class listClosejson(listClose):
    def get(self):
        top = request.args.get('top', type=int, default=None)
        close_times = super().get()["close"]
        close_times.sort()
        if top is not None and top > 0:
            close_times = close_times[:top]
        return {"close": close_times}

class listClosecsv(Resource):
    def get(self):
        top = request.args.get('top', type=int, default=None)
        close_times = []
        brevet_documents = db.find()
        for document in brevet_documents:
            brevets = document.get("brevets", [])
            for brevet in brevets:
                controls = brevet.get("controls", [])
                for control in controls:
                    close_times.append(control.get("close"))
        close_times.sort()
        if top is not None and top > 0:
            close_times = close_times[:top]
        csv = ",".join(map(str, close_times))
        return csv

api.add_resource(All, '/')

api.add_resource(listAll, '/listAll')
api.add_resource(listAlljson, '/listAll/json')
api.add_resource(listAllcsv, '/listAll/csv')

api.add_resource(listOpen, '/listOpenOnly')
api.add_resource(listOpenjson, '/listOpenOnly/json')
api.add_resource(listOpencsv, '/listOpenOnly/csv')

api.add_resource(listClose, '/listCloseOnly')
api.add_resource(listClosejson, '/listCloseOnly/json')
api.add_resource(listClosecsv, '/listCloseOnly/csv')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
