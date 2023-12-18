import folium
from folium.plugins import MarkerCluster
import pandas as pd
import requests

def json_to_df(data):
    elements = data['elements']
    places = {'category': [], 'lat': [], 'lon': [], 'name': [], 'address': []}
    
    for i in elements:
        
        tipo = i.get('tags', None).get('amenity', None)
        latitude = i.get('lat', None)
        longitude = i.get('lon', None)
        name = i.get('tags', {}).get('name', "NO NAME")
        street = i.get('tags', {}).get('addr:street', "NO STREET")
        number = i.get('tags', {}).get('addr:housenumber', 9999)

        places['category'].append(tipo)
        places['lat'].append(latitude)
        places['lon'].append(longitude)
        places['name'].append(name)
        places['address'].append(street + ' ' + str(number))

            
    return pd.DataFrame(places)

list_health = ["hospital", "clinic", "doctors"]

dataframes = []
for amenity in list_health: 
    overpass_url = "http://overpass-api.de/api/interpreter"

    overpass_query = f"""
    [out:json];
    node["amenity"= {amenity}]
      (40.40, -3.71,40.54, -3.60);
    out;
    """
    # the bridge está en el Latitud: 40.421703 Longitud: -3.691725
    response = requests.get(overpass_url, params={'data': overpass_query})
    try: 
        data = response.json()
        df = json_to_df(data)
        dataframes.append(df)
    except:
        continue

health_csv = pd.concat(dataframes)

coordenadas_TB = (40.421703,-3.691725)


some_map2 = folium.Map(location=coordenadas_TB, zoom_start=14)



#for row in subset.itertuples():
some_map2.add_child(folium.Marker(location=[40.421703,-3.691725], popup="The Bridge", 
                               icon=folium.Icon(icon='home', color='red')))
    


mc = MarkerCluster()

for row in health_csv.itertuples():
    mc.add_child(folium.Marker(location = [row.lat, row.lon], popup=row.name,
                                     icon=folium.Icon(icon='glyphicon glyphicon-heart-empty', color='blue')))
    
some_map2.add_child(mc)


some_map2.save('templates/map.html')