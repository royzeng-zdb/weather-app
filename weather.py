from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    weather_api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY'
    response = requests.get(weather_api_url)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

    weather_data = response.json()
    if 'main' not in weather_data or 'temp' not in weather_data['main']:
        return jsonify({'error': 'Failed to parse weather data'}), 500

    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']

    return jsonify({'city': city, 'temperature': temperature, 'description': description}), 200

if __name__ == '__main__':
    app.run(debug=True)

