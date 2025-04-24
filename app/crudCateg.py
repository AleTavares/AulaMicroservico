from flask import Flask, request, jsonify
from flasgger import Swagger
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter
import Util.bd as bd
import base64

app = Flask(__name__)

# Configuração do Swagger
swagger = Swagger(app)

# Configuração do Prometheus
metrics = PrometheusMetrics(app, default_labels={'app_name': 'flask_app'})

# Métricas personalizadas para sucessos e erros
success_counter = Counter(
    'http_success_count', 'Contagem de respostas HTTP com sucesso',
    ['endpoint', 'method', 'status']
)

error_counter = Counter(
    'http_error_count', 'Contagem de respostas HTTP com erro',
    ['endpoint', 'method', 'status']
)

@app.after_request
def after_request(response):
    """
    Middleware para capturar os retornos de todos os endpoints.
    """
    endpoint = request.path
    method = request.method
    status = response.status_code

    if 200 <= status < 300:
        success_counter.labels(endpoint=endpoint, method=method, status=str(status)).inc()
    else:
        error_counter.labels(endpoint=endpoint, method=method, status=str(status)).inc()

    return response

@app.route('/categories', methods=['POST'])
def create_category():
    """
    Cria uma nova categoria.
    ---
    tags:
      - Categories
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            category_id:
              type: integer
            category_name:
              type: string
            description:
              type: string
            picture:
              type: string
    responses:
      201:
        description: Categoria criada com sucesso.
      400:
        description: Erro ao criar a categoria.
    """
    data = request.get_json()
    conn = bd.create_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO categories (category_id, category_name, description, picture)
            VALUES (%s, %s, %s, %s)
            """,
            (data['category_id'], data['category_name'], data.get('description'), data.get('picture'))
        )
        conn.commit()
        return jsonify({"message": "Category created successfully"}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

@app.route('/categories/<int:category_id>', methods=['GET'])
def read_category(category_id):
    """
    Retorna uma categoria pelo ID.
    ---
    tags:
      - Categories
    parameters:
      - name: category_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Categoria encontrada.
      404:
        description: Categoria não encontrada.
    """
    conn = bd.create_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM categories WHERE category_id = %s", (category_id,))
        category = cursor.fetchone()
        if category is None:
            return jsonify({"error": "Category not found"}), 404
        return jsonify({
            "category_id": category[0],
            "category_name": category[1],
            "description": category[2],
            "picture": base64.b64encode(category[3]).decode('utf-8') if category[3] else None,
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)