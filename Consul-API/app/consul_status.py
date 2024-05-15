# consul_status.py
import os
import requests
import logging
from flask import jsonify

# get the Consul server's IP address from an environment variable
ip_address = os.environ.get('IP_ADDRESS')
consul_url = f'http://{ip_address}:8500'

def get_consul_status():
    try:
        # send a GET request to the Consul API to get status information
        response = requests.get(f'{consul_url}/v1/status/leader')
        if response.status_code == 200:
            return jsonify({"status": 1, "message": "Consul server is running"})
        else:
            return jsonify({"status": 0, "message": "Consul server is down"})

    except Exception as e:
        # if there's an error, log it, and return message
        logging.exception("An error occurred: %s", str(e))
        return jsonify({"error": "An unexpected error occurred. Please check the logs for more details."})