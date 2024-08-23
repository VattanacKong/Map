import requests
import json

API_KEY = 'xxxxx'
base_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'
districts = [
    'Chamkar Mon, Phnom Penh', 'Tuol Kouk, Phnom Penh', 'Koh Thom, Kandal',
    'Chbar Ampov, Phnom Penh', 'Dangkao, Phnom Penh'
]
filename = 'coord.json'

def get_coords(params):
    response = requests.get(base_URL, params= params).json()
    if response['status'] == 'OK':
        result = response['results']
        geometry = result[0]['geometry']
        adr = result[0]['formatted_address']
        coord = geometry['location']
        content = {
            'address' : adr,
            'location': coord
        }
        with open('coord.json', 'w') as file:
            json.dump(content, file, indent = 4)
        print('success')
    else:
        content = {
            'address' : 'a coord could not be found'
        }
        with open('coord.json', 'w') as file:
            json.dump(content, file, indent = 4)
            
            
            
for district in districts:
    params = {'key' : API_KEY,'address' : district}
    get_coords(params)

    
