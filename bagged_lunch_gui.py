from tkinter import Tk, Button, ttk #Label
from gui_calendar import Calendar
import calendar
import requests
#import tkinter
import tkinter.font
import sys

"""Create a calendar within that allows for selection of multiple dates
Find a way to have 3 clickable areas per calendar day to allow for choices between
breakfast, lunch and dinner. Alternate through colours representing seperate meals 
and show meals on sidebar
"""
url = 'http://dining.carleton.ca/locations/fresh-food-company/' 
class CalendarGUI:
	def __init__(self, master):
		self.master=master
		master.title("Calendar GUI")



		self.submit_button = Button(master, text="Send Requests(Breakfast)", command=self.send_request)
		self.submit_button.pack()


		self.calendar=Calendar(firstweekday=calendar.SUNDAY)
		self.calendar.pack(expand=1, fill='both')#I have no idea what either of these do, they work the same without them, leaving them in for now

		if 'win' not in sys.platform:	#Checks for the windows operating system, changes style if not
			style = ttk.Style()
			style.theme_use('clam')

	
	def send_request(self):
		dates=(self.calendar.selection)
		if(dates==None):
			return
		print(dates)
		info=get_info()
		meal=get_meal()
		key=get_keys()
		date={'input_5': ""}
		payload={**info, **meal, **key, **date}
		for date in dates:
			payload['input_5']= date
			print("Order for: %s" %date)
			#r=requests.post(url, data=payload) #Commented out so as not to send a ton of requests




def get_info():
	info={}
	info['input_1.3']="Test"
	info['input_1.6']="Account"
	info['input_2']="100000000"
	info['input_3']="6131000000"
	info['input_4']="redstonewarlock@gmail.com"
	return info
def get_meal():
	mealinfo={}
	mealinfo['input_14']= "Bagel with cream cheese"
	mealinfo['input_20']= ""
	mealinfo['input_6']="Breakfast"
	mealinfo['input_16']="Apple Juice" 
	return mealinfo
def get_keys():
	return {'is_submit_3':'1', 'gform_submit':'3', 'state_3':'WyJbXSIsImQ0NjBmMzhkZDZiMGJmYmI3NDI2NDA0YTZkNTIxNzhkIl0='}
	
root= Tk()
calendar_gui=CalendarGUI(root)
root.mainloop()