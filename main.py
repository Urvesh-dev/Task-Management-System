####################################################################
###############          Import packages         ###################
####################################################################
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from flask_restful import Resource, Api

from __init__ import app
####################################################################
# our main blueprint
main = Blueprint('main', __name__)
####################################################################
@app.route('/') # home page that return 'index'
def index():
    return 'index'

####################################################################
@app.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

if __name__ == '__main__':
    app.run(debug=True) # run the flask app on debug mode