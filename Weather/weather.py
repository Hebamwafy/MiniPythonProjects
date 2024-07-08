import tkinter as tk
from tkinter import messagebox
import requests

def search():
    location=location_entry.get()
    api_key="b450ba2b6752c95c662e8fd00fff1bb7"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    payload={}
    headers={
    "apikey": "b450ba2b6752c95c662e8fd00fff1bb7"
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    try:
        
        complete_url = f"{url}?q={location}&appid={api_key}&units=metric"
        response = requests.request("GET", complete_url, headers=headers, data=payload)
        data = response.json()
            
        current = data["current"]
        daily = data["daily"][0]
        
        temperature = current["temp"]
        pressure = current["pressure"]
        humidity = current["humidity"]
        wind_speed = current["wind_speed"]
        weather_description = current["weather"][0]["description"]
        
        precipitation = daily.get("pop", 0) * 100

        result = (f"Temperature: {temperature}°C\n"
                  f"Pressure: {pressure} hPa\n"
                  f"Humidity: {humidity}%\n"
                  f"Wind Speed: {wind_speed} m/s\n"
                  f"Description: {weather_description.capitalize()}\n"
                  f"Chance of Rain: {precipitation}%")
        
        weather_result.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

window = tk.Tk()
window.title("Weather Forecast")
window.rowconfigure(0,minsize=600)
window.columnconfigure(1,minsize=800)

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
