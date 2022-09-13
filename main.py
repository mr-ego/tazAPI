from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/getlastdata')
def get_lastdata():
    data_point = [{'datetime': datetime.now().strftime("%m.%d.%Y %H:%M:%S"), 'temp1': 85, 'temp2': 85, 'temp3': 85, 'temp4': 85, 'temp5': 85 }]
    return jsonify(data_point)
