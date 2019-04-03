#!/usr/bin/python3.6.7
###################################################################################################
# Name: routes.py
# Summary: This file contains code for datetime api
# Author(s): Irtiza Ali
# LastUpdated: 18/01/2019
###################################################################################################


# sys modules
import os
import json
from flask import Blueprint
from flask import request, jsonify, abort
from flask_api import status
import datetime
mod = Blueprint('datetime_api', __name__)

# Extracting environment variable
name = os.environ['Name']

@mod.route('/datetime', methods=['GET'])
def health_check():
    '''
    It will be used to verify the status of api
    '''
    response = {}
    dt = datetime.datetime.now()
    response['datetime'] = datetime.datetime.strftime(dt, "%Y-%m-%d %H:%M:%S") + ", Hello " + str(name)
    response['message'] = "Current datetime has been returned"
    return jsonify(response), status.HTTP_200_OK

@mod.route('/', methods=['GET'])
def default_controller():
    '''
    It is the default route
    '''
    response = {}
    dt = datetime.datetime.now()
    response['datetime'] = datetime.datetime.strftime(dt, "%Y-%m-%d %H:%M:%S") + ", Hello " + str(name)
    response['message'] = "Current datetime has been returned"
    return jsonify(response), status.HTTP_200_OK
