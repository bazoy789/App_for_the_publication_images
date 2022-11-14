from flask import Flask, render_template, request

from app.main1.views import catalog_blueprint
from app.api.views import api_blueprint

app = Flask(__name__)

app.register_blueprint(catalog_blueprint)
app.register_blueprint(api_blueprint)
app.config['JSON_AS_ASCII'] = False


@app.errorhandler(404)
def error404(error):
    return 'Статус кода 404'

@app.errorhandler(500)
def error500(error):
    return 'Статус кода 500'


if __name__ == '__main__':
    app.run()
