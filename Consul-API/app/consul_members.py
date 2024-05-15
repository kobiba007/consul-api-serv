# consul_members.py
import os
import requests
from flask import jsonify
import logging

# get the Consul server's IP address from an environment variable
ip_address = os.environ.get('IP_ADDRESS')

# consul API address
consul_url = f'http://{ip_address}:8500'

# a function to get Consul nodes
def get_consul_members():
    try:
        # send a GET request to the Consul API to get member information
        response = requests.get(f'{consul_url}/v1/agent/members')

        # member names
        members = []
        for member in response.json():
            members.append(member['Name'])

        # return list of member names
        return jsonify({"registered_nodes": members})

    except Exception as e:
        # if there's an error, log it, and return message
        logging.exception("An error occurred: %s", str(e))
        return jsonify({"error": "An unexpected error occurred. Please check the logs for more details."})