from google.oauth2 import service_account
import googleapiclient.discovery

from events.event_db_controller import EventDBController
from events.event_model import Event, Person


class EventController(object):
    SPREADSHEET_ID = '1lRt-zBiF9nIB-MRnfCYudG9THZahf8rcJfuBBz3Wn0I'
    RANGE_NAME = 'ark!A2:E'

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'w4crew.json'
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
                title = row[0]
                description = row[1]
                date = row[2]
                created_by = row[3]


                person = self.event_db_controller.find_person(created_by)

                print('%s, %s' % (row[0], row[3]))
                print(row)

    def find_person_or_create(self, name):
        person = self.event_db_controller.find_person(name)
        if person is None:
            self.event_db_controller.add_person(name)
            return self.event_db_controller.find_person(name)
        return person


event_controller = EventController()
event_controller.read_sheet()
