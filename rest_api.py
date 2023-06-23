# using flask_restful
from flask import Flask, jsonify, request,session, redirect
from flask_restful import Resource, Api

from models import *

from __init__ import app

api = Api(app)


class Dashboard(Resource):
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        if 'username' in session:
            username = session['username']
            user = User.objects.filter(name=username)
            data = Dashboard.query.filter_by(user_id=user.id)
            return jsonify({'data': data})
        return redirect('auth.login')