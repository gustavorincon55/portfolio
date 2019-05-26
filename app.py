import csv
import json
from flask import Flask, jsonify, redirect, render_template, request
import os
# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
temp_projectsJSON = os.path.join(THIS_FOLDER, 'templates/projects.json')

with open(temp_projectsJSON) as x:
    projects = json.loads(x.read())

@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    path = os.getcwd()
    return render_template("main.html", projects=projects["projects"], path=path)

if __name__ == '__main__':
    app.run(debug=True)