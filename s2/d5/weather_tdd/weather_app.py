# from flask import Flask, jsonify, request
# from weather_data import weather_data

# app = Flask(__name__)

# @app.route('/weather/<string:city>/', methods=['GET'])
# def get_weather(city):
#     # print(city,weather_data)
#     if city in weather_data:
#         print(weather_data[city])
#         return jsonify(weather_data[city], 200)
#     else:
#         return "City not found", 404


# @app.route('/weather/', methods=['POST'])
# def create_weather():
#     data = request.get_json()
#     city = data.get('city')
#     if city and city not in weather_data:
#         weather_data[city] = {'temperature': data.get('temperature'), 'weather': data.get('weather')}
#         return 'Weather data created', 201
#     return 'Invalid request', 400

# @app.route('/weather/<string:city>/', methods=['PUT'])
# def update_weather(city):
#     data = request.get_json()
#     if city in weather_data:
#         weather_data[city]['temperature'] = data.get('temperature', weather_data[city]['temperature'])
#         weather_data[city]['weather'] = data.get('weather', weather_data[city]['weather'])
#         return 'Weather data updated'
#     return 'City not found', 404

# @app.route('/weather/<string:city>/', methods=['DELETE'])
# def delete_weather(city):
#     if city in weather_data:
#         del weather_data[city]
#         return 'Weather data deleted'
#     return 'City not found', 404

# if __name__ == '__main__':
#     app.run()

from flask import Flask, jsonify, request
from weather_data import weather_data

app = Flask(__name__)

@app.route('/weather/<string:city>/', methods=['GET'])
def get_weather(city):
    if city in weather_data:
        return weather_data[city], 200
    else:
        return "City not found", 404

@app.route('/weather/', methods=['POST'])
def create_weather():
    data = request.get_json()
    city = data.get('city')
    if city and city not in weather_data:
        weather_data[city] = {'temperature': data.get('temperature'), 'weather': data.get('weather')}
        return 'Weather data created', 201
    return 'Invalid request', 400

@app.route('/weather/<string:city>/', methods=['PUT'])
def update_weather(city):
    data = request.get_json()
    if city in weather_data:
        weather_data[city]['temperature'] = data.get('temperature', weather_data[city]['temperature'])
        weather_data[city]['weather'] = data.get('weather', weather_data[city]['weather'])
        return 'Weather data updated'
    return 'City not found', 404

@app.route('/weather/<string:city>/', methods=['DELETE'])
def delete_weather(city):
    if city in weather_data:
        del weather_data[city]
        return 'Weather data deleted'
    return 'City not found', 404

if __name__ == '__main__':
    app.run()
