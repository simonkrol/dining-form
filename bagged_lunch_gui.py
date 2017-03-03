from tkinter import Tk, Label, Button
import time
import calendar

    #Creates Tkinter
"""Create a calendar within that allows for selection of multiple dates
Find a way to have 3 clickable areas per calendar day to allow for choices between
breakfast, lunch and dinner. Alternate through colours representing seperate meals 
and show meals on sidebar
"""

class CalendarGUI:
	def __init__(self, master):
		self.master=master
		master.title("Calendar GUI")

		self.label = Label(master, text="Basic GUI testing")
		self.label.pack()

		self.submit_button = Button(master, text="Send Requests", command=self.send)
		self.submit_button.pack()

		self.end_button = Button(master, text="Close", command=master.quit)
		self.end_button.pack()
		
		cal=calendar.month(int(time.strftime("%Y")), int(time.strftime("%m")))
		self.callabel=Label(master, text=cal, font=('courier', 14, 'bold'), bg='blue')
		self.callabel.pack()


	def send(self):
		print("Requests sent")
root= Tk()
calendar_gui=CalendarGUI(root)
root.mainloop()

# supply year and month
#year = 2017
#month = 2    # jan=1
# assign the month's calendar to a multiline string
#str1 = calendar.month(year, month)
# create the window form and call it root (typical)
#top = tkinter.Tk()
#top.title("Meal Choice")

# pick a fixed font like courier so spaces behave right 
#label1 = tkinter.Label(top, text=str1, font=('courier', 14, 'bold'), bg='yellow')
#label1.pack(padx=3, pady=5)
# run the event loop (needed)

#top.mainloop()  #Opens the gui