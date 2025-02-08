import requests

API_KEY = "ViH7SiJScZEoAGk8mE88QYLQTuDYkITh"
URL = f"https://wallhaven.cc/api/v1/search?q=space&sorting=random&apikey={API_KEY}"

response = requests.get(URL)
data = response.json()

# Print the first wallpaper URL
print(data["data"][0]["path"])

