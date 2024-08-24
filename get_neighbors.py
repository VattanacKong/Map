import geopandas as gpd
import json

districts = gpd.read_file('/mnt/d/Tux/Math for AI/map project/district.geojson')
content = {}

for index, dist in districts.iterrows():
    content[dist['HRName']] = districts[districts.geometry.touches(dist.geometry)]['HRName'].tolist()
    print(f'success {index + 1}')
    
with open('/mnt/d/Tux/Math for AI/map project/districts.json', 'w') as file:
    json.dump(content, file, indent = 3)