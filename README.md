#  Real-Time Weather App

A Streamlit web application that fetches and displays current weather data for any city worldwide using the OpenWeatherMap API.

## Features

-  Search weather by city name
-  Temperature display in °C or °F
-  Humidity percentage
-  Wind speed with appropriate units
-  Weather condition with visual icons
-  Local time display for searched location
-  Mobile-responsive design


##  How It Works
1. Enter a city name in the search field
2. Choose preferred temperature unit (°C or °F)
3. Click **"Get Weather"** to fetch current weather data
4. View detailed weather information including:
   - Current temperature
   - Weather condition
   - Humidity percentage
   - Wind speed
   - Local time
   - Smart weather tip based on temperature

##  Smart Weather Notifications
Based on the current temperature:
- If it's **≥ 30°C**, you'll see:  
  ` It’s quite hot in [City] today!`
- If it's **≤ 18°C**, you'll see:  
  ` It’s chilly in [City], dress warm!`
- Otherwise, it will display:  
  ` The weather in [City] seems pleasant.`
   

## Installation

### Prerequisites
- Python 3.8+
- Streamlit
- Requests library

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
Install dependencies:

bash
pip install -r requirements.txt
Get your OpenWeatherMap API key:

Sign up at https://openweathermap.org/api

Get your free API key

Add your API key:

Replace API_KEY = "your_api_key_here" in the Python script

Running the App
bash
streamlit run weather_app.py
The app will launch in your default browser at http://localhost:8501

Deployment
Deploy to Streamlit Sharing:

Create a GitHub repository with your code

Go to Streamlit Sharing

Click "New app" and connect your GitHub repository

Set the main file path to weather_app.py

Click "Deploy"

Technologies Used
Python 3

Streamlit (Frontend)

Requests (API calls)

OpenWeatherMap API (Weather data)

Future Enhancements
5-day weather forecast

Air quality index

UV index

Precipitation probability

Historical weather data

Favorite locations

License
This project is licensed under the MIT License - see the LICENSE file for details.

Note: You'll need your own OpenWeatherMap API key (free tier available). The free tier has rate limits (60 calls/minute, 1,000,000 calls/month).


### Key Elements Included:
1. **Visual Header** with placeholder for screenshot
2. **Features** section highlighting key capabilities
3. **Clear Installation Instructions** with prerequisites
4. **API Key Guidance** for OpenWeatherMap
5. **Deployment Instructions** for Streamlit Sharing
6. **Technology Stack** overview
7. **Future Roadmap** for potential improvements
8. **License Information**
