from AlfredWorkflowCreds.AlfredWorkflowCreds import get_creds
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import sys
import json
import re

args = sys.argv[1]

def get_people():
	# TODO: Cache `people`
	creds = get_creds()
	people_service = build("people", "v1", credentials=creds)
	people = people_service.people().connections().list(
				resourceName="people/me",
				pageSize=10,
				personFields="names,emailAddresses",
			).execute()
	return people

def main():
	if len(sys.argv) > 1:
		people = get_people()
		filtered = list(filter(
			lambda connection: re.search(args, json.dumps(connection), re.IGNORECASE),people["connections"]
		))

		to_alfred_results = list(map(lambda connection: {
				"uid": connection["resourceName"],
				"type": "default",
				"title": connection["names"][0]["displayName"],
				"subtitle": connection["emailAddresses"][0]["value"],
				"arg": json.dumps({
					"displayName": connection["names"][0]["displayName"],
					"email": connection["emailAddresses"][0]["value"]
				}),
				"autocomplete": connection["names"][0]["displayName"],
				"icon": {
					"type": "fileicon",
					"path": "~/Desktop"
				}
			}, filtered))

		print (json.dumps({"items": to_alfred_results}))

if __name__ == "__main__":
	main()