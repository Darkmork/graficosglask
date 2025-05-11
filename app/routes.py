from flask import Blueprint, jsonify, request, send_file
from io import BytesIO
from app.utils.chart_generator import generate_chart

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def home():
    return jsonify({"message": "Bienvenido a la API de generación de gráficos"})


@main_bp.route('/generate-chart', methods=['POST'])
def generate_chart_endpoint():
    data = request.json

    # Validar datos de entrada
    if not data or 'chart_type' not in data:
        return jsonify({"error": "Datos inválidos"}), 400

    try:
        # Generar el gráfico
        img = generate_chart(
            chart_type=data['chart_type'],
            x_data=data.get('x_data'),
            y_data=data.get('y_data'),
            title=data.get('title', 'Gráfico generado'),
            x_label=data.get('x_label', 'Eje X'),
            y_label=data.get('y_label', 'Eje Y')
        )

        # Devolver la imagen
        return send_file(img, mimetype='image/png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500