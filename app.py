from flask import Flask, request, jsonify

app = Flask(__name__)

# Anasayfa Endpoint
@app.route("/")
def home():
    return "REST API çalışıyor!", 200

# Toplama İşlemi (GET)
@app.route("/add", methods=["GET"])
def add_numbers():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        result = a + b
        return jsonify({"result": result}), 200
    except ValueError:
        return jsonify({"error": "Geçerli bir sayı girin."}), 400

# Çarpma İşlemi (POST)
@app.route("/multiply", methods=["POST"])
def multiply_numbers():
    try:
        data = request.get_json()
        # JSON doğrulama
        if not data or "num1" not in data or "num2" not in data:
            return jsonify({"error": "JSON verisi eksik ya da hatalı"}), 400
        num1 = int(data.get("num1", 0))
        num2 = int(data.get("num2", 0))
        result = num1 * num2
        return jsonify({"result": result}), 200
    except (ValueError, TypeError):
        return jsonify({"error": "Geçerli bir JSON verisi gönderin."}), 400

# Uygulamayı başlat
if __name__ == "__main__":
    app.run(port=2144, debug=True)
