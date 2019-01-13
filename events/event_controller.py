from datetime import datetime
from events.sheet_provider import SheetProvider
from events.event_model import Event, Person
from events.event_db_controller import EventDBController


class EventController(object):
    event_db_controller = EventDBController()
    sheet_provider = SheetProvider()

    def add_event_from_row(self, row):
        title = row[0]
        description = row[1]
        date = datetime.strptime(row[2], '%d-%m-%Y')
        created_by = row[3]

        person = self.find_person_or_create(created_by)
        self.event_db_controller.add_event(title, description, date, person)

    def find_person_or_create(self, name):
        person = self.event_db_controller.find_person(name)
        if person is None:
            self.event_db_controller.add_person(name)
            return self.event_db_controller.find_person(name)
        return person

    def get_all_events(self):
        return self.event_db_controller.get_all_events()

    def get_event(self, title):
        return self.event_db_controller.find_event(title)


    def add_sheet_to_db(self):
        rows = self.sheet_provider.read_sheet()
        for row in rows:
            if not self.event_db_controller.is_event_pressent(row[0]):
               self.add_event_from_row(row)

    def like_event(self, title):
        return self.event_db_controller.like_event(title)

    def sign_up_for_event(self, title, name):
        return self.event_db_controller.signup_for_event(title, name)