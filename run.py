import json
from flask_sqlalchemy import SQLAlchemy
from plastic_pollution import plastic_pollution, views


plastic_pollution.run(debug=True, 
              host="0.0.0.0")
