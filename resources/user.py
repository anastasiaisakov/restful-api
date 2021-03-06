import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Can't be blank.")
    parser.add_argument('password', type=str, required=True, help="Can't be blank.")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "This user already exists."}

        user = UserModel(**data) #for each key set the value
        user.save_to_db()

        return {"message": "User created successfully."}, 201
