import streamlit as st
import requests
from datetime import datetime

# OpenWeatherMap API details
API_KEY = "0d41e966a4c4d530e34ca782d81b5b05"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Streamlit page config
st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")

# App Title
st.title("🌍 Real-Time Weather App")
st.markdown("Check current weather conditions anywhere in the world")

# User Input
col1, col2 = st.columns([3, 1])
with col1:
    city = st.text_input("Enter a city name", placeholder="e.g., London, Tokyo")
with col2:
    unit = st.selectbox("Unit", ("°C", "°F"), index=0)

# Button to get weather
if st.button("Get Weather", type="primary"):
    if city:
        try:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric" if unit == "°C" else "imperial"
            }
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()  # Raises exception for 4XX/5XX errors
            
            data = response.json()
            
            # Extract weather data
            temperature = data['main']['temp']
            condition = data['weather'][0]['description'].title()
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            country = data['sys']['country']
            icon_code = data['weather'][0]['icon']
            
            # Get current time
            timezone_offset = data['timezone']
            current_time = datetime.utcnow().timestamp() + timezone_offset
            local_time = datetime.fromtimestamp(current_time).strftime('%I:%M %p, %b %d')
            
            # Display weather info
            st.subheader(f"{city.title()}, {country}")
            st.caption(f"Local time: {local_time}")
            
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(f"http://openweathermap.org/img/wn/{icon_code}@2x.png", width=100)
            with col2:
                st.metric(label="Temperature", value=f"{temperature:.1f} {unit}")
            
            st.write(f"**Condition:** {condition}")
            st.write(f"**Humidity:** {humidity}%")
            st.write(f"**Wind Speed:** {wind_speed} {'km/h' if unit == '°C' else 'mph'}")
            
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                st.error("City not found. Please check the spelling and try again.")
            else:
                st.error(f"API Error: {str(e)}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a city name")
