# app.py (Instância Principal)
from flask import Flask
from flask_restx import Api
from controllers.user_controller import api as user_ns
from controllers.product_controller import api as product_ns

app = Flask(__name__)
api = Api(
    app,
    version="1.0",
    title="Exemplo de API REST",
    description="API estruturada por namespaces com Flask-RestX",
)

# Registrar os namespaces
api.add_namespace(user_ns, path="/users")
api.add_namespace(product_ns, path="/products")

if __name__ == "__main__":
    app.run(debug=True)
