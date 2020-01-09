from mycroft import MycroftSkill, intent_file_handler


class OpenNews(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('news.open.intent')
    def handle_news_open(self, message):
        self.speak_dialog('news.open')


def create_skill():
    return OpenNews()

