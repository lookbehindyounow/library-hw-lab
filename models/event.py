import datetime

class Event():

    def __init__(self, name_of_event,number_of_guests, event_location,description,date,recurring=False):
        self.name_of_event = name_of_event
        self.description = description
        self.number_of_guests = number_of_guests
        self.event_location = event_location
        self.day = datetime.date(date[0],date[1],date[2])
        self.recurring=recurring
