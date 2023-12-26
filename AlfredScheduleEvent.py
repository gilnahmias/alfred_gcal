import sys
import json
from AlfredWorkflowCreds.AlfredWorkflowCreds import get_creds
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

args = sys.argv[1]

def main():
  creds = get_creds()

  attendee = json.loads(args)

  try:
    service = build("calendar", "v3", credentials=creds)

    event = {
		"summary": "Meeting with " + attendee["displayName"],
		"location": "Some place over the rainbow",
		"description": "Created by Alfred",
		"start": {
			"dateTime": "2024-01-02T09:00:00-07:00",
			"timeZone": "America/Los_Angeles",
		},
		"end": {
			"dateTime": "2024-01-02T17:00:00-07:00",
			"timeZone": "America/Los_Angeles",
		},
		"attendees": [
			{
				"displayName": attendee["displayName"],
				"email": attendee["email"]
			},
		]
	}

    event = service.events().insert(calendarId="primary", body=event).execute()

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()