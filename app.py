from flask import Flask, jsonify, render_template, request
import os, optparse
import json

app = Flask(__name__)
app.static_folder = 'templates'
developer = os.getenv("DEVELOPER", "Me")
environment = os.getenv("ENVIRONMENT", "development")


@app.route('/')
def hello_world():
    return render_template('cards.html')


if __name__ == "__main__":
    debug = False
    if environment == "development" or environment == "local":
        debug = True
    app.run(host="0.0.0.0", debug=debug)
