import streamlit as st
import requests

# OpenWeatherMap API details
API_KEY = "0d41e966a4c4d530e34ca782d81b5b05"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Streamlit page config
st.set_page_config(page_title="Weather App", page_icon="🌤️")

# App Title
st.title("Real-Time Weather App")
st.markdown("Check current temperature, weather conditions, and humidity in any city around the world.")

# User Input
city = st.text_input("Enter a city name")

# Button to get weather
if st.button("Get Weather"):
    if city:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            condition = data['weather'][0]['description'].title()
            humidity = data['main']['humidity']
            country = data['sys']['country']

            # Display weather info
            st.subheader(f"Weather in {city.title()}, {country}")
            st.metric(label="Temperature", value=f"{temperature} °C")
            st.write(f"**Condition:** {condition}")
            st.write(f"**Humidity:** {humidity}%")
        elif response.status_code == 404:
            st.error("City not found. Please enter a valid city name.")
        else:
            st.error("Something went wrong. Try again later.")
    else:
        st.warning("Please enter a city name to continue.")