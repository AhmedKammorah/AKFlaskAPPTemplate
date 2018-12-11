from flask import Flask

from config import *

from flask_autodoc import Autodoc


app = Flask(__name__)

# from flask_api import FlaskAPI
# app = FlaskAPI(__name__)
auto = Autodoc(app)


app.debug = True

app.config['SECRET_KEY'] = AK_API_JWT_SECRET_KEY
app.config['JWT_ALGORITHM'] = AK_JWT_ALGORITHM
app.config['JWT_VERIFY_CLAIMS']   = [] #['signature', 'nbf', 'iat'] # 'exp',
app.config['JWT_REQUIRED_CLAIMS'] = [] #[ 'iat', 'nbf']  # 'exp',