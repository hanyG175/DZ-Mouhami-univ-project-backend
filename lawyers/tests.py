# views.py

import requests
import requests

def get_coordinates(address):
    url = f'https://nominatim.openstreetmap.org/search?q={address}&format=json'
    response = requests.get(url)
    data = response.json()
    if data:
        location = data[0]  # Assuming the first result is the most relevant
        return float(location['lat']), float(location['lon'])
    else:
        return None

# Usage example
coordinates = get_coordinates('1600 Amphitheatre Parkway, Mountain View, CA')
if coordinates:
    print('Latitude:', coordinates[0])
    print('Longitude:', coordinates[1])
else:
    print('Failed to retrieve coordinates')

