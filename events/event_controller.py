from google.oauth2 import service_account
import googleapiclient.discovery

from events.event_db_controller import EventDBController
from events.event_model import Event, Person
from datetime import datetime


class EventController(object):
    SPREADSHEET_ID = '1lRt-zBiF9nIB-MRnfCYudG9THZahf8rcJfuBBz3Wn0I'
    RANGE_NAME = 'ark!A2:E'

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'events/w4crew.json'
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials)

    event_db_controller = EventDBController()

    def read_sheet(self):
        # Call the Sheets API
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                    range=self.RANGE_NAME).execute()
        values = result.get('values', [])

        # Read the output
        if not values:
            print('No data found.')
        else:
            for row in values:
                self.add_event_from_row(row)
                print(row)

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
