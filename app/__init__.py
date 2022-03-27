from app.datetime_api.routes import mod
from flask import Flask

app = Flask(__name__)

# registering application
app.register_blueprint(mod, uri_prefix='/datetime_api')
