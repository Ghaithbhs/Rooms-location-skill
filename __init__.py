from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.log import LOG


class FocusDepartments(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

#    @intent_file_handler('departments.focus.intent')
#    def handle_departments_focus(self, message):
#        self.speak_dialog('departments.focus')

    @intent_handler(IntentBuilder(" ").require("department"))
    def handle_departments_focus(self, message):
        if message.data["department"] == "Ghaith":
	    self.speak_dialog('departments.focus')
	elif message.data["department"] == "buvette":
	    self.speak_dialog('cafeteria.focus')

def create_skill():
    return FocusDepartments()

