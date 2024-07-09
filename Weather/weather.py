import tkinter as tk
from tkinter import messagebox
import requests

def search():
    location=location_entry.get()
    api_key="b450ba2b6752c95c662e8fd00fff1bb7"
    url= f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    try:
        
        response = requests.get(url)
        data = response.json()
            
        current = data["main"]
        daily = data["wind"]
        
        temperature = current["temp"]- 273.15
        pressure = current["pressure"]
        humidity = current["humidity"]
        wind_speed = daily["speed"]
        
        perciption = 0 # no perciption in api data

        result = (f"Temperature: {temperature}°C\n"
                  f"Pressure: {pressure} hPa\n"
                  f"Humidity: {humidity}%\n"
                  f"Wind Speed: {wind_speed} m/s\n"
                  f"Chance of Rain: {perciption}%")
        
        weather_result.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

window = tk.Tk()
window.title("Weather Forecast")
window.minsize(width=300, height=250)

frame_buttons = tk.Frame(window,relief=tk.RAISED)
search_btn = tk.Button(frame_buttons, text="Search", command=search, height=1)
search_btn.grid(column=8, row=0 , sticky="ne" , padx=5 , pady=5)

frame_buttons.grid(column=8 , row=0 , sticky="ns")
tk.Label(window, text="Enter location:").grid(column= 4,sticky="ne", row=0 ,pady=5)
location_entry = tk.Entry(window)
location_entry.grid(column= 5,sticky="ne", row=0 ,pady=5)

weather_result = tk.Label(window, text="", justify="left", font=("Helvetica", 12))
weather_result.grid(pady=20)

window.mainloop()
