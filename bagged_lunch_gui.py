#from tkinter import Tk, Button, ttk #Label
import tkinter as tk
from gui_calendar import Calendar
from other_gui import InfoGUI
import calendar
import requests
import tkinter.font
import sys
import os


class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		#self.keyorder=['input_1.3', 'input_1.6', 'input_2', 'input_3', 'input_4']
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
		

		self.parent.withdraw()
		self.window=InfoGUI(None, self.parent)

	def readInfo(self):
		infile=open_data('data', 'info.dat', 'r')
		self.info={}
		for line in infile:
			split=line.split()
			self.info[split[0]]=split[1]
		infile.close()

	def send_request(self):	
		dates=(self.calendar.selection)
		if(dates==None):
			return
		self.readInfo()
		meal=dict()
		key=self.get_keys()
		date={'input_5': ""}
		payload={**self.info, **meal, **key, **date}

		infile=open_data('data', 'info.dat', 'a')

		for date in dates:
			payload['input_5']= date
			print("Order for: %s" %date)
			infile.write(date)
			infile.write("\n")
		infile.close()


			#r=requests.post(url, data=payload) #Commented out so as not to send a ton of requests while testing
	def get_keys(self):
		return {'is_submit_3':'1', 'gform_submit':'3', 'state_3':'WyJbXSIsImQ0NjBmMzhkZDZiMGJmYmI3NDI2NDA0YTZkNTIxNzhkIl0='}

if __name__ == "__main__":
	root = tk.Tk()
	MainApplication(root).pack(side="top", fill="both", expand=True)
	root.mainloop()


def open_data(dir_loc, file, opentype):
	directory = os.path.dirname(dir_loc)
	if not os.path.exists(directory):
		os.makedirs(directory)
	try:
		open('data/dates.dat', 'x')
	except OSError as e:
		pass
	location=('%s/%s' %(dir_loc, file))
	infile=open(location, opentype)
	return infile
