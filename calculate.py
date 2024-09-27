from flask import Flask, request, jsonify

app = Flask(__name__)

# Простой калькулятор, поддерживающий сложение, вычитание, умножение и деление
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    operation = data.get("operation")
    num1 = data.get("num1")
    num2 = data.get("num2")

    if not all([operation, num1, num2]):
        return jsonify({"error": "Пожалуйста, передайте все необходимые параметры."}), 400

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({"error": "Параметры должны быть числами."}), 400

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return jsonify({"error": "Деление на ноль."}), 400
        result = num1 / num2
    else:
        return jsonify({"error": "Операция не поддерживается."}), 400

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
