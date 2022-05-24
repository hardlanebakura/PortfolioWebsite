from flask_cors import CORS, cross_origin
from log_config import logging
from routing.routes import *
from routing.routes_api import *
from routing.routes_games import *

def create_app():
    app = Flask(__name__, template_folder = "Templates")

    set_config(app.config, app.jinja_env)

    db.init_app(app)
    #with app.app_context():
        #db.create_all()
    SESSION_TYPE = 'sqlalchemy'
    app.config.from_object(__name__)

    return app

app = create_app()

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#create all databases
#with app.app_context():
    #db.create_all()
# app = create_app()
# app.app_context().push()

app.register_blueprint(index_pages)
app.register_blueprint(api_pages)
app.register_blueprint(games_pages)

if __name__ == "__main__":
    app.run(debug = True)