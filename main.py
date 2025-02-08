import os
import requests
import sys

API_KEY = "CntQQfCou1HHhT3RlMnlqriifgIQyZrg"
KEYWORD = " ".join(sys.argv[1:])

URL = f"https://wallhaven.cc/api/v1/search?q={KEYWORD}&sorting=random&apikey={API_KEY}"

response = requests.get(URL)
data = response.json()

# Print the first wallpaper URL
print(data["data"][0]["path"])

# URL of the wallpaper (change this to any URL you want)
WALLPAPER_URL = data["data"][0]["path"]

# Path to save the wallpaper
WALLPAPER_PATH = os.path.expanduser("~/wali-wali/wallpaper.jpg")

def download_wallpaper(url, save_path):
    """Download an image from the URL and save it locally."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Wallpaper downloaded to {save_path}")
    else:
        print("Failed to download wallpaper.")

def set_wallpaper_sway(image_path):
    """Set wallpaper on SwayWM using swaybg."""
    os.system("swaymsg reload")

# Run the script
if __name__ == "__main__":
    download_wallpaper(WALLPAPER_URL, WALLPAPER_PATH)
    set_wallpaper_sway(WALLPAPER_PATH)
