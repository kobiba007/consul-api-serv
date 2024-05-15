# app.py
import logging
import sys
from flask import Flask
from consul_status import get_consul_status
from consul_summary import get_consul_summary
from consul_members import get_consul_members
from system_info import get_system_info

consulApi = Flask(__name__)


# set logging level to INFO
logging.basicConfig(level=logging.INFO)

# status endpoint
@consulApi.route('/v1/api/consulCluster/status')
def consul_status_route():
    return get_consul_status()

# summary endpoint
@consulApi.route('/v1/api/consulCluster/summary')
def consul_summary_route():
    return get_consul_summary()

# members endpoint
@consulApi.route('/v1/api/consulCluster/members')
def consul_members_route():
    return get_consul_members()

# systemInfo endpoint
@consulApi.route('/v1/api/consulCluster/systemInfo')
def system_info_route():
    return get_system_info()

if __name__ == '__main__':
    consulApi.run(debug=False, host='0.0.0.0')
