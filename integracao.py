from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:74631234@DESKTOP-51TQN4P\\MSSQLSERVER01:50054/Dados?driver=SQL+Server'
db = SQLAlchemy(app)

class CasosFull(db.Model):
    __tablename__ = 'casos_full'
    __table_args__ = {'schema': 'dbo'}
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255))
    city_ibge_code = db.Column(db.String(255))
    date = db.Column(db.Date)
    epidemiological_week = db.Column(db.String(255))
    estimated_population = db.Column(db.Integer)
    estimated_population_2019 = db.Column(db.Integer)
    is_last = db.Column(db.Boolean)
    is_repeated = db.Column(db.Boolean)
    last_available_confirmed = db.Column(db.Integer)
    last_available_confirmed_per_100k_inhabitants = db.Column(db.Float)
    last_available_date = db.Column(db.Date)
    last_available_death_rate = db.Column(db.Float)
    last_available_deaths = db.Column(db.Integer)
    order_for_place = db.Column(db.Integer)
    place_type = db.Column(db.String(255))
    state = db.Column(db.String(255))
    new_confirmed = db.Column(db.Integer)
    new_deaths = db.Column(db.Integer)

@app.route('/visualizar_dados', methods=['GET'])
def visualizar_dados():
    casos = CasosFull.query.all()
    casos_json = [{'city': caso.city, 'date': caso.date, 'new_confirmed': caso.new_confirmed, 'new_deaths': caso.new_deaths} for caso in casos]
    return jsonify({'casos': casos_json})

if __name__ == '__main__':
    app.run(debug=True)

