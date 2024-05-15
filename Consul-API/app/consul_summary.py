# consul_summary.py
import os
import requests
import logging
from flask import jsonify

# get the Consul server's IP address from an environment variable
ip_address = os.environ.get('IP_ADDRESS')
consul_url = f'http://{ip_address}:8500'

def get_consul_summary():
    try:
        #  number of registered nodes
        nodes_response = requests.get(f"{consul_url}/v1/catalog/nodes")
        nodes = nodes_response.json()
        registered_nodes = len(nodes)
        
        #  number of registered services
        services_response = requests.get(f"{consul_url}/v1/catalog/services")
        services = services_response.json()
        registered_services = len(services)
        
        #  leader IP and port
        leader_response = requests.get(f"{consul_url}/v1/status/leader")
        leader_ip_port = leader_response.text.strip('\"')  # remove \" from the output 
        
        #  internal protocol version (number of peers)
        peers_response = requests.get(f"{consul_url}/v1/status/peers")
        cluster_protocol = len(peers_response.json())
        
        # create summary data
        summary_data = {
            "registered_nodes": registered_nodes,
            "registered_services": registered_services,
            "leader": leader_ip_port,
            "cluster_protocol": cluster_protocol
        }
        
        return jsonify(summary_data)
    except Exception as e:
        # if there's an error, log it, and return message
        logging.exception("An error occurred: %s", str(e))
        return jsonify({"error": "An unexpected error occurred. Please check the logs for more details."})