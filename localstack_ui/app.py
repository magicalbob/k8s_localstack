#!/usr/bin/env python3
from flask import Flask, render_template
import json
import subprocess

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

@app.route('/<service_url>/<section_name>/<item_name>')
def item_page(service_url, section_name, item_name):
    service = next((s for s in config['top_level_services'] if s['service_url'] == service_url), None)
    if service:
        sections = config.get(service_url, {})
        if section_name in sections:
            items = sections[section_name]
            for item in items:
                if item['item'] == item_name:
                    info_command = item.get('info_command')
                    if info_command:
                        try:
                            # Execute the AWS command and capture its output
                            info_command_output = subprocess.check_output(info_command, shell=True, text=True)
                            return render_template('item_page.html', service=service, section=section_name, item=item_name, output=info_command_output)
                        except subprocess.CalledProcessError as e:
                            return f"Error executing AWS command: {str(e)}"
    return "Service, section, or item not found"

if __name__ == '__main__':
    app.run(debug=True)

