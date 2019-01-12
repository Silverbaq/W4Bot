from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

from events.event_model import Event, Base, Person


class EventDBController(object):
    engine = create_engine('sqlite:///events/events.db')
    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    # A DBSession() instance establishes all conversations with the database
    # and represents a "staging zone" for all the objects loaded into the
    # database session object. Any change made against the objects in the
    # session won't be persisted into the database until you call
    # session.commit(). If you're not happy about the changes, you can
    # revert all of them back to the last commit by calling
    # session.rollback()
    session = DBSession()

    def insert(self):
        # Insert a Person in the person table
        new_person = Person(name='new person')
        self.session.add(new_person)
        self.session.commit()

        # Insert an Address in the address table
        new_event = Event(title="new event", created_by=new_person, description="something",
                          date=datetime.datetime.now())
        self.session.add(new_event)
        self.session.commit()

    def read_all(self):
        persons = self.session.query(Person).all()
        for person in persons:
            print('Id: {0}, Name: {1}'.format(person.id, person.name))

        events = self.session.query(Event).all()
        for event in events:
            print('Title: {0}, Date: {1}, Created by: {2}'.format(event.title, event.date, event.created_by))

    def find_person(self, name):
        person = self.session.query(Person).filter_by(name=name).first()
        return person

    def add_person(self, name):
        new_person = Person(name=name)
        self.session.add(new_person)
        self.session.commit()

    def add_event(self, title, description, date, person):
        new_event = Event(title=title, created_by=person, description=description, date=date)
        self.session.add(new_event)
        self.session.commit()

    def get_all_events(self):
        events = self.session.query(Event).all()
        return events

    def is_event_pressent(self, title):
        event = self.session.query(Event).filter_by(title=title).first()
        return event is not None