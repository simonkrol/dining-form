# CuDining

An easier way to send Fresh Food Company's bagged meal requests.

### Technology
- Python
- Tkinter

Includes a clickable calendar GUI which allows users to choose dates to post bagged meal requests to the Fresh Food Company. Original non-clickable calendar from metulburr on python-forum.io.

### Options
- choose between breakfast, lunch or dinner 
- select multiple dates
- store meal preferences and user info

### To do
* Add multiclickable Calendar GUI (DONE)
* Add an Info GUI to the Calendar GUI (DONE)
* Add a Meal  GUI to the Calendar GUI (DONE)
* Block the requesting of meals that have already been requested (DONE)
* Make meal blocking user specific, based on student number (DONE)
* Add special request capability (DONE)
* Prevent meals in the past from being ordered(DONE)
* Remove dates stored in the past from dat file? (DONE)
* **Condense the stored meal information**
* Store user meals and retrieve them upon startup to block dates (DONE)
* **Send out email reminders when you need to pick up bagged lunches(Would need some sort of server)**
* Exit all frames upon any window close (DONE)
* Add warning label to indicate what needs to be done, ie: info needs to be filled..etc (DONE)
* Don't remove chosen dates when switching between meals and student numbers (DONE)
>Version 1.6

### Setup
- Download or clone the repository
- Make sure `pip` and Python 3 are installed
- Install the requests library
```
$ pip install requests
```
- Run
```
python bagged_lunch_gui.py
```
