import joblib
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Model for Stunting check
def Model_deteksi(Usia, Berat, Tinggi, JK):
    model = joblib.load('model.pkl')
    data = pd.DataFrame({
        'Usia': [Usia],
        'Berat': [Berat],
        'Tinggi': [Tinggi],
        'JK': [JK]
        })
    predictions = model.predict(data)[0]
    return predictions

@app.route('/deteksi', methods=['POST'])
def deteksi():
    data = request.get_json()
    if 'usia' in data and 'berat' in data and 'tinggi' in data and 'jk' in data:
        Usia = data['usia']
        Berat = data['berat']
        Tinggi = data['tinggi']
        JK = data['jk']
        model = Model_deteksi(Usia, Berat, Tinggi, JK)
        response = {
            'message': 'Deteksi Berhasil Dilakukan',
            'data': model
        }
        return jsonify(response), 200 
    else:
        return jsonify({'error': 'Data tidak lengkap'}), 400
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)