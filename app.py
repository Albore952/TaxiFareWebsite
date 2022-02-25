import streamlit as st

'''
# TaxiFareModel front
'''

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

import datetime

date = st.date_input("Date?")
time = st.time_input("Time?")
#st.write('Your birthday is:', d)
pickup_longitude = st.number_input('pickup longitude?', value = -73.950655)
pickup_latitude = st.number_input('pickup latitude?', value = 40.783282)
dropoff_longitude = st.number_input('dropoff longitude?', value = -73.984365)
dropoff_latitude = st.number_input('dropoff latitude?', value = 40.769802)
passenger_count = st.number_input('passenger count?', value = 1)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'
import requests

params = {
    "pickup_datetime": f"{date} {time}",
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

response = round(requests.get(url, params=params).json()['fare'],2)

response

'''

2. Let's build a dictionary containing the parameters for our API...



print(response)

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
