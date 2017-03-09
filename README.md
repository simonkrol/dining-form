~Simon Krol (https://github.com/simonkrol)

A python side project to provide an easier way of sending Fresh Food Company's bagged meal requests. A first version will be made using the python console to interact with the user, followed by a second version which will use a Tkinter GUI.

Tkinter will be used to create a clickable calendar GUI to quickly allow users to choose the dates they would like bagged meals. Each date on the calendary will have three clickable boxes, one for each of breakfast, lunch and dinner. The available saved meals for each part of the day can be cycled through by continuing to click, eventually arriving back at a "no-meal" state.

Python is being used to read and write from a resource file where each user created "meal" will be stored for quick access. (The user creates their meals and may then access them each time they want to required bagged lunches)

The requests API is being used to post the required information to the Fresh Food Company's webpage

The OS library is currently being used to clear the console.


Once the Tkinter GUI is complete and working:
Add a Tkinter Meal Creation GUI to the Calendar GUI
Block the requesting of meals that have already been requested
Condense the stored meal information
Allow for the editing and deleting of meals
Store user info in editable sidebar
Store user meals and retrieve them upon startup to block dates
-Send out email reminders when you need to pick up bagged lunches
(It is currently midterm season so progress may be slower than normal)
Version 1.1