from flask import Flask, request, jsonify
from deposit import Deposit


def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def api():
        try:
            deposit_object = Deposit(**request.json)
            result = deposit_object.get_amount()
        except ValueError as ve:
            result = {'error': 'Ошибка валидации входящего JSON'}
            return jsonify(result), 400
        except Exception as exc:
            result = {'error': f'Внутренняя ошибка: {str(exc)}'}
            return jsonify(result), 500
        return jsonify(result)
    return app
