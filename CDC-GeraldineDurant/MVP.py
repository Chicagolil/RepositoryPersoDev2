from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def dashboard():
    
    sites = ["http://example.com", "http://example.org"]
    status = {}

    for site in sites:
        try:
            response = requests.get(site)
            status[site] = "En ligne" if response.status_code == 200 else "Hors ligne"
        except requests.ConnectionError:
            status[site] = "Hors ligne"

    return render_template('dashboard.html', status=status)

if __name__ == '__main__':
    app.run(debug=True)
