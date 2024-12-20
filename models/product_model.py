# models/product_model.py
from flask_restx import fields

def product_model(api):
    return api.model('Product', {
        'id': fields.Integer(description="ID do produto", required=True),
        'name': fields.String(description="Nome do produto", required=True),
        'price': fields.Float(description="Preço do produto", required=True),
    })
