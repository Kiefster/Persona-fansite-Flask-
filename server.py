from distutils.log import debug
from flask_app import app
from flask_app.controllers import users, games
import os
from flask import flash,request,redirect,url_for
from werkzeug.utils import secure_filename
if __name__ =="__main__":
    app.run(debug=True)
    UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','png'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER