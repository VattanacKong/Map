import requests
import json

API_KEY = 'xxxxxxxx'
base_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'
districts = [
    'Chamkar Mon, Phnom Penh', 'Tuol Kouk, Phnom Penh', 'Koh Thom, Kandal',
    'Chbar Ampov, Phnom Penh', 'Dangkao, Phnom Penh', 'd'
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
            adr : {'location' : coord}
        }
        main_dic.update(content)
        print('success')
    else:
        content = {
            district : 'coord could not be found'
        }
        main_dic.update(content)
        print('fail')
            

main_dic  = {}
            
for district in districts:
    params = {'key' : API_KEY,'address' : district}
    get_coords(params)

with open('your file directory', 'w') as file:
    json.dump(main_dic, file, indent = 4)
    
