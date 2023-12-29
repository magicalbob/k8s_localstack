#!/usr/bin/env python3
from flask import Flask, render_template
import json

app = Flask(__name__)

# Read the config.json file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

@app.route('/')
def landing_page():
    return render_template('landing_page.html', services=config['top_level_services'])

@app.route('/service/<service_url>')
def service(service_url):
    service = next((s for s in config['top_level_services'] if s['service_url'] == service_url), None)
    if service:
        sections = config.get(service_url, {})
        items = []
        for section_name, section_items in sections.items():
            for item in section_items:
                items.append(item)
        return render_template('service_page.html', service=service, sections=items)
    return "Service not found"

if __name__ == '__main__':
    app.run(debug=True)

