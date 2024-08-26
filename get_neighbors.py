import geopandas as gpd
import json

#This file create a fuunction to retrieve districts and it's neighbors from a GeoJson dataset

def get_dist_and_neig(file):
    districts = gpd.read_file(file)
    content = {}
    #loop through each district to find neighbors
    for index, dist in districts.iterrows():
        content[dist['HRName']] = districts[districts.geometry.touches(dist.geometry)]['HRName'].tolist()
        print(f'success {index + 1}')
    return content




















# with open('/mnt/d/Tux/Math for AI/map project/districts.json', 'w') as file:
#     json.dump(content, file, indent = 3)
# %%
