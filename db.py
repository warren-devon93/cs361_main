from configparser import ConfigParser
from ddl import creates
from dml import units, inserts, updates, selects, delete
import zmq, json, subprocess, os

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

def get_db_path():
    data = get_endpoint("main")
    path_to_cwd = data["path"]
    db_filename = "recipes"
    db_filepath = path_to_cwd + db_filename
    return db_filepath

def send_request(socket, request):
    socket.send_json(request)
    # Await response from server
    json_string = socket.recv()
    response = json.loads(json_string)
    print(f"Response from server: {response}")
    return response

def parse_statement(data, string):
    statement = ""
    tokens = string.split('?')
    i = 0
    for column in data:
        statement = tokens[i] + column
        i += 1
    statement += tokens[i]
    # TODO: Test print
    print(statement)
    return statement

def insert_units(request):
    endpoint = get_endpoint("dml")
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    config_and_connect(socket, endpoint)
    command = inserts["unit"] # See dml.py
    for unit in units: # ibid
        start_subprocess(endpoint)
        request["statement"] = parse_statement([unit], command)
        send_request(socket, request)

def setup_database(request):
    endpoint = get_endpoint("ddl")
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    config_and_connect(socket, endpoint)
    request["db_path"] = get_db_path()
    for statement in creates:
        start_subprocess(endpoint)
        request["statement"] = statement
        send_request(socket, request)
    insert_units(request)

# TODO: Initialize request object and create recipes database if none exists 
request = {"db_path": "", "statement": ""}
if os.path.isfile('recipes.db') is False: setup_database(request)
# TODO: Insert test data into all tables

# TODO: Query test data

# TODO: Update test data

# TODO: Query test data

# TODO: Delete test data

# TODO: Query test data
