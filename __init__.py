from mycroft import MycroftSkill, intent_file_handler


class FocusDepartments(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

#    @intent_file_handler('departments.focus.intent')
#    def handle_departments_focus(self, message):
#        self.speak_dialog('departments.focus')

    @intent_handler(IntentBuilder(" ").require("querry").require("department"))
    def handle_departments_focus(self, message):
        if message.data["department"] == "support":
	    self.speak_dialog('departments.focus')
	elif message.data["department"] == "buvette":
	    self.speak_dialog('cafeteria.focus')

def create_skill():
    return FocusDepartments()

