in alfred, create a new custom workflow.

open the custom workflow folder in terminal (do to so, right click on the custom workflow name in alfted. then choose "open in terminal")

do prereqs https://developers.google.com/calendar/api/quickstart/python

install locally into the alfred's customm workflow folder (with `--target .`)
```
pip install --target . --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

enable APIs: people, calendar


_______

```
          Script Filter                                         Script Filter
python3 ./AlfredScheduleEvent.py "{query}"   -->   python3 ./AlfredScheduleEvent.py "{query}"
       (input as {query})                                    (input as {query})
```
