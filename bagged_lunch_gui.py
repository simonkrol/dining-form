#from tkinter import Tk, Button, ttk #Label
import tkinter as tk
from gui_calendar import Calendar
from other_gui import InfoGUI
import calendar
import requests
import tkinter.font
import sys

"""Create a calendar within that allows for selection of multiple dates
Find a way to have 3 clickable areas per calendar day to allow for choices between
breakfast, lunch and dinner. Alternate through colours representing seperate meals 
and show meals on sidebar
"""
#url = 'http://dining.carleton.ca/locations/fresh-food-company/' 
# class CalendarGUI(Frame):
# 	def __init__(self):

# 		self.master=Tk()
# 		self.master.title("Calendar GUI")

# 		self.data_set_button = Button(self, text="Set Information", command=self.create_window)
# 		self.data_set_button.pack()

# 		self.submit_button = Button(self, text="Send Requests", command=self.send_request)
# 		self.submit_button.pack()


# 		self.calendar=Calendar(firstweekday=calendar.SUNDAY)
# 		self.calendar.pack(expand=1, fill='both')#I have no idea what either of these do, they work the same without them, leaving them in for now

# 		if 'win' not in sys.platform:	#Checks for the windows operating system, changes style if not
# 			style = ttk.Style()
# 			style.theme_use('clam')
	
# 	def send_request(self):
# 		dates=(self.calendar.selection)
# 		if(dates==None):
# 			return
# 		print(dates)
# 		info=get_info()
# 		meal=get_meal()
# 		key=get_keys()
# 		date={'input_5': ""}
# 		payload={**info, **meal, **key, **date}
# 		for date in dates:
# 			payload['input_5']= date
# 			print("Order for: %s" %date)
# 			#r=requests.post(url, data=payload) #Commented out so as not to send a ton of requests while testing

# 	def create_window(self):
# 		if(self.window!=None):
# 			self.deleteWindow()
# 		self.window=InfoGUI(root)
# 		button=Button(self.window, text="Done", command=self.deleteWindow)
# 	def deleteWindow(self):
# 		self.window.destroy()

# def get_info():
# 	info={}
# 	info['input_1.3']="Test"
# 	info['input_1.6']="Account"
# 	info['input_2']="100000000"
# 	info['input_3']="6131000000"
# 	info['input_4']="redstonewarlock@gmail.com"
# 	return info
# def get_meal():
# 	mealinfo={}
# 	mealinfo['input_14']= "Bagel with cream cheese"
# 	mealinfo['input_20']= ""
# 	mealinfo['input_6']="Breakfast"
# 	mealinfo['input_16']="Apple Juice" 
# 	return mealinfo
# def get_keys():
# 	return {'is_submit_3':'1', 'gform_submit':'3', 'state_3':'WyJbXSIsImQ0NjBmMzhkZDZiMGJmYmI3NDI2NDA0YTZkNTIxNzhkIl0='}
	
# calendar_gui=CalendarGUI()
#root.mainloop()


class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		self.parent.title("Calendar GUI")

		self.data_set_button = tk.Button(self, text="Set Information", command=self.create_window)
		self.data_set_button.pack()

		self.submit_button = tk.Button(self, text="Send Requests", command=self.send_request)
		self.submit_button.pack()


		self.calendar=Calendar(firstweekday=calendar.SUNDAY)
		self.calendar.pack(expand=1, fill='both')#I have no idea what either of these do, they work the same without them, leaving them in for now

		if 'win' not in sys.platform:	#Checks for the windows operating system, changes style if not
			style = ttk.Style()
			style.theme_use('clam')
	def create_window(self):
		values=['Simon', 'Krol', '101047304', '6134021404', 'simonkrol@cmail.carleton.ca']
		self.window=InfoGUI(None, values)
		

	def send_request(self):	
		print(self.window.val1)
		# dates=(self.calendar.selection)
		# if(dates==None):
		# 	return
		# print(dates)
		# info=get_info()
		# meal=get_meal()
		# key=get_keys()
		# date={'input_5': ""}
		# payload={**info, **meal, **key, **date}
		# for date in dates:
		# 	payload['input_5']= date
		# 	print("Order for: %s" %date)
			#r=requests.post(url, data=payload) #Commented out so as not to send a ton of requests while testing


if __name__ == "__main__":
	root = tk.Tk()
	MainApplication(root).pack(side="top", fill="both", expand=True)
	root.mainloop()