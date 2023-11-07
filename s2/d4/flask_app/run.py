from flask import Flask
from models import db  # Import the SQLAlchemy database instance from your models
from config import Config  # Import your configuration

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the SQLAlchemy database
db.init_app(app)

if __name__ == '__main__':
    app.run()
