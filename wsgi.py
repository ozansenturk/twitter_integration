from rest import create_app
import os
from rest import api

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
api.init_app(app)

if __name__ == "__main__":
    app.run(port=5000)