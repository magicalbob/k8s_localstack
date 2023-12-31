#!/usr/bin/env python3
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
import json
import subprocess
from json2html import json2html

app = Flask(__name__)

# Initialize CSRF protection
csrf = CSRFProtect(app)

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
        return render_template('service_page.html', service=service, sections=sections)
    return "Service not found"

@app.route('/<service_url>/<section_name>/<item_name>')
def item_page(service_url, section_name, item_name):
    service = next((s for s in config['top_level_services'] if s['service_url'] == service_url), None)
    if service:
        sections = config.get(service_url, {})
        if section_name in sections:
            items = sections[section_name]
            for item in items:
                result = process_item(service, item, section_name, item_name)
                if result is not None:
                    return result
    return "Service or section not found"

def process_item(service, item, section_name, item_name):
    if item['item'] == item_name:
        info_command = item.get('info_command')
        if info_command:
            try:
                # Execute the AWS command and capture its output as a string
                info_command_output = subprocess.check_output(info_command, shell=True, text=True)

                # Check if the output is empty or not
                if not info_command_output.strip():
                    print("DEBUG 5")
                    return "No data available."

                # Convert the JSON data to an HTML table
                json_data = json.loads(info_command_output)
                table_html = json2html.convert(json=json_data)

                return render_template('item_page.html', service=service, section=section_name, item=item_name, table_html=table_html)
            except subprocess.CalledProcessError as e:
                return f"Error executing AWS command: {str(e)}"
            except json.JSONDecodeError as e:
                return f"Error decoding JSON data: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8443)
