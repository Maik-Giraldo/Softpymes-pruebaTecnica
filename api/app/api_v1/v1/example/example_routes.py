# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Routes Example
#########################################################

from flask import request, jsonify
from app.api_v1 import api
from app.controllers import ExampleController as Controller


@api.route('/index', methods=['GET'])
def get_index():
    response = Controller.get_index()
    return jsonify(data=response)

@api.route('/query', methods=['GET'])
def get_all():
    response = Controller.get_all()
    return jsonify(data=response)

@api.route('/query/<page>', methods=['GET'])
def get_page(page):
    response = Controller.get_page(page)
    return jsonify(data=response)