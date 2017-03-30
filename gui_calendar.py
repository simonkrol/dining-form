#Created by svn.python.org, modified by Simon Krol
from lunch_methods import open_data
from tkinter import ttk
import calendar
import tkinter
import random
import datetime
import os

def get_calendar(locale, fwday):
	# instantiate proper calendar class
	if locale is None:
		return calendar.TextCalendar(fwday)
	else:
		return calendar.LocaleTextCalendar(fwday, locale)

class Calendar(ttk.Frame):


	datetime = calendar.datetime.datetime
	timedelta = calendar.datetime.timedelta
	canvas={}
	days=[]

	def __init__(self, v, master=None, **kw):
		self.v=v
		"""
		WIDGET-SPECIFIC OPTIONS

			locale, firstweekday, year, month, selectbackground,
			selectforeground
		"""
		# remove custom options from kw before initializating ttk.Frame
		fwday = kw.pop('firstweekday', calendar.MONDAY)
		year = kw.pop('year', self.datetime.now().year)
		month = kw.pop('month', self.datetime.now().month)
		locale = kw.pop('locale', None)
		#generate default canvas background
		self.sel_bg = kw.pop('selectbackground', '#ecffc4')
		self.sel_fg = kw.pop('selectforeground', '#05640e')

		self._date = self.datetime(year, month, 1)
		self._selection = None # no date selected

		ttk.Frame.__init__(self, master, **kw)

		self._cal = get_calendar(locale, fwday)

		self.__setup_styles()	   # creates custom styles
		self.__place_widgets()	  # pack/grid used widgets
		self.__config_calendar()	# adjust calendar columns and setup tags
		# configure a canvas, and proper bindings, for selecting dates
		self.__setup_selection()

		# store items ids, used for insertion later
		self._items = [self._calendar.insert('', 'end', values='')
							for _ in range(6)]
		# insert dates in the currently empty calendar
		self._build_calendar()

		# set the minimal size for the widget
		self._calendar.bind('<Map>', self.__minsize)

		self.canvi=[]
		self._blocks(True)

	def __setup_styles(self):
		# custom ttk styles
		style = ttk.Style(self.master)
		arrow_layout = lambda dir: (
			[('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
		)
		style.layout('L.TButton', arrow_layout('left'))
		style.layout('R.TButton', arrow_layout('right'))

	def __place_widgets(self):
		# header frame and its widgets
		hframe = ttk.Frame(self)
		lbtn = ttk.Button(hframe, style='L.TButton', command=self._prev_month)
		rbtn = ttk.Button(hframe, style='R.TButton', command=self._next_month)
		self._header = ttk.Label(hframe, width=15, anchor='center')
		# the calendar
		self._calendar = ttk.Treeview(show='', selectmode='none', height=7)

		# pack the widgets
		hframe.pack(in_=self, side='top', pady=4, anchor='center')
		lbtn.grid(in_=hframe)
		self._header.grid(in_=hframe, column=1, row=0, padx=12)
		rbtn.grid(in_=hframe, column=2, row=0)
		self._calendar.pack(in_=self, expand=1, fill='both', side='bottom')

	def __config_calendar(self):
		cols = self._cal.formatweekheader(3).split()
		self._calendar['columns'] = cols
		self._calendar.tag_configure('header', background='grey90')
		self._calendar.insert('', 'end', values=cols, tag='header')
		# adjust its columns width
		font = tkinter.font.Font()
		maxwidth = max(font.measure(col) for col in cols)
		for col in cols:
			self._calendar.column(col, width=maxwidth, minwidth=maxwidth,
				anchor='e')

	def __setup_selection(self):
		self._font = tkinter.font.Font()
		self._calendar.bind('<ButtonPress-1>', self._pressed)
	
	def __minsize(self, evt):
		width, height = self._calendar.master.geometry().split('x')
		height = height[:height.index('+')]
		self._calendar.master.minsize(width, height)

	def _build_calendar(self):
		year, month = self._date.year, self._date.month

		# update header text (Month, YEAR)
		header = self._cal.formatmonthname(year, month, 0)
		self._header['text'] = header.title()

		# update calendar shown dates
		cal = self._cal.monthdayscalendar(year, month)
		for indx, item in enumerate(self._items):
			week = cal[indx] if indx < len(cal) else []
			fmt_week = [('%02d' % day) if day else '' for day in week]
			self._calendar.item(item, values=fmt_week)

	def _show_selection(self, text, bbox):
		"""Configure canvas for a new selection."""
		if(self._selection==None):
			return
		#Place a new canvas on the GUI
		self.placecanvas(self._selection[0],True, self.sel_bg, self.sel_fg) 


	
	def placecanvas(self, text, removable, nbackground, textcolour):
		newdate=datetime.date(self._date.year, self._date.month, int(text))	#date to place icon on

		weekday=((newdate.isoweekday())%7)								#get day of week(0-6)
		weeknum=(int((newdate.day-1)/7))									#get which week the day falls on

		if(weekday<(datetime.date(newdate.year, newdate.month, 1)).isoweekday()):	#account for weeks starting on different day
			weeknum+=1																#adding one to the week count if the current day is earlier in the calendar than the first of the month

		x, y, width, height = ((33*weekday)+1,(20*weeknum)+21,33,20)	#generate coordinates

		newcanvas = tkinter.Canvas(self._calendar,
		background=nbackground, borderwidth=0, highlightthickness=0) #Create new canvas

		newcanvas.text = newcanvas.create_text(0, 0, fill=textcolour, anchor='w')	#Set the canvas text
		newcanvas.bind('<ButtonPress-1>', lambda evt: self._unpressed(newcanvas))	#Bind the unpressed method to canvas button press
		
		newcanvas.configure(width=width, height=height)		#Set canvas height and width to the size of date box
		newcanvas.coords(newcanvas.text, width - self._font.measure(text), height / 2 - 1)
		newcanvas.itemconfigure(newcanvas.text, text=text)
		newcanvas.place(in_=self._calendar, x=x, y=y)
		newcanvas.addtag_all("%i/%s/%i" %(newdate.month, text, newdate.year))
		if(removable):	#Add to days list if to be removable
			self.days.append("%i/%s/%i" %(newdate.month, text, newdate.year))
		
		self.canvi.append(newcanvas) #Append the canvas to a list of canvasses to be accessed when removal is required

	#Delete all canvases within self
	def _deletecanvas(self, chosen):
		for i in self.canvi: 	#For each canvas stored on the frame
			i.place_forget()	#Delete the canvas itself
		if(chosen):
			self.days=[]		#Clear the lists storing days to be sent and current canvases
		self.canvi=[]

	def _unpressed(self, canvas):
		tag=canvas.gettags(canvas.text)[0]		#Get the tag appended to the canvas
		if(tag in self.days):				#If in the 'removable' list, remove the tag from the list and delete the canvas on the frame
			self.days.remove(tag)
			canvas.place_forget()

	def _pressed(self, evt):
		"""Clicked somewhere in the calendar."""
		x, y, widget = evt.x, evt.y, evt.widget
		item = widget.identify_row(y)
		column = widget.identify_column(x)

		if not column or not item in self._items:
			# clicked in the weekdays row or just outside the columns
			return

		item_values = widget.item(item)['values']
		if not len(item_values): # row is empty for this month
			return

		text = item_values[int(column[1]) - 1]
		if not text: # date is empty
			return

		bbox = widget.bbox(item, column)
		if not bbox: # calendar not visible yet
			return

		#Update calendar, either removing removing selection or adding a new one
		text = ('%02d' % text)
		if(self._selection == (text, item, column)):
			self._selection=None
		else:
			self._selection = (text, item, column)
		self._show_selection(text, bbox)


	def _prev_month(self):
		
		"""Updated calendar to show the previous month."""

		self._date = self._date - self.timedelta(days=1)
		self._date = self.datetime(self._date.year, self._date.month, 1)
		self._build_calendar() # reconstuct calendar
		self._blocks(True)

	def _next_month(self):
		
		"""Update calendar to show the next month."""

		year, month = self._date.year, self._date.month
		self._date = self._date + self.timedelta(
			days=calendar.monthrange(year, month)[1] + 1)
		self._date = self.datetime(self._date.year, self._date.month, 1)
		self._build_calendar() # reconstruct calendar
		self._blocks(True)


	def _blocks(self, chosen):
		self._deletecanvas(chosen) #Delete all canvases currently on the frame
		remove=[]
		today = datetime.datetime.now()
		if(self._date.year<today.year):
			for i in range(1, calendar.monthrange(self._date.year, self._date.month)[1]+1):
				self.placecanvas(i,False, '#F7BE81', self.sel_fg)
		elif(self._date.year==today.year):
			if(self._date.month<today.month):
				for i in range(1, calendar.monthrange(self._date.year, self._date.month)[1]+1):
					self.placecanvas(i,False, '#F7BE81', self.sel_fg)
			elif(self._date.month==today.month):
				print(today.day)
				for i in range(1, today.day+1):
					print(i)
					self.placecanvas(i,False, '#F7BE81', self.sel_fg)

		meal=int(self.v.get())	#Find the current meal
		infile=open_data('data', 'info.dat', 'r')
		lines=infile.readlines()
		if(len(lines)<5):
			return
		split=lines[2].split()
		infile.close()
		studentNum=split[1]
		infile=open_data('data', 'dates.dat', 'r') #Open the dates file to find meals needing to be blocked
		for line in infile: #Parse file and block meals
			majorsplit=line.split()
			if(majorsplit[2]==studentNum):
				if(int(majorsplit[0])==meal):
					split=majorsplit[1].split('/')
					if(int(split[2])==self._date.year and int(split[0])==self._date.month):
						if(majorsplit[1] in self.days):
							self.days.remove(majorsplit[1])
						self.placecanvas(split[1],False, '#DC143C', self.sel_fg)		#Place a non-removable canvas with colour red
		infile.close()
		if(not chosen):
			for day in self.days:
				split=day.split('/')
				self.placecanvas(split[1], False, self.sel_bg, self.sel_fg) #Place the canvases back on the frame, non-removable because they already exist in self.days
		
		
	def selection(self):
		"""Return a list of strings representing all currently selected days"""
		return self.days

	def get_day(self): #Returns the day that was just selected
		if(self._selection!=None):
			return ("%i/%s/%i" %(self._date.month, self._selection[0], self._date.year))
