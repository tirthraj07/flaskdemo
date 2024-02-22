from app import create_app
from flask_socketio import SocketIO
from flask_cors import CORS

from app.Model.loadEnvironment import *

app = create_app()
CORS(app)

socketio = SocketIO(app,cors_allowed_origins="*")

if __name__ == "__main__":
    # waitress-serve --listen=127.0.0.1:8000 wsgi:app 
    socketio.run(app)
    

# Build Command : pip install -r requirements.txt
# Run Command waitress-serve --listen=127.0.0.1:8000 wsgi:app
