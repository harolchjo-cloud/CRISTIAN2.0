from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

peritajes = []
inventario = []

@app.route('/api/peritajes', methods=['POST'])
def guardar_peritaje():
    data = request.get_json()
    if not data or "placa" not in data:
        return jsonify({"error":"Debes enviar la placa ej Json"}), 400
    nuevo = {
        "placa": data["placa"].upper()  # FIX: mayusculas forzadas,
        "hora": str(datetime.datetime.now())
    }
    peritajes.append(nuevo)
    return jsonify({"mensaje": "Peritaje registrado", "placa": nuevo["placa"]}), 201

@app.route('/api/peritajes', methods=['GET'])
def ver_peritajes():
    return jsonify({"peritajes": peritajes})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

#Simulacion de el desarrollo de una nueva ruta
@app.route('/api/inventario', methods=['GET'])
def inventario_wip():
    pass
