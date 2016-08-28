from flask import Flask
from src.api import api_blueprint

import os
import sys

def create_app(config='config.DevelopmentConfig'):
    reload(sys)
    sys.setdefaultencoding('utf-8')

    app = Flask(__name__)
    app.config.from_object(config)

    app.secret_key = 'ABC_TEST'

    app.register_blueprint(api_blueprint)

    return app


app = create_app(config=os.environ.get('APP_SETTING', 'config.DevelopmentConfig'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 45000))
    app.run(host=app.config['HOST'], port=port, debug=True)