import json
import re
from get_straight_line import straight_dis

with open('/mnt/d/TUX/Math for AI/mapproject/Data/cleaned3.json')as file:
    districts = json.load(file)
    

def get_graph(districts, destination):
    temp = {}
    #get origin coord to calculate straight line
    destination_dicts = [items for items in districts[destination] if isinstance(items, dict)] 
    for destination_key, destination_value in destination_dicts[0].items():
        destination_coords = destination_value['location']
    #base district 
    for main_key, value in districts.items():
        neighbors = []
        dicts_only= [item for item in value if isinstance(item, dict)]
        #dictionary that store coords of the main key
        for key,value in dicts_only[0].items():
            coords = value['location']
        #neighbors dictionaries
        for i in dicts_only[1:]:
            #neighbor districts that were saved as dictionaries
            for key, value in i.items():
                #get coords of the current neighbor
                current =[items for items in districts[key] if isinstance(items, dict)]
                for a, b in current[0].items():
                    nei_coords = b['location']
                distance = straight_dis(list(destination_coords.values()), list(nei_coords.values()))
                #add all data as content and add to temp
                content = [key, value['distance'], value['duration'], distance]
                neighbors.append(content)
        temp[main_key] = neighbors + list(coords.values())
    return temp

def gbfs(origin, destination, districts):
    distances = []
    open = [origin]
    close = []
    graph = get_graph(districts,destination)
    while open:
        node = open.pop(0)
        if node not in close:
            close.append(node)
            neighbors = graph[node][:-2]
            neighbors.sort(key = lambda x: x[-1])
            next_open, distance, duration, straight_Line = neighbors.pop(0)
            open.append(next_open)
            distances.append(distance)
            if open[0] == destination:
                close.append(destination)
                total_distance = []
                for distance in distances:
                    total_distance.append(float(re.findall('\d*\.*\d', distance)[0]))
                print(sum(total_distance))
                print(close)
                return close
            
        
        
        

