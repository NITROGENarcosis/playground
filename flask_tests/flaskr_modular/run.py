from flask import Flask
from views.home import home
from views.admin import admin

#config
DATABASE = 'flaskr'
DB_HOST = 'devdbhost'
DB_USER = 'lamar'
DB_PASS = 'the333'
DEBUG = True
SECRET_KEY = 'dev_key'
USERNAME = 'admin'
PASSWORD = 'qwerty'

app = Flask(__name__)
app.config.from_object(__name__)
app.register_blueprint(home)
app.register_blueprint(admin)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
