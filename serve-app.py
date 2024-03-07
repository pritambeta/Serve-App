from flask import Flask, send_from_directory
from webbrowser import open
import os
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("path", nargs="?", default=os.getcwd(), help="Path of the app")
parser.add_argument("--port", default=1668, type=int, help="Port to run")
args = parser.parse_args()

app_folder = args.path
port = args.port
if not port:
    print("Port not defined")
    sys.exit()

if port < 1000 or port > 65535:
    print("Port must be between 1024 and 65535")
    sys.exit()


app = Flask(__name__, static_folder='*')

def serve_index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app_folder, path)):
        return send_from_directory(app_folder, path)
    else:
        return send_from_directory(app_folder, 'index.html')

if __name__ == '__main__':
    open(f'http://localhost:{port}/')
    app.run(port=port, host="0.0.0.0")
