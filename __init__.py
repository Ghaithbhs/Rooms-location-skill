from mycroft import MycroftSkill, intent_file_handler


class FocusDepartments(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('departments.focus.intent')
    def handle_departments_focus(self, message):
        self.speak_dialog('departments.focus')


def create_skill():
    return FocusDepartments()

