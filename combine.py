from get_coords import get_coords as gcoord
from get_neighbors import get_dist_and_neig as gdist
import json

#This file combines districts with neighbors and coords into one file

API_KEY = 'xxxxxxxxxx'
districts = gdist('/mnt/d/Tux/Math for AI/map project/Data/district.geojson')
for district in districts:
    para = {'key': API_KEY, 'address': district}
    lat_lon = gcoord(para)
    districts[district].append(lat_lon)
    
with open('/mnt/d/Tux/Math for AI/map project/Data/unclean.json', 'w') as file:
    json.dump(districts, file, indent = 4)