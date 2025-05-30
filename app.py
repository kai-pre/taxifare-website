import streamlit as st
import requests

'''
# TaxiFareModel front
'''
st.date_input()
st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

date = st.date_input(
    label="Please enter a departure date: "
    format = "YYYY/MM/DD")

time = st.time_input(
    label="Please enter a departure time: "
    format = "")

deplat = st.number_input('Please specify departure latitude: ', value = 40.75749697)
deplon = st.number_input('Please specify departure longitude: ', value = -73.971162782)

droplat = st.number_input('Please specify dropoff latitude: ', value = 40.7620270)
dropplon = st.number_input('Please specify dropoff longitude: ', value = -73.971321)

passcount = st.number_input('Please enter passenger count: ', value = 1)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':
    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''
2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
params = {"pickup_datetime" = " ".join(date, time), "pickup_longitude" = deplon,
            "pickup_latitude" = deplat, "dropoff_longitude" = droplon,
            "dropoff_latitude" = droplat, "passenger_count" = passcount}

apicall = requests.get(url, timeout = 10)

#prediction = apicall.json()
st.json(apicall)
