import tkinter as tk


class InfoGUI(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.master.title("test")
		self.pack()

		



		self.__entryPane = tk.Frame(self)
		self.__entryPane.pack()


		self.fname=tk.Entry(self.__entryPane)
		self.fname.pack()

		self.lname=tk.Entry(self.__entryPane)
		self.lname.pack()

		self.sn=tk.Entry(self.__entryPane)
		self.sn.pack()

		self.pn=tk.Entry(self.__entryPane)
		self.pn.pack()

		self.email=tk.Entry(self.__entryPane)
		self.email.pack()


		self.__buttonA1 = tk.Button(self.__entryPane,text = "Done",command = self._close)
		self.__buttonA1.pack()

	def _close(self):
		self.destroy()

