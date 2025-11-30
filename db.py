from configparser import ConfigParser
from ddl import request, statements
import zmq
import json
import subprocess

# Configure and connect to ZeroMQ socket
def config_and_connect(socket, endpoint):
    protocol = endpoint["protocol"]
    port = endpoint["port"]
    host = endpoint["host"]
    socket.connect(f"{protocol}://{host}:{port}")

# Return socket endpoint data in a dictionary
def get_endpoint(socket_prefix):
    config = ConfigParser()
    config.read("config.ini") # See config_template.txt for config.ini section names and items
    endpoint = {}
    for section in config.sections():
        tokens = section.split('_')
        # Retrieves config.ini section data according to socket prefix (rep, ddl, or dml)
        section_prefix = tokens[0]
        if socket_prefix == section_prefix:
            for key, value in config.items(section):
                endpoint[key] = value
            break
    return endpoint

# Start microservice server in a subprocess
def start_subprocess(endpoint):
    arguments = []
    cwd = "./" # Set default current working directory in case none provided in .ini
    for key in endpoint:
        tokens = key.split('_')
        prefix = tokens[0]
        # Retrieve subprocess command line arguments and new current working directory
        if prefix == "arg":
            value = endpoint[key]
            arguments.append(value)
        elif prefix == "cwd":
            cwd = endpoint[key]
    subprocess.Popen(arguments, cwd = cwd) # Start microservice in non-blocking subprocess

# Configure and connect to ddl request socket 
endpoint = get_endpoint("ddl")
context = zmq.Context()
socket = context.socket(zmq.REQ)
config_and_connect(socket, endpoint)
# Send request to ddl server
for statement in statements:
    start_subprocess(endpoint)
    request["statement"] = statement
    socket.send_json(request)
    # Await response from server
    json_string = socket.recv()
    response = json.loads(json_string)
    print(f"Response from server: {response}")

# from configparser import ConfigParser
# import sqlite3
#     def get_endpoint():
#         pass
#     def create(path):
#         pass
#     def start_server(server_prefix):
#         pass
#     def insert_data(self):
#         pass
#     def add_data(self):
#         pass
#     def load_data(self):
#         pass
#     def call_data(self):
#         pass
#     def update_data(self):
#         pass
#     def delete_data(self):
#         pass
