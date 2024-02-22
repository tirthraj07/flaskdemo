from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

from .Model.loadEnvironment import *


socketio = SocketIO()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRETKEY

    socketio.init_app(app,cors_allowed_origins="*")

    from .routes import main
    app.register_blueprint(main)

    from .api.routes import api
    app.register_blueprint(api,url_prefix='/api')

    return app

if __name__ == '__main__':
    app = Flask(__name__)
    socketio = SocketIO(app)
    app.config['SECRET_KEY'] = SECRETKEY
    
    from routes import main
    app.register_blueprint(main)

    from api.routes import api
    app.register_blueprint(api,url_prefix='/api')

    socketio.init_app(app,cors_allowed_origins="*")
    socketio.run(app,host=HOSTNAME,port=PORT)
