import requests
import json
import get_districts as getd

API_KEY = 'xxxxxxxxxxx'
base_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'
districts = getd.get_dist()
filename = 'coord.json'
failed_to_find = []
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
        print(f'Success: {district}')
    else:
        content = {
            district : 'coord could not be found'
        }
        main_dic.update(content)
        print(f'Fail: {district}')
        failed_to_find.append(district)
            

main_dic  = {}
            
for district in districts:
    params = {'key' : API_KEY,'address' : district}
    get_coords(params)

with open('your directory', 'w') as file:
    json.dump(main_dic, file, indent = 4)

print(f'Failed to find: {failed_to_find}')
