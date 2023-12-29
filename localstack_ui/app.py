from flask import Flask, render_template
import json

app = Flask(__name__)

# Read the config.json file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

@app.route('/')
def landing_page():
    return render_template('landing_page.html', services=config['top_level_services'])

@app.route('/<service_url>')
def service_page(service_url):
    service = next((s for s in config['top_level_services'] if s['service_url'] == service_url), None)
    if service:
        return f"<h1>{service['service_name']}</h1>"
    return "Service not found"

if __name__ == '__main__':
    app.run(debug=True)

