from flask_restful import Resource, reqparse
from models.hotel import HotelModel

# Classes usadas nos endpoints
class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}
    
class Hotel(Resource):
    args = reqparse.RequestParser()
    args.add_argument('nome')
    args.add_argument('estrelas')
    args.add_argument('diaria')
    args.add_argument('cidade')

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)

        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found.'}, 404

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': f'Hotel id {hotel_id} already exists.'}, 400

        dados = Hotel.args.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json()

    def put(self, hotel_id):
        dados = Hotel.args.parse_args()

        hotel_encontrado = HotelModel.find_hotel(hotel_id)

        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json(), 201

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            hotel.delete_hotel()
            return {'message': 'Hotel deleted.'}
        return {'message': 'Hotel not found.'}