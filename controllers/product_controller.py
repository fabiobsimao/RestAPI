# controllers/product_controller.py
from flask_restx import Namespace, Resource
from models.product_model import product_model

api = Namespace('products', description="Operações relacionadas a produtos")

# Registrar o modelo
product_dto = product_model(api)

# Endpoints
products = []

@api.route('/')
class ProductList(Resource):
    @api.marshal_list_with(product_dto)
    def get(self):
        """Retorna todos os produtos"""
        return products

    @api.expect(product_dto)
    def post(self):
        """Cria um novo produto"""
        new_product = api.payload
        products.append(new_product)
        return {"message": "Produto criado com sucesso!"}, 201
