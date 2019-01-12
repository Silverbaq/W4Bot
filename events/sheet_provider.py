from google.oauth2 import service_account
import googleapiclient.discovery

from events.event_db_controller import EventDBController


class SheetProvider(object):
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
        output = []
        if not values:
            print('No data found.')
        else:
            for row in values:
                output.append(row)
        return output