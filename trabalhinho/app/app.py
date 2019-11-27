
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
# from flask_login import LoginManager


# from config import Config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pegasus.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)

# from app
import routes
# from app 
import models
# from .models 
from models import Produto
# from models import models

if __name__ == "__main__":
    app.run(debug=True)