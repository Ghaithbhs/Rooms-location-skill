from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.log import LOG


class RoomsLocation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder("").require("querry").require("Room"))
    def handle_departments_focus(self, message):
        if message.data["Room"] == "bathroom":
            self.speak_dialog('bathroom.location')
        elif message.data["Room"] == "bedroom":
            self.speak_dialog('Bedroom.location')

def create_skill():
    return RoomsLocation()
