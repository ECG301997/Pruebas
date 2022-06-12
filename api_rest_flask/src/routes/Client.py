from flask import Blueprint, jsonify

#Models
from models.Client_model import ClientModel

main = Blueprint('client_blueprint',__name__)

@main.route('/')
def get_client():
    try:
        clients = ClientModel.get_client()
        return jsonify(clients)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
