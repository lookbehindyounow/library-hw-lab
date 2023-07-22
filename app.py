from flask import Flask, Blueprint, request
from controllers.events_controller import events_blueprint

app = Flask(__name__)
app.register_blueprint(events_blueprint)