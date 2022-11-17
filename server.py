import random
from flask import Flask
from flask_restful import Api, Resource, reqparse


app = Flask('server')
api = Api(app)
ads_list = [
    {
        'id': 1,
        'title': 'Cat',
        'description': 'big cat',
        'date_create': '28.10.2022',
        'owner': 'Alise'
    },
    {
        'id': 2,
        'title': 'Dog',
        'description': 'Small dog',
        'date_create': '21.10.2022',
        'owner': 'Jack'
    }
]


class Ads(Resource):

    def get(self, id=0):
        if id == 0:
            return ads_list
        for ads in ads_list:
            if ads['id'] == id:
                return ads, 200
        return random.choice(ads_list), 200

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('title')
        parser.add_argument('description')
        parser.add_argument('date_create')
        parser.add_argument('owner')
        params = parser.parse_args()
        for ads in ads_list:
            if id == ads['id']:
                return f'Ad with id {id} already exists'
        ads = {
            'id': int(id),
            'title': params['title'],
            'description': params['description'],
            'date_create': params['date_create'],
            'owner': params['owner']
        }
        ads_list.append(ads)
        return ads, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('title')
        parser.add_argument('description')
        parser.add_argument('date_create')
        parser.add_argument('owner')
        params = parser.parse_args()
        ads = {
            'id': id,
            'title': params['title'],
            'description': params['description'],
            'date_create': params['date_create'],
            'owner': params['owner']
        }
        ads_list.append(ads)
        return ads, 201

    def delete(self, id):
        global ads_list
        ads_list = [ads for ads in ads_list if ads["id"] != id]
        return f"Ad with id {id} is deleted.", 200


api.add_resource(Ads, '/api_ads', '/api_ads/', '/api_ads/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)
