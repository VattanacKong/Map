import requests

#This file create a function to retrieve coords of the selected district from geocoding api

def get_coords(parameters):
    base_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_URL, params= parameters).json()
    main_dic  = {}
    failed_to_find = []
    district = parameters['address']
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
    print(f'Failed to find: {failed_to_find}')
    return main_dic

