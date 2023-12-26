import sys
import json

args = sys.argv[1]

if len(args) > 0:
    output = args + str(len(args))
    
    # The object Alfred expects, per:
    # https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
    results = {"items": [
        {
            "uid": "gil is dev",
            "type": "file",
            "title": output,
            "subtitle": "ze soup title",
            "arg": output ,
            "autocomplete": "auto complete thisss",
            "icon": {
                "type": "fileicon",
                "path": "~/Desktop"
            }
        }
    ]}
    
    # Alfred takes stdout as input
    print (json.dumps(results))
 