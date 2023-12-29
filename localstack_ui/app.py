#!/usr/bin/env python3
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def landing_page():
    # Read the configuration from config.json
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)

    # Extract the top-level services from the config
    top_level_services = config_data.get('top_level_services', [])

    return render_template('landing_page.html', top_level_services=top_level_services)

if __name__ == '__main__':
    app.run(debug=True)

