import json

with open('/mnt/d/Tux/Math for AI/map project/Data/cleaned3.json', 'r') as file:
    districts = json.load(file)


def get_path(destination, origin, store,path = []):   
    for i in store:
        if i[0] == destination:
            path.append(i)
            break
    if path[-1][1] == origin:
        return path
    else:
        new_destination = path[-1][1]
        return get_path(new_destination, origin, store, path)

def dfs(origin, destination, districts, open =[], close= [], store = []): 
    for neighbor in districts[origin]:
        if isinstance(neighbor, str) and (neighbor not in open) and(neighbor not in close):
            store.append([neighbor,origin])
            open.insert(0,neighbor)
    if origin not in close:
        close.append(origin)
    if open[0] == destination:
        path = get_path(destination,close[0],store )
        real_path = [destination]
        for i in path:
            real_path.insert(0,i[1])
        print(real_path)
        return real_path

    else:
        next_start = open[0]
        open.remove(open[0])
        dfs(next_start,destination,districts, open, close , store)
            
dfs('Tuol Kouk', "Kandal Stueng", districts)
