in alfred, create a new custom workflow.

open the custom workflow folder in terminal (do to so, right click on the custom workflow name in alfted. then choose "open in terminal")

clone this git repo into the newly created folder

do prereqs https://developers.google.com/calendar/api/quickstart/python

install python dependencies locally into the alfred's custom workflow folder (with `--target .`) by typing:
```
pip3 install --target . --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

[Enable google APIs](https://console.cloud.google.com/apis/library): people, calendar


_______

```
             Script Filter                                               Script Filter
python3 ./AlfredAutoCompleteContacts.py "{query}"    -->    python3 ./AlfredScheduleEvent.py "{query}"
           (input as {query})                                           (input as {query})
```
