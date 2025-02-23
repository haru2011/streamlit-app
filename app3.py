import requests
import streamlit as st
st.title('Weather Forecast')
city_id = st.text_input('Enter city ID', '400040')
if st.button('Get forecast'):
    response = requests.get(f'https://weather.tsukumijima.net/api/forecast/city/{city_id}')
    if response.status_code == 200:
        data = response.json()
        st.write(data
                 )
    else:
        st.write('Error:', response.status_code)