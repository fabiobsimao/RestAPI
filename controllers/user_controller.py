# controllers/user_controller.py
from flask_restx import Namespace, Resource
from models.user_model import user_model

api = Namespace('users', description="Operações relacionadas a usuários")

# Registrar o modelo
user_dto = user_model(api)

# Endpoints
users = []

@api.route('/')
class UserList(Resource):
    @api.marshal_list_with(user_dto)
    def get(self):
        """Retorna todos os usuários"""
        return users

    @api.expect(user_dto)
    def post(self):
        """Cria um novo usuário"""
        new_user = api.payload
        users.append(new_user)
        return {"message": "Usuário criado com sucesso!"}, 201
