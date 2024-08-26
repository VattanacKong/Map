import json
import geopy.distance

#This file will create a new file and write straight line from one district to another
#For instance, if my destination was  Kork district

destination ={
        "lat": 11.561158,
        "lng": 104.8980058
        }

with open('/mnt/d/TUX/Math for AI/map project/Data/cleaned2.json', 'r') as file:
    districts = json.load(file)

content = {}

#This function return straight line distance from one origin to one destination in km
def straight_dis(origin, destination):
    coords1 = (origin['lat'], origin['lng'])
    coords2 = (destination['lat'], destination['lng'])
    result = geopy.distance.geodesic(coords1, coords2).km
    return result
#This function retrieve lat and lng of the chosen district from the main data file
def get_lat_lng(district):
    location_data = None
    for item in districts[district]:
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, dict) and 'location' in value:
                    location_data = value['location']
                    return location_data
        if location_data:
            break 


for district in districts:
    origin = get_lat_lng(district)
    distance = straight_dis(origin, destination)
    content.update({district: distance})
    
with open('/mnt/d/TUX/Math for AI/map project/Data/straight_line.json', 'w') as file:
    json.dump(content, file, indent = 1)
