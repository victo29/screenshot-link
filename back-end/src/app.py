from flask import Flask
from flask_cors import CORS
from controllers.ScreeshotController import screenshot_bp
import os



BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), 'static'), 
    static_url_path='/static'
)

CORS(app)

app.register_blueprint(screenshot_bp)

if __name__ == "__main__":
    app.run(debug=False, threaded=False)