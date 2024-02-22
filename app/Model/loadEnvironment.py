from dotenv import load_dotenv
import os


dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)

PORT = os.getenv("PORT")
HOSTNAME = os.getenv("HOSTNAME")
SECRETKEY = os.getenv('SECRETKEY')
