from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/tasker', methods=['POST'])
def tasker():
    data = request.get_data()  # Obtener los datos de la solicitud sin procesar
    print("Datos recibidos desde Tasker:", data)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
