import pandas as pd

tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_districts,_municipalities_and_sections_in_Cambodia')
name = 'Name'
dis = []
for table in tables:
    if name in table:
        dis.append(table[name])
    else:
        continue
districts =sorted(list(pd.concat(dis, ignore_index= True))) 

def get_dist():
    return districts