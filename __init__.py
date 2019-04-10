from mycroft import MycroftSkill, intent_file_handler


class FocusDepartments(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('departments.focus.intent')
    def handle_departments_focus(self, message):
	if message.data =="where is the it":
            self.speak_dialog('departments.focus')
	else: 
	    self.speak_dialog('cafeteria.focus')

#    @intent_handler(IntentBuilder().require("question"))
#    def handle_departments_focus(self, message):
#	if message.data["question"] == "where is the I T" :
#	    self.speak_dialog('departments.focus')
#	else if message.data["question"] == "where is the cafeteria" :
#	    self.speak_dialog('cafeteria.focus')

def create_skill():
    return FocusDepartments()

