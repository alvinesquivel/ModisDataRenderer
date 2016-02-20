#!/usr/bin/python27
import Tkinter as tk
from Tkinter import *
from Tkinter import StringVar
import ttk
import tkMessageBox as mbox # for popup message boxes
import tkFileDialog as openfile # for Opening Files

import numpy as np
from pyhdf.SD import SD, SDC, SDS
import sys

L_FONT = ("Verdana", 12)
M_FONT = ("Verdana", 10)
S_FONT = ("Verdana", 8)

# mod06 = "C:/Users/Mark Steven/Documents/GitHub/ModisDataRenderer/MOD06_L2.A2015348.0215.006.2015348152515.hdf"
# mod35 = "C:\Users\Mark Steven\Documents\GitHub\ModisDataRenderer\MOD35_L2.A2015220.0215.006.2015220134621.hdf"
# mod03 = "C:\Users\Mark Steven\Documents\GitHub\ModisDataRenderer\MOD03.A2015188.0215.006.2015188145151.hdf"
mod06 = ""
mod35 = ""
mod03 = ""

class modisApp(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		tk.Tk.iconbitmap(self,default='clienticon.ico')
		tk.Tk.wm_title(self, "Modis Data Renderer")

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
		helpmenu.add_command(label='Instructions',command= lambda: mbox.showinfo('About','Nothing yet'))
		menubar.add_cascade(label='Help',menu=helpmenu)

		tk.Tk.config(self, menu=menubar)

		self.frames = {}

		for F in (SplashPage, InputPage, AttributesPage, RenderPage): #add every window class here

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="NSEW")

		self.show_frame(SplashPage)	#First window to show - Splash screen

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

class SplashPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text="WELCOME!", font=L_FONT)
		label.pack(pady=10,padx=10)

		Button = ttk.Button(self, text='Next', command= lambda: controller.show_frame(InputPage))
		Button.pack(side=BOTTOM, pady=20)

class InputPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)

#DEFINING METHODS

		def OpenHDF_cp(): #cp  = cloud products
			filein1 = openfile.askopenfile(filetypes = (("HDF file", "*.hdf"),("All files", "*.*")))
			if(filein1 != None):			# 'Nonetype' has no .name attribute
				entrybox1.delete(0, END)
				entrybox1.insert(0, filein1.name)
				mod06 = filein1.name

		def OpenHDF_cm(): #cm = cloud mask
			filein2 = openfile.askopenfile(filetypes = (("HDF file", "*.hdf"),("All files", "*.*")))
			if(filein2 != None):			# 'Nonetype' has no .name attribute
				entrybox2.delete(0, END)
				entrybox2.insert(0, filein2.name)
				mod35 = filein2.name

		def OpenHDF_geo(): #geo = geolocation
			filein3 = openfile.askopenfile(filetypes = (("HDF file", "*.hdf"),("All files", "*.*")))
			if(filein3 != None):			# 'Nonetype' has no .name attribute
				entrybox3.delete(0, END)
				entrybox3.insert(0, filein3.name)
				mod03 = filein3.name

		def Clear(): #clears inputs
			entrybox1.delete(0,END)
			entrybox2.delete(0,END)
			entrybox3.delete(0,END)
			mod06 = ""
			mod35 = ""
			mod03 = ""

#FRAME LAYOUT

		self.grid_columnconfigure(1, weight = 1)
		self.grid_rowconfigure(1, weight = 1)

		topframe = Frame(self)
		topframe.grid(column = 1)
		innerframe = Frame(self)
		innerframe.grid(column = 1, sticky = N+S+E+W, padx = 15)
		bottomframe = Frame(self)
		bottomframe.grid(column = 1, sticky = E, padx = 15)

		innerframe.grid_columnconfigure(2, weight = 1)
		innerframe.grid_rowconfigure(2, weight = 1)
		innerframe.grid_rowconfigure(4, weight = 1)
		innerframe.grid_rowconfigure(6, weight = 1)

#LABELS
		label = ttk.Label(topframe, text="Input", font=L_FONT)
		label.pack(pady = 10)

		label1 = ttk.Label(innerframe, text="MOD06 Cloud Properties", font=M_FONT)
		label1.grid(row=2,column=0, padx = 10, pady = 10)

		label2 = ttk.Label(innerframe, text="MOD35 Cloud Mask", font=M_FONT)
		label2.grid(row=4,column=0,padx = 10, pady = 10)

		label3 = ttk.Label(innerframe, text="MOD03 Geolocation", font=M_FONT)
		label3.grid(row=6,column=0,padx = 10, pady = 10)

#TEXT BOXES
		entrybox1 = ttk.Entry(innerframe)
		entrybox1.grid(row=2,column=2, padx = 10, pady = 10, sticky = EW)

		entrybox2 = ttk.Entry(innerframe)
		entrybox2.grid(row=4,column=2, padx = 10, pady = 10, sticky = EW)

		entrybox3 = ttk.Entry(innerframe)
		entrybox3.grid(row=6,column=2, padx = 10, pady = 10, sticky = EW)

#BUTTONS

		button1 = ttk.Button(innerframe, text="Browse", command=OpenHDF_cp)
		button1.grid(row=2,column=4, padx = 10, pady = 10)

		button2 = ttk.Button(innerframe, text="Browse", command=OpenHDF_cm)
		button2.grid(row=4,column=4, padx = 10, pady = 10)

		button3 = ttk.Button(innerframe, text="Browse", command=OpenHDF_geo)
		button3.grid(row=6,column=4, padx = 10, pady = 10)

		button4 = ttk.Button(bottomframe, text="Clear", command=Clear)
		button4.grid(column = 1, row = 0,padx = 10, pady = 10)

		button5 = ttk.Button(bottomframe, text="Check Attributes",
							command=lambda: controller.show_frame(AttributesPage))
		button5.grid(column = 2, row = 0,padx = 10, pady = 10)

		button6 = ttk.Button(bottomframe, text="Render",
							command=lambda: controller.show_frame(RenderPage))
		button6.grid(column = 3, row = 0, padx = 10, pady = 10)




class AttributesPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

# FRAME LAYOUTS

		self.grid_columnconfigure(1, weight = 1)
		self.grid_rowconfigure(1, weight = 1)

		frame0 = Frame(self)
		frame0.grid(columnspan = 2)
		frame1 = Frame(self)
		frame1.grid(column = 0, sticky = N)
		frame2 = Frame(self)
		frame2.grid(row = 1, column = 1, sticky = N+W)
		frame3 = Frame(self)
		frame3.grid(columnspan = 2, sticky = E)
		frame4 = Frame(frame2)
		frame4.grid(row = 1)
		frame4.grid_propagate(False)

		frame5 = Frame(frame1)
		frame5.grid(row = 0, column = 0)
		frame6 = Frame(frame1)
		frame6.grid(row = 0, column = 1)
		frame2.grid_columnconfigure(0, weight = 1)
# LABELS

		label0 = ttk.Label(frame0, text = "Attributes", font = L_FONT).pack(padx = 10, pady = 10)
		label1 = ttk.Label(frame5, text = "Products", font = M_FONT).pack(padx = 10, pady = 10)
		label2 = ttk.Label(frame6, text = "Scientific Data Sets", font = M_FONT).grid(row = 0, columnspan = 2)
		label3 = ttk.Label(frame2, text = "Metadata", font = M_FONT).grid(row = 0, padx = 10, pady = 10)

# BUTTONS

		button0 = ttk.Button(frame3, text = "Render", command = lambda: controller.show_frame(RenderPage)).pack(side = RIGHT, padx = 10, pady = 10)
		button1 = ttk.Button(frame3, text = "Show Values").pack(side = RIGHT, padx = 10, pady = 10)
		button2 = ttk.Button(frame3, text = "Back", command = lambda: controller.show_frame(InputPage)).pack(side = RIGHT, padx = 10, pady = 10)

# Test Buttons
		button3 = ttk.Button(frame3, text = "Insert Text", command = lambda: textbox0.insert(INSERT, "This is a line of text. "))
		button3.pack(side = RIGHT, padx = 10, pady = 10)
		button4 = ttk.Button(frame3, text = "Delete Text", command = lambda: textbox0.delete(1.0, END))
		button4.pack(side = RIGHT, padx = 10, pady = 10)
		button5 = ttk.Button(frame3, text = "Delete Character?", command = lambda: textbox0.delete(1.0))
		button5.pack(side = RIGHT, padx = 10, pady = 10)


# LISTBOXES

		self.listbox0 = tk.Listbox(frame5, font = M_FONT)
		self.listbox0.pack(padx = 10, pady = 10, fill = BOTH)

		for item in ["Cloud Mask", "Cloud Products", "Geolocation"]:
			self.listbox0.insert(END, item)

		self.listbox0.bind("<<ListboxSelect>>", self.show_sds)

		scrollbar0 = ttk.Scrollbar(frame6, orient = "vertical")
		scrollbar1 = ttk.Scrollbar(frame6, orient = "horizontal")

		self.listbox1 = tk.Listbox(frame6, width = 25, height = 25, font = M_FONT, yscrollcommand = scrollbar0.set, xscrollcommand = scrollbar1.set)
		self.listbox1.grid(pady = 10, row = 1, column = 0)

		scrollbar0.config(command = self.listbox1.yview)
		scrollbar0.grid(column = 1, row = 1, sticky = N+S)
		scrollbar1.config(command = self.listbox1.xview)
		scrollbar1.grid(row = 2, columnspan = 2, sticky = E+W)

# TEXT BOX

		textbox0 = tk.Text(frame4, font = L_FONT)
		textbox0.pack(fill = BOTH, expand = True, padx = 10, pady = 10)
		textbox0.config(state = NORMAL)

	def show_sds(self, event):
		widget = event.widget
		selection=widget.curselection()
		value = widget.get(selection)
		if(value == 'Cloud Mask'):
			_file = mod35
			read = SD(_file, SDC.READ)
			datasets = read.datasets()
			datasets_list = datasets.keys()
		elif(value == 'Cloud Products'):
			_file = mod06
			read = SD(_file, SDC.READ)
			datasets = read.datasets()
			datasets_list = datasets.keys()
		elif(value == 'Geolocation'):
			_file = mod03
			read = SD(_file, SDC.READ)
			datasets = read.datasets()
			datasets_list = datasets.keys()


		self.listbox1.delete(0, END)

		for i in range(len(datasets_list)):
			self.listbox1.insert(END, datasets_list[i])
		read.end()



class RenderPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text="Render Page", font=L_FONT)
		label.pack()

		button1 = ttk.Button(self, text="Back",command=lambda: controller.show_frame(InputPage))
		button1.pack()

		button2 = ttk.Button(self, text="Attributes",command=lambda: controller.show_frame(AttributesPage))
		button2.pack()



app = modisApp()
app.geometry('800x600')
app.mainloop()