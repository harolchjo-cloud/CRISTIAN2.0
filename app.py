from flask import Flask, request, jsonify
import os
import time
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
        "placa": data["placa"].upper(),
        "hora": str(datetime.datetime.now())
    }
    peritajes.append(nuevo)
    return jsonify({"mensaje": "Peritaje registrado", "placa": nuevo["placa"]}), 201

@app.route('/api/peritajes', methods=['GET'])
def ver_peritajes():
    return jsonify({"peritajes": peritajes})


@app.route("/api/health", methods=["GET"])
def health_check():
    sistema_archivos_ok = os.path.exists("/tmp") or os.path.exists(".")
    if sistema_archivos_ok:
        return jsonify({"status": "healthy", "timestamp": int(time.time()), "environment": "production-cloud", "uptime_check": "passed"}), 200
    else:
        return jsonify({"status": "unhealthy", "reason": "Storage unreachable"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
