ZONE_HOME = {
    "tl_y": 40.747935, # Top-Left Latitude (deg) https://www.latlong.net/ the bigger the zone, the more planes you'll get
    "tl_x": -73.686689, # Top-Left Longitude (deg)
    "br_y": 40.742993, # Bottom-Right Latitude (deg)
    "br_x": -73.668824 # Bottom-Right Longitude (deg)
}
LOCATION_HOME = [
    40.745488, # Latitude (deg)
    -73.680744 # Longitude (deg)
]
TEMPERATURE_LOCATION = "40.745488,-73.680744" #same as location home
TOMORROW_API_KEY = "4ZyWsCOtKqvnQqzL8tpVApXHO4nhs4ZW" # Get an API key from https://tomorrow.io they only allows 25 pulls an hour, if you reach the limit you'll need to wait until the next hour 
TEMPERATURE_UNITS = "imperial" #can use "metric" if you want, same for distance 
DISTANCE_UNITS = "imperial"
CLOCK_FORMAT = "12hr" #use 12hr or 24hr
MIN_ALTITUDE = 1000 #feet
BRIGHTNESS = 100
BRIGHTNESS_NIGHT = 50
NIGHT_BRIGHTNESS = False #True for on False for off
NIGHT_START = "22:00" #dims screen between these hours
NIGHT_END = "06:00"
GPIO_SLOWDOWN = 2 #depends what Pi you have I use 2 for Pi 3 and 1 for Pi Zero
JOURNEY_CODE_SELECTED = "JFK" #your home airport code
JOURNEY_BLANK_FILLER = " ? " #what to display if theres no airport code
HAT_PWM_ENABLED = False #only if you have soldered the PWM bridge use False if you didn't
FORECAST_DAYS = 3 #today plus the next two days
