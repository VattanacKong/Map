import requests
import json

#This file create a function to retrieve distances and durations of each district to each of it's neighbors by using Distanace Matrix api

API_KEY = 'xxxxxxxxxxxxx'
def get_distance(parameters):
    URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?parameters'
    response = requests.get(URL, parameters).json()
    rows = response['rows'][0]
    element= rows['elements']
    if element[0]['status'] == 'OK':
        distance = element[0]['distance']
        duration = element[0]['duration']
        content = {
            parameters['destinations']: {
            "distance" : distance['text'], 
            "duration" : duration['text']
            }
        }
        print('success')
    else:
        content = {
            parameters['destinations']: 'Failed to retrieve data'
        }
        print('fail')
    return content



#This section call the function above and write all the data to a new file called 'unclean2.json'

with open('/mnt/d/Tux/Math for AI/map project/Data/cleaned.json', 'r')as file:
    districts = json.load(file)

for district in districts:
    neighbors = districts[district]
    for neig in neighbors[:-1]:
        para = {
            'destinations' : neig,
            'origins' : district,
            'key': API_KEY
        }
        dist_dur = get_distance(para)
        districts[district].append(dist_dur)

with open('/mnt/d/Tux/Math for AI/map project/Data/uncleaned2.json', 'w') as file:
    json.dump(districts, file, indent = 4)