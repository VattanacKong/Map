#%%
import folium
import json


m = folium.Map([11.5726398,  104.899008])
with open('/mnt/d/Tux/Math for AI/map project/coord.json', 'r') as file:
    coord = json.load(file)
    print(coord.keys())
    
for key in coord.keys():
    if 'location' in coord[key]:
        location = coord[key]['location']
        lat = location['lat']
        lng = location['lng']
        folium.Marker(
        location=[lat, lng],
        tooltip="Click me!",
        popup="Mt. Hood Meadows",
        icon=folium.Icon(icon="cloud"),
        ).add_to(m)
    else:
        continue

m
# %%
