~Simon Krol (https://github.com/simonkrol)

A python side project to provide an easier way of sending Fresh Food Company's bagged meal requests. A first version will be made using the python console to interact with the user, followed by a second version which will use a Tkinter GUI.

Tkinter will be used to create a clickable calendar GUI to quickly allow users to choose the dates they would like bagged meals. The user will be able to choose between breakfast lunch or dinner and may click as many of as few dates as they would like. After submitting, the requestd meal will be ordered for each of the chosen dates.

Python is being used to read and write from a resource file where each user created "meal" will be stored for quick access. (The user creates their meals and may then access them each time they want to required bagged lunches)

The requests API is being used to post the required information to the Fresh Food Company's webpage

The OS library is currently being used to clear the console.

A calendar from svn.python.org is being used as a base for the calendar gui


To do:
Add multiclickable Calendar GUI (DONE)
Add an Info GUI to the Calendar GUI (DONE)
Add a Meal  GUI to the Calendar GUI
Block the requesting of meals that have already been requested
Prevent meals in the past from being ordered
Remove dates stored in the past from dat file?
Condense the stored meal information
Store user meals and retrieve them upon startup to block dates
-Send out email reminders when you need to pick up bagged lunches
(It is currently midterm season so progress may be slower than normal)
Version 1.2