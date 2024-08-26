import folium
import json
from get_straight_line import get_lat_lng


m = folium.Map([11.5726398,  104.899008])
with open('/mnt/d/TUX/Math for AI/map project/Data/cleaned3.json', 'r') as file:
    districts = json.load(file)
    
    
for district in districts:
    coords = get_lat_lng(district)
    lat = coords['lat']
    lng = coords['lng']
    folium.Marker(
    location=[lat, lng],
    icon=folium.Icon(icon="cloud", color='blue'),
    popup= district
    ).add_to(m)
    neighbors = [i for i in districts[district] if type(i) is str]
    for neig in neighbors:
        n_coords = get_lat_lng(neig)
        n_lat = n_coords['lat']
        n_lng = n_coords['lng']
        folium.Marker(
        location=[n_lat, n_lng],
        icon=folium.Icon(icon="cloud", color='red'),
        popup=neig
        ).add_to(m)
        trail_coords = [(lat, lng),(n_lat, n_lng)]
        folium.PolyLine(trail_coords).add_to(m)

m.save('index1.html')