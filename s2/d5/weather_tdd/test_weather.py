import unittest
import json
from weather_app import app

class WeatherAppTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_weather_valid_city(self):
        response = self.app.get('/weather/Austin/')
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data, {"temperature": 32, "weather": "Hot"})

    def test_get_weather_invalid_city(self):
        response = self.app.get('/weather/NonExitentCity/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, b'City not found')

    def test_create_weather(self):
        data = {'city': 'NonExistentCity', 'temperature': 25, 'weather': 'Sunny'}
        response = self.app.post('/weather/', json=data)
        self.assertEqual(response.status_code, 201)

    def test_create_existing_city(self):
        data = {'New York':{'temperature': 22, 'weather': 'Cloudy'}}
        response = self.app.post('/weather/', json=data)
        self.assertEqual(response.status_code, 400)

    def test_update_weather(self):
        data = {'temperature': 15, 'weather': 'Rainy'}
        response = self.app.put('/weather/San%20Francisco/', json=data)
        self.assertEqual(response.status_code, 200)

    def test_update_nonexistent_city(self):
        data = {'temperature': 15, 'weather': 'Rainy'}
        response = self.app.put('/weather/NonExitentCity/', json=data)
        self.assertEqual(response.status_code, 404)

    def test_delete_weather(self):
        response = self.app.delete('/weather/New%20York/')
        self.assertEqual(response.status_code, 200)

    def test_delete_nonexistent_city(self):
        response = self.app.delete('/weather/NonExitentCity/')
        self.assertEqual(response.status_code, 404)
    
if __name__ == '__main__':
    unittest.main()
