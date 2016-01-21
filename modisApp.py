#!/usr/bin/python27
import Tkinter as tk
from Tkinter import *
import tkMessageBox as mbox # for popup message boxes
import tkFileDialog as openfile # for Opening Files

L_FONT = ("Verdana", 12)
M_FONT = ("Verdana", 10)
S_FONT = ("Verdana", 8)


class modisApp(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
#MENU BAR
		menubar = tk.Menu(container)

		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label='Exit',command=self.quit)
		menubar.add_cascade(label='File', menu=filemenu)

		helpmenu = tk.Menu(menubar, tearoff=0)
		helpmenu.add_command(label='About',command= lambda: mbox.showerror('About','Nothing yet'))
		menubar.add_cascade(label='Help',menu=helpmenu)

		tk.Tk.config(self, menu=menubar)

		self.frames = {}

		for F in (SplashPage, InputPage, AttributesPage, RenderPage): #add every window class here

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(SplashPage)	#First windo to show - Splash screen

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

class SplashPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)

		label = tk.Label(self, text="WELCOME!", font=L_FONT)
		label.pack(pady=10,padx=10)

		Button = tk.Button(self, text='Next',font=L_FONT, command= lambda: controller.show_frame(InputPage))
		Button.pack(side=BOTTOM, pady=20)

class InputPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)

		def OpenHDF_cp(): #cp  = cloud products
			filein = openfile.askopenfile(filetypes = (("HDF file", "*.hdf"),("All files", "*.*")))
			if(filein != None):			# 'Nonetype' has no .name attribute
				entrybox1.delete(0, END)
				entrybox1.insert(0, filein.name)

		def OpenHDF_cm(): #cm = cloud mask
			filein = openfile.askopenfile(filetypes = (("HDF file", "*.hdf"),("All files", "*.*")))
			if(filein != None):			# 'Nonetype' has no .name attribute
				entrybox2.delete(0, END)
				entrybox2.insert(0, filein.name)

		def OpenHDF_geo(): #geo = geolocation
			filein = openfile.askopenfile(filetypes = (("HDF file", "*.hdf"),("All files", "*.*")))
			if(filein != None):			# 'Nonetype' has no .name attribute
				entrybox3.delete(0, END)
				entrybox3.insert(0, filein.name)

		def Clear(): #clears inputs
			entrybox1.delete(0,END)
			entrybox2.delete(0,END)
			entrybox2.delete(0,END)

#LABELS
		label = tk.Label(self, text="Input", font=L_FONT)
		label.grid(row=0,column=0, pady = 10)

		label1 = tk.Label(self, text="MOD06 Cloud Properties", font=M_FONT)
		label1.grid(row=2,column=0,sticky=W, padx = 5, pady = 5)

		label2 = tk.Label(self, text="MOD35 Cloud Mask", font=M_FONT)
		label2.grid(row=4,column=0,sticky=W, padx = 5, pady = 5)

		label3 = tk.Label(self, text="MOD03 Geolocation", font=M_FONT)
		label3.grid(row=6,column=0,sticky=W, padx = 5, pady = 5)


							#	.grid() layout manager ignores empty rows and columns
							#	left an empty row between the 3 labels for easier adjusting in the future
#TEXT BOXES
		entrybox1 = tk.Entry(self)
		entrybox1.grid(row=2,column=2,padx = 5, pady = 5)

		entrybox2 = tk.Entry(self)
		entrybox2.grid(row=4,column=2, padx = 5, pady = 5)

		entrybox3 = tk.Entry(self)
		entrybox3.grid(row=6,column=2, padx = 5, pady = 5)

#BUTTONS

		button1 = tk.Button(self, text="Browse", command=OpenHDF_cp)
		button1.grid(row=2,column=4, padx = 5, pady = 5)

		button2 = tk.Button(self, text="Browse", command=OpenHDF_cm)
		button2.grid(row=4,column=4, padx = 5, pady = 5)

		button3 = tk.Button(self, text="Browse", command=OpenHDF_geo)
		button3.grid(row=6,column=4, padx = 5, pady = 5)

		checkButton = tk.Button(self, text="Check Attributes", #moves to page one at the moment
							command=lambda: controller.show_frame(AttributesPage)) #lambda overrides run at creation behavior, see examples online
		checkButton.grid(row=8,column=2,sticky=E, padx = 5, pady = 5)

		nextButton = tk.Button(self, text="Next", #moves to page two at the moment
							command=lambda: controller.show_frame(RenderPage))
		nextButton.grid(row=8,column=4, padx = 5, pady = 5)

		clear = tk.Button(self, text="Clear", command=Clear)
		clear.grid(row=8, column=0, padx = 5, pady = 5)


class AttributesPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Attributes", font=L_FONT)
		label.pack(pady=10,padx=10)

		button1 = tk.Button(self, text="Back",
							command=lambda: controller.show_frame(InputPage))
		button1.pack()

		button2 = tk.Button(self, text="Next",
							command=lambda: controller.show_frame(RenderPage))
		button2.pack()


class RenderPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Render Page", font=L_FONT)
		label.pack(pady=10,padx=10)

		button1 = tk.Button(self, text="Back to Home",
							command=lambda: controller.show_frame(InputPage))
		button1.pack()

		button2 = tk.Button(self, text="Page One",
							command=lambda: controller.show_frame(AttributesPage))
		button2.pack()



app = modisApp()
app.mainloop()