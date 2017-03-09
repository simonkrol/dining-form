from tkinter import Tk, Button, ttk #Label
from gui_calendar import Calendar
import calendar
#import tkinter
import tkinter.font
import sys

"""Create a calendar within that allows for selection of multiple dates
Find a way to have 3 clickable areas per calendar day to allow for choices between
breakfast, lunch and dinner. Alternate through colours representing seperate meals 
and show meals on sidebar
"""

class CalendarGUI:
	def __init__(self, master):
		self.master=master
		master.title("Calendar GUI")



		self.submit_button = Button(master, text="Send Requests", command=self.get_date)
		self.submit_button.pack()


		self.calendar=Calendar(firstweekday=calendar.SUNDAY)
		self.calendar.pack(expand=1, fill='both')#I have no idea what either of these do, they work the same without them, leaving them in for now

		if 'win' not in sys.platform:	#Checks for the windows operating system, changes style if not
			style = ttk.Style()
			style.theme_use('clam')

	def send(self):
		print("Requests sent")
	def get_date(self):
		print(self.calendar.selection)
root= Tk()
calendar_gui=CalendarGUI(root)
root.mainloop()