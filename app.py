from flask import Flask
from views import views

app = Flask(__name__, static_url_path='', static_folder='templates', template_folder='templates')
app.register_blueprint(views, url_prefix="/119161005")


if __name__ == '__main__':
    app.run(debug=True, port=8000)
