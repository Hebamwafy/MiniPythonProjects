import tkinter as tk
from tkinter import messagebox
import requests

def search():
    location = location_entry.get()
    api_key = "b450ba2b6752c95c662e8fd00fff1bb7"
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={api_key}"
    
    try:
        # Get latitude and longitude for the location
        geocode_response = requests.get(geocode_url)
        geocode_data = geocode_response.json()

        if len(geocode_data) == 0:
            messagebox.showerror("Error", "City Not Found")
            return

        lat = geocode_data[0]['lat']
        lon = geocode_data[0]['lon']

        # Get weather data using One Call API
        weather_url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,alerts&appid={api_key}&units=metric'
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        current = weather_data["current"]
        daily = weather_data["daily"][0]

        temperature = current["temp"]
        pressure = current["pressure"]
        humidity = current["humidity"]
        wind_speed = current["wind_speed"]
        weather_description = current["weather"][0]["description"]

        chance_of_rain = daily.get("pop", 0) * 100

        result = (f"Temperature: {temperature}°C\n"
                  f"Pressure: {pressure} hPa\n"
                  f"Humidity: {humidity}%\n"
                  f"Wind Speed: {wind_speed} m/s\n"
                  f"Description: {weather_description.capitalize()}\n"
                  f"Chance of Rain: {chance_of_rain}%")
        
        weather_result.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

window = tk.Tk()
window.title("Weather Forecast")
window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=800)

frame_buttons = tk.Frame(window, relief=tk.RAISED)
search_btn = tk.Button(frame_buttons, text="Search", command=search, height=1)
search_btn.grid(column=0, row=0, sticky="ne", padx=5, pady=5)

frame_buttons.grid(column=0, row=0, sticky="ns")
tk.Label(window, text="Enter location:").grid(column=1, row=0, padx=5, pady=5)
location_entry = tk.Entry(window)
location_entry.grid(column=2, row=0, padx=5, pady=5)

weather_result = tk.Label(window, text="", justify="left", font=("Helvetica", 12))
weather_result.grid(column=0, row=1, columnspan=3, padx=20, pady=20)

window.mainloop()
