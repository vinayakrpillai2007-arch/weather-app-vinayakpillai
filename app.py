import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

st.set_page_config(page_title="Weather App",page_icon="❄️")

st.title("Weather App ❄️")

st.write("This app provides weather information for any location. Enter a city name to get the current weather conditions.")

city_name = st.text_input("Enter city name:")

if(st.button("Get Weather")):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric')
    if(response.status_code == 200):
        st.success("Weather data retrieved successfully!")
        data = response.json()

        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_condition = data['weather'][0]['description']
        name = data['name']
        country = data['sys']['country']

        st.subheader(f"Weather in {name}, {country}")

        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        
        col1.metric('Temperature ❄️', f"{temperature} °C")
        col2.metric('Humidity 💧', f"{humidity} %")
        col3.metric('Wind Speed 🌬️', f"{wind_speed} m/s")
        col4.metric('Weather Condition 🌤️', f"{weather_condition}")
    else :
        st.error("City not found. Please check the city name and try again.")