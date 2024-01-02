#!/usr/bin/env python3
from flask import Flask, render_template
import json
import subprocess
from json2html import json2html

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
        return render_template('service_page.html', service=service, sections=sections)
    return "Service not found"

def execute_info_command(info_command):
    try:
        # Execute the AWS command and capture its output as a string
        info_command_output = subprocess.check_output(info_command, shell=True, text=True)
        return info_command_output
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Error executing AWS command: {str(e)}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON data: {str(e)}")

def get_item_info(service_url, section_name, item_name):
    service = next((s for s in config['top_level_services'] if s['service_url'] == service_url), None)
    if service:
        sections = config.get(service_url, {})
        if section_name in sections:
            items = sections[section_name]
            for item in items:
                if item['item'] == item_name:
                    return item
    return None

def item_page(service_url, section_name, item_name):
    item = get_item_info(service_url, section_name, item_name)
    if item:
        info_command = item.get('info_command')
        if info_command:
            try:
                info_command_output = execute_info_command(info_command)
                if not info_command_output.strip():
                    return "No data available."

                # Convert the JSON data to an HTML table
                json_data = json.loads(info_command_output)
                table_html = json2html.convert(json=json_data)

                return render_template('item_page.html', service=service, section=section_name, item=item_name, table_html=table_html)
            except ValueError as e:
                return str(e)
    return "Service or section not found"

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8443)

