from flask import render_template, Blueprint, request, redirect
from models.event_list import events, Event

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/')
def index():
    return render_template('index.jinja', title='My Task List', events=events)

@events_blueprint.route('/event/<event>')
def call_event(index):
    return render_template('event.jinja',title=events[int(index)].name_of_event,event=events[int(index)])

@events_blueprint.route('/form')
def form():
    return render_template('form.jinja', title='My Task List', events=events)

@events_blueprint.route('/', methods=["POST"])
def add_event():
    name_of_event = request.form['name_of_event']
    description = request.form['description']
    number_of_guests = int(request.form['number_of_guests'])
    event_location = request.form['event_location']
    event_date = request.form['event_date']
    event_date = (int(event_date[0:4]),int(event_date[5:7]),int(event_date[8:10]))
    try:
        request.form["recurring"]
        recurring=True
    except KeyError:
        recurring=False
    event=Event(name_of_event,number_of_guests,event_location,description,event_date,recurring)
    if event.name_of_event not in [event.name_of_event for event in events]:
        events.append(event)
    return render_template('index.jinja', title="My Task List", events=events)

@events_blueprint.route('/events/<index>/delete', methods=["POST"])
def remove_event(index):
    print(index,type(index),len(events),[event.name_of_event for event in events])
    del events[int(index)]
    return redirect('/')
