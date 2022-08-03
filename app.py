from flask import Flask, request, jsonify
from utils import validate_json
from deposit import get_amount

app = Flask(__name__)


@app.route('/')
def api():
    try:
        if request.json and validate_json(request.json):
            result = get_amount(request.json)
        else:
            result = {'error': 'Ошибка валидации входящего JSON'}
            return jsonify(result), 400
    except Exception as exc:
        result = {'error': f'Внутренняя ошибка: {str(exc)}'}
        return jsonify(result), 400
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
