import streamlit as st
import pandas as pd
import requests
import folium
import streamlit_folium

'''
# TaxiFareModel, kai-pre version
'''
st.markdown('''
Website to predict NY taxi fares''')



date = st.date_input(
    label="Please enter a departure date: ",
    format = "YYYY/MM/DD")

time = st.time_input(
    label="Please enter a departure time: ")

deplat = st.number_input('Please specify departure latitude: ', value = 40.75749697)
deplon = st.number_input('Please specify departure longitude: ', value = -73.971162782)

droplat = st.number_input('Please specify dropoff latitude: ', value = 40.7620270)
droplon = st.number_input('Please specify dropoff longitude: ', value = -73.971321)

passcount = st.number_input('Please enter passenger count: ', value = 1)



#mapdata = pd.DataFrame(
#            [[deplat, deplon], [droplat, droplon]],
#            columns=['lat', 'lon']
#        )
#st.map(mapdata, zoom = 12)


# Create a Folium map
center = [(deplat + droplat) / 2, (deplon + droplon) / 2]
route = [[deplat, deplon], [droplat, droplon]]
map = folium.Map(location=center, tiles="Cartodb Positron", zoom_start=13)

folium.Marker([droplat, droplon], draggable = True).add_to(map)
folium.Marker([deplat, deplon], draggable = True).add_to(map)

marker1name = list(map.to_dict()["children"])[1]
marker2name = list(map.to_dict()["children"])[2]

folium.PolyLine(route,
                color='green',
                weight=5,
                opacity=0.8).add_to(map)

map.fit_bounds([min(route), max(route)], padding = [10, 10])

imap = streamlit_folium.st_folium(map)

print(imap)



url = 'https://taxifare.lewagon.ai/predict'

if st.button('Predict the fare'):
    st.write('Fare predicted: ')
    params = {"pickup_datetime": " ".join([str(date), str(time)]), "pickup_longitude": deplon,
            "pickup_latitude": deplat, "dropoff_longitude": droplon,
            "dropoff_latitude": droplat, "passenger_count": passcount}

    apicall = requests.get(url, params = params, timeout = 10)
    st.text(f"The fare for the queried taxi ride is {round(apicall.json()['fare'], 2)} dollars.")
else:
    st.write('(Press button to predict fare)')
