#Numpy License
"""
Numpy is licensed under the BSD license, enabling reuse with few restrictions.

Copyright (c) 2005 - 2013, NumPy Developers.
All rights reserved.

Redistribution and use in source and binary in forms, with or without modification,
are permitted provided that the following conditions are met:

	1. Redistribution of source code must retain the above copyright notice,
	this list of conditions and the following disclaimer.

	2. Redistributions in binary form must reproduce the above copyright notice,
	this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

	3. Neither the name of the NumPy Developers nor the names of any contributors
	may be used to endorse or promote products derived from this software without specific prior written permission.

	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS AS IS AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING,
	BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
	SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
	DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
	HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
	ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""

#Python-hdf4 License
"""
The MIT License (MIT)

Copyright (c) 2014 The Python-HDF4 Authors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

#Matplotlib License
"""
License

Matplotlib only uses BSD compatible code, and its license is based on the PSF license.
See the Open Source Initiative licenses page for details on individual licenses.
Non-BSD compatible licenses (e.g., LGPL) are acceptable in matplotlib toolkits.
For a discussion of the motivations behind the licencing choice, see Licenses.

Copyright Policy

John Hunter began matplotlib around 2003. Since shortly before his passing in 2012,
Michael Droettboom has been the lead maintainer of matplotlib, but, as has always been the case,
matplotlib is the work of many.

Prior to July of 2013, and the 1.3.0 release, the copyright of the source code was held by John Hunter.
As of July 2013, and the 1.3.0 release, matplotlib has moved to a shared copyright model.
matplotlib uses a shared copyright model. Each contributor maintains copyright over their contributions to matplotlib.
But, it is important to note that these contributions are typically only changes to the repositories.
Thus, the matplotlib source code, in its entirety, is not the copyright of any single person or institution.
Instead, it is the collective copyright of the entire matplotlib Development Team.
If individual contributors want to maintain a record of what changes/contributions they have specific copyright on,
they should indicate their copyright in the commit message of the change, when they commit the change to one of the matplotlib repositories.

The Matplotlib Development Team is the set of all contributors to the matplotlib project. A full list can be obtained from the git version control logs.


License agreement for matplotlib 1.5.1

1. This LICENSE AGREEMENT is between the Matplotlib Development Team ("MDT"), and the Individual or Organization ("Licensee")
accessing and otherwise using matplotlib software in source or binary form and its associated documentation.

2. Subject to the terms and conditions of this License Agreement, MDT hereby grants Licensee a nonexclusive, royalty-free,
world-wide license to reproduce, analyze, test, perform and/or display publicly, prepare derivative works, distribute,
and otherwise use matplotlib 1.5.1 alone or in any derivative version, provided, however, that MDT's License Agreement and
MDT's notice of copyright, i.e., "Copyright (c) 2012-2013 Matplotlib Development Team; All Rights Reserved" are retained in
matplotlib 1.5.1 alone or in any derivative version prepared by Licensee.

3. In the event Licensee prepares a derivative work that is based on or incorporates matplotlib 1.5.1 or any part thereof,
and wants to make the derivative work available to others as provided herein, then Licensee hereby agrees to include in any such work a
brief summary of the changes made to matplotlib 1.5.1.

4. MDT is making matplotlib 1.5.1 available to Licensee on an "AS IS" basis. MDT MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED.
BY WAY OF EXAMPLE, BUT NOT LIMITATION, MDT MAKES NO AND DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY
PARTICULAR PURPOSE OR THAT THE USE OF MATPLOTLIB 1.5.1 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

5. MDT SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF MATPLOTLIB 1.5.1 FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS
AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING MATPLOTLIB 1.5.1, OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material breach of its terms and conditions.

7. Nothing in this License Agreement shall be deemed to create any relationship of agency, partnership, or joint venture between MDT and Licensee.
This License Agreement does not grant permission to use MDT trademarks or trade name in a trademark sense to endorse or promote products or services of
Licensee, or any third party.

8. By copying, installing or otherwise using matplotlib 1.5.1, Licensee agrees to be bound by the terms and conditions of this License Agreement.




"""

#Imports

from Tkinter import *
import Tkinter as tk
from Tkinter import StringVar
import ttk
import tkMessageBox as mbox 				# for popup message boxes
import tkFileDialog as openfile 			# for Opening Files
import FileDialog 							#for building exe

import numpy as np
from pyhdf.SD import SD, SDC, SDS
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap
from scipy import interpolate
from scipy.interpolate import griddata
from scipy import integrate					#for building exe
import sys
import os

import six.moves							#for building exe


L_FONT = ("Verdana", 12)
M_FONT = ("Verdana", 10)
S_FONT = ("Verdana", 8)

#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

def fileformat():
	ff = tk.Tk()
	ff.wm_title("Filename Format")

	canvas = tk.Canvas(ff, height = 316, width = 600)
	canvas.grid(sticky = E)
	image = tk.PhotoImage(master = canvas, file = "./fileformat.gif", height = 316, width = 600)

	showcanvas = canvas.create_image(600/2, 316/2, image = image)

	button = ttk.Button(ff, text = "OK", command =  ff.destroy)
	button.grid(sticky = SE, padx = 10, pady = 10)
	ff.mainloop()

class modisApp(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		self.filenames = {"mod06": tk.StringVar(), "mod35": tk.StringVar(), "mod03": tk.StringVar()}
		self.icon = 'clienticon.ico'
		self.filenames["mod06"].set("")
		self.filenames["mod35"].set("")
		self.filenames["mod03"].set("")

		tk.Tk.wm_iconbitmap(self, default = self.icon)
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
		helpmenu.add_command(label='Where to Download',command= lambda: mbox.showinfo('Where to Download','To download the necessary HDF files, you must visit the official website of NASA.\n\n The link is provided below:\n\nhttps://ladsweb.nascom.nasa.gov/data/search.html'))
		helpmenu.add_command(label='Filename Format', command = lambda: fileformat())
		menubar.add_cascade(label='Help',menu=helpmenu)

		tk.Tk.config(self, menu=menubar)
# END OF MENUBAR
		self.frames = {}

		for F in (SplashPage, InputPage, AttributesPage, RenderPage): #add every window class here

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="NSEW")

		self.show_frame(SplashPage)	#First window to show - Splash screen

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

	def get_filename(self, filename): # Strips away absolute path, leaves filename and extension
		rev = filename[::-1]
		for i in range(0,len(rev)):
			check = rev[i]
			if(check == "/"):
				break
		rev = rev[0:i]
		filename = rev[::-1]
		return filename

	def check_match(self): #SETS FLAG 'matched' IF SELECTED FILES MATCH
		if(self.filenames["mod06"].get() != ""):							# only set filenames for selected
			fname_mod06 = self.get_filename(self.filenames["mod06"].get())
			time_mod06 = fname_mod06[10:17] + fname_mod06[18:22]
		if(self.filenames["mod35"].get() != ""):
			fname_mod35 = self.get_filename(self.filenames["mod35"].get())
			time_mod35 = fname_mod35[10:17] + fname_mod35[18:22]
		if(self.filenames["mod03"].get() != ""):
			fname_mod03 = self.get_filename(self.filenames["mod03"].get())
			time_mod03 = fname_mod03[7:14] + fname_mod03[15:19]
		# checking conditions
		#All three
		if((self.filenames["mod06"].get() != "") and (self.filenames["mod35"].get() != "") and (self.filenames["mod03"].get() != "")):
			if(time_mod06 == time_mod35 == time_mod03):
				return 1
			else:
				return 0
		# MOD35 	and 	mod03
		elif((self.filenames["mod06"].get() == "") and (self.filenames["mod35"].get() != "") and (self.filenames["mod03"].get() != "")):
			if(time_mod35 == time_mod03):
				return 1
			else:
				return 0
		#			mod06 and mod03
		elif((self.filenames["mod06"].get() != "") and (self.filenames["mod35"].get() == "") and (self.filenames["mod03"].get() != "")):
			if(time_mod06 == time_mod03):
				return 1
			else:
				return 0
		#mod35 and mod06
		elif((self.filenames["mod06"].get() != "") and (self.filenames["mod35"].get() != "") and (self.filenames["mod03"].get() == "")):
			if(time_mod06 == time_mod35):
				return 1
			else:
				return 0
		else:
			return 1 # when only one file is selected no need to compare

	def navigate_render(self):
		if((self.filenames["mod06"].get() == "") and (self.filenames["mod35"].get() == "") and (self.filenames["mod03"].get() == "")):
			mbox.showerror("Error", "Input the required files")
		elif((self.filenames["mod06"].get() == "") and (self.filenames["mod35"].get() == "") and (self.filenames["mod03"].get() != "")):
			mbox.showerror("Error", "Input the required files")
		else:
			match = self.check_match()
			if(match == 1):

				self.show_frame(RenderPage)
			else:
				mbox.showerror("Error", "Input files did not match!\n\nData date and time must be the same.\n\nSee Help > Filename Format.")

	def navigate_attrib(self):
		if((self.filenames["mod06"].get() == "") and (self.filenames["mod35"].get() == "") and (self.filenames["mod03"].get() == "")):
			mbox.showerror("Error", "Input the required files")
		elif((self.filenames["mod06"].get() == "") and (self.filenames["mod35"].get() == "") and (self.filenames["mod03"].get() != "")):
			mbox.showerror("Error", "Input the required files")
		else:
			match = self.check_match()
			if(match == 1):
				self.show_frame(AttributesPage)
			else:
				mbox.showerror("Error", "Input files did not match!\n\nData date and time must be the same.\n\nSee Help > Filename Format.")

#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

class SplashPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)

		self.grid_rowconfigure(0, weight = 1)
		self.grid_columnconfigure(0, weight = 1)

		centerframe = Frame(self)
		centerframe.grid()

		label0 = ttk.Label(centerframe, text="MODIS Data Renderer", font=L_FONT)
		label0.grid(sticky = N, row = 0, columnspan = 3, pady=10,padx=10)

		label1 = ttk.Label(centerframe, text  = "A Graphical User Interface of Selected Moderate Resolution Imaging Spectroradiometer Data", font = M_FONT)
		label1.grid(sticky = N, row = 1, columnspan = 3, pady = 10, padx = 10)

		button0 = ttk.Button(centerframe, text='Proceed', command = lambda: controller.show_frame(InputPage))
		button0.grid(row = 2, column = 1, padx = 10, pady=10)

		button1 = ttk.Button(centerframe, text = "Developers", command = lambda: mbox.showinfo("Developers","   Alvin B. Esquivel\n\n   Mark Steven Luber\n\n   Mark Angelo Serrano"))
		button1.grid(row = 3, column = 1, padx = 10, pady = 10)

#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

class InputPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self,parent)
		self.controller = controller

#DEFINING METHODS

		def OpenHDF_cp(): #cp  = cloud products - MOD06
			filein1 = openfile.askopenfile(filetypes = (("HDF file", "*.hdf"),("All files", "*.*")))
			if(filein1 != None):			# 'Nonetype' has no .name attribute
				entrybox1.delete(0, END)
				filename = self.controller.get_filename(filein1.name)
				if(filename[0:5] != "MOD06"):
					mbox.showerror("Error", "Please input the correct HDF file.\n\nNote: Leave filename as-is upon download.")
				else:
					entrybox1.insert(0, filename)
					self.controller.filenames["mod06"].set(filein1.name)

		def OpenHDF_cm(): #cm = cloud mask - MOD35
			filein2 = openfile.askopenfile(filetypes = (("HDF file", "*.hdf"),("All files", "*.*")))
			if(filein2 != None):			# 'Nonetype' has no .name attribute
				entrybox2.delete(0, END)
				filename = self.controller.get_filename(filein2.name)
				if(filename[0:5] != "MOD35"):
					mbox.showerror("Error", "Please input the correct HDF file.\n\nNote: Leave filename as-is upon download.")
				else:
					entrybox2.insert(0, filename)
					self.controller.filenames["mod35"].set(filein2.name)

		def OpenHDF_geo(): #geo = geolocation - MOD03
			filein3 = openfile.askopenfile(filetypes = (("HDF file", "*.hdf"),("All files", "*.*")))
			if(filein3 != None):			# 'Nonetype' has no .name attribute
				entrybox3.delete(0, END)
				filename = self.controller.get_filename(filein3.name)
				if(filename[0:5] != "MOD03"):
					mbox.showerror("Error", "Please input the correct HDF file.\n\nNote: Leave filename as-is upon download.")
				else:
					entrybox3.insert(0, filename)
					self.controller.filenames["mod03"].set(filein3.name)

		def Clear(): #clears inputs
			entrybox1.delete(0, END)
			entrybox2.delete(0, END)
			entrybox3.delete(0, END)
			self.controller.filenames["mod06"].set("")
			self.controller.filenames["mod35"].set("")
			self.controller.filenames["mod03"].set("")

#FRAME LAYOUT

		self.grid_columnconfigure(1, weight = 1)
		self.grid_rowconfigure(1, weight = 1)

		topframe = Frame(self)
		topframe.grid(column = 1)
		innerframe = Frame(self)
		innerframe.grid(column = 1, sticky = NSEW, padx = 15)
		bottomframe = Frame(self)
		bottomframe.grid(column = 1, sticky = E, padx = 15)

		innerframe.grid_columnconfigure(2, weight = 1)
		innerframe.grid_rowconfigure(2, weight = 1)
		innerframe.grid_rowconfigure(4, weight = 1)
		innerframe.grid_rowconfigure(6, weight = 1)

#LABELS
		label = ttk.Label(topframe, text="Input MODIS Atmospheric Products (.HDF)", font=L_FONT)
		label.pack(pady = 10)

		label1 = ttk.Label(innerframe, text="MOD06 Cloud Properties", font=M_FONT)
		label1.grid(row=2,column=0, padx = 5, pady = 10)

		label1a = ttk.Label(innerframe, text="MOD06 is a level 2 MODIS atmosphere product that monitors the physical and radiative\n properties of clouds. Cloud Top Temperature, Cloud Top Pressure, Effective Radius, \nCloud Water Path and Cloud Optical Thickness are the basic SDS that can be\n extracted from this file. ", font=M_FONT)
		label1a.grid(row=3,columnspan=10)

		label2 = ttk.Label(innerframe, text="MOD35 Cloud Mask", font=M_FONT)
		label2.grid(row=4,column=0,padx = 5, pady = 10)

		label2a = ttk.Label(innerframe, text="MOD35 is a level 2 MODIS atmosphere product that indicates whether the instrument's\n field of view of Earth's surface is affected by clouds or cloud shadows.\nSurface Type and Unobstructed FOV Quality Flag can be extracted from this file.", font=M_FONT)
		label2a.grid(row=5,columnspan=10)

		label3 = ttk.Label(innerframe, text="MOD03 Geolocation", font=M_FONT)
		label3.grid(row=6,column=0,padx = 5, pady = 10)

		label3a = ttk.Label(innerframe, text="MOD03 is a MODIS Geolocation product containing geodetic coordinates, ground elevation,\n and solar and satellite zenith, and azimuth angle for each MODIS 1-km sample.\n Geolocation file is optional", font=M_FONT)
		label3a.grid(row=7,columnspan=10)

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

		button5 = ttk.Button(bottomframe, text="Go to Attributes Page",command = controller.navigate_attrib)
		button5.grid(column = 2, row = 0,padx = 10, pady = 10)

		button6 = ttk.Button(bottomframe, text="Go to Render Page",command = controller.navigate_render)
		button6.grid(column = 3, row = 0, padx = 10, pady = 10)




#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

class AttributesPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.selected_prod = StringVar()
		self.selected_sds = StringVar()

# FRAME LAYOUTS

		self.grid_columnconfigure(1, weight = 1)
		self.grid_rowconfigure(1, weight = 1)

		topframe = Frame(self)
		topframe.grid(columnspan = 2)
		leftframe = Frame(self)
		leftframe.grid(column = 0, sticky = N)
		rightframe = Frame(self)
		rightframe.grid(row = 1, column = 1, sticky = N+W)
		bottomframe = Frame(self)
		bottomframe.grid(columnspan = 2, sticky = E)
		rightframe_sub = Frame(rightframe)
		rightframe_sub.grid(row = 1)
		rightframe_sub.grid_propagate(False)

		leftframe_sub_left = Frame(leftframe)
		leftframe_sub_left.grid(row = 0, column = 0)
		leftframe_sub_right = Frame(leftframe)
		leftframe_sub_right.grid(row = 0, column = 1)
		rightframe.grid_columnconfigure(0, weight = 1)
# LABELS

		attrib = ttk.Label(topframe, text = "Attributes", font = L_FONT).pack(padx = 10, pady = 10)
		products = ttk.Label(leftframe_sub_left, text = "Products", font = L_FONT).grid(row =0, padx = 10, pady = 10)
		sci_data_sets = ttk.Label(leftframe_sub_right, text = "Scientific Data Sets", font = L_FONT).grid(row = 0, columnspan = 2, pady = 10)
		metadata = ttk.Label(rightframe, text = "Metadata", font = L_FONT).grid(row = 0, padx = 10, pady = 10)

		indicator1 = ttk.Label(leftframe_sub_left, text = 0, textvariable = self.selected_prod, font = S_FONT).grid(row = 1, padx = 5, pady = 5)
		indicator2 = ttk.Label(leftframe_sub_right, text = 0, textvariable = self.selected_sds, font = S_FONT).grid(row = 1, columnspan = 2, padx = 5, pady = 5)

# BUTTONS

		renderbutton = ttk.Button(bottomframe, text = "Go to Render Page", command = lambda: controller.show_frame(RenderPage)).pack(side = RIGHT, padx = 10, pady = 10)

		backbutton = ttk.Button(bottomframe, text = "Go to Input Page", command = lambda: controller.show_frame(InputPage)).pack(side = RIGHT, padx = 10, pady = 10)


# LISTBOXES

		self.listbox0 = tk.Listbox(leftframe_sub_left ,height = 19, font = M_FONT)
		self.listbox0.grid(row = 2, padx = 10, pady = 10)

		self.listbox0.insert(END, "Cloud Mask")
		self.listbox0.insert(END, "Cloud Products")
		self.listbox0.insert(END, "Geolocation")

		self.listbox0.bind("<<ListboxSelect>>", self.show_sds)

		scrollbar0 = ttk.Scrollbar(leftframe_sub_right, orient = "vertical")

		self.listbox1 = tk.Listbox(leftframe_sub_right, width = 25, height = 19, font = M_FONT, yscrollcommand = scrollbar0.set)
		self.listbox1.grid(pady = 10, row = 2, column = 0)

		self.listbox1.bind("<<ListboxSelect>>", self.show_meta)

		scrollbar0.config(command = self.listbox1.yview)
		scrollbar0.grid(column = 1, row = 2, sticky = N+S)

# TEXT BOX

		self.textbox0 = tk.Text(rightframe_sub, font = L_FONT, borderwidth = 2, relief = "sunken", height = 19)
		self.textbox0.pack(fill = BOTH, expand = True, pady = 10)
		self.textbox0.config(state = NORMAL)

		scrollb = ttk.Scrollbar(rightframe, command=self.textbox0.yview)
		scrollb.grid(row = 1, column = 1, sticky = N+S+W)
		self.textbox0['yscrollcommand'] = scrollb.set

##################################################################################################################################
##################################################################################################################################

	def show_sds(self, event):	#populates listbox with scientific data sets when product clicked
		widget = event.widget
		selection=widget.curselection()
		value = widget.get(selection)
		self.selected_product = value
		self.selected_prod.set(self.selected_product)
		if(value == 'Cloud Mask'):
			if(self.controller.filenames["mod35"].get() == ""):
				mbox.showerror("Error", "Input MOD35 (Cloud Mask) file!")
			else:
				_file = str(self.controller.filenames["mod35"].get())
				read = SD(_file, SDC.READ)
				datasets = read.datasets()
				datasets_list = datasets.keys()
		elif(value == 'Cloud Products'):
			if(self.controller.filenames["mod06"].get() == ""):
				mbox.showerror("Error", "Input MOD06 (Cloud Products) file!")
			else:
				_file = str(self.controller.filenames["mod06"].get())
				read = SD(_file, SDC.READ)
				datasets = read.datasets()
				datasets_list = datasets.keys()
		elif(value == 'Geolocation'):
			if(self.controller.filenames["mod03"].get() == ""):
				mbox.showerror("Error", "Input MOD03 (Geolocation) file!")
			else:
				_file = str(self.controller.filenames["mod03"].get())
				read = SD(_file, SDC.READ)
				datasets = read.datasets()
				datasets_list = datasets.keys()

		self.listbox1.delete(0, END)
		self.selected_sds.set("")
		self.textbox0.delete(1.0, END)

		for i in range(len(datasets_list)):
			self.listbox1.insert(END, datasets_list[i])
		read.end()


	def show_meta(self, event):	#populates text field with Metadata
		widget = event.widget
		selection=widget.curselection()
		value = widget.get(selection)
		self.textbox0.delete(1.0, END)
		if(self.selected_product == "Cloud Mask"):
			_file = str(self.controller.filenames["mod35"].get())
		elif(self.selected_product == "Cloud Products"):
			_file = str(self.controller.filenames["mod06"].get())
		elif(self.selected_product == "Geolocation"):
			_file = str(self.controller.filenames["mod03"].get())

		read = SD(_file, SDC.READ)
		self.selected_sds.set(value)
		sds = read.select(self.selected_sds.get())

		data = sds.attributes(full=1)
		data_keys_lst = data.keys()
		self.textbox0.insert(END, "\n")
		self.textbox0.insert(END, "************************************\n")
		self.textbox0.insert(END, value + "\n")
		self.textbox0.insert(END, "============================\n")
		for key in data_keys_lst:
			self.textbox0.insert(END, key + ":")
			self.textbox0.insert(END, data[key])
			self.textbox0.insert(END, "\n")
		self.textbox0.insert(END, "============================\n")
		read.end()

#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

class RenderPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

#FRAMES

		self.grid_rowconfigure(2, weight = 1)
		self.grid_columnconfigure(1, weight = 1)

		topframe = Frame(self)
		topframe.grid(row = 0, sticky = N, columnspan = 2)
		leftframe = Frame(self)
		leftframe.grid(row = 1, column = 0, sticky = N)
		rightframe = Frame(self)
		rightframe.grid(row = 1, column = 1)
		bottomframe = Frame(self)
		bottomframe.grid(row = 2, columnspan = 2, sticky = SE)

		selected = StringVar()
		selected.set("Cloud_Optical_Thickness") # Initialize 'selected' variable for radiobuttons

#RADIO BUTTONS

		Radiobutton(leftframe, text = "Cloud Optical Thickness", value= "Cloud_Optical_Thickness", variable = selected, font = M_FONT, command = lambda: self.show_desc(selected.get())).grid(row = 1, column = 0, sticky = W, padx = 20)
		Radiobutton(leftframe, text = "Cloud Water Path", value= "Cloud_Water_Path", variable = selected, font = M_FONT, command = lambda: self.show_desc(selected.get())).grid(row = 2, column = 0, sticky = W, padx = 20)
		Radiobutton(leftframe, text = "Cloud Effective Radius", value = "Cloud_Effective_Radius", variable = selected, font = M_FONT, command = lambda: self.show_desc(selected.get())).grid(row = 3, column = 0, sticky = W, padx = 20)
		Radiobutton(leftframe, text = "Cloud Top Temperature", value = "Cloud_Top_Temperature", variable = selected, font = M_FONT, command = lambda: self.show_desc(selected.get())).grid(row = 4, column = 0, sticky = W, padx = 20)
		Radiobutton(leftframe, text = "Cloud Top Pressure", value = "Cloud_Top_Pressure", variable = selected, font = M_FONT, command = lambda: self.show_desc(selected.get())).grid(row = 5, column = 0, sticky = W, padx = 20)
		Radiobutton(leftframe, text = "Surface Type", value = "Surface_Type", variable = selected, font = M_FONT, command = lambda: self.show_desc(selected.get())).grid(row = 7, column = 0, sticky = W, padx = 20)
		Radiobutton(leftframe, text = "Unobstructed FOV Quality Flag", value = "FOV_Quality", variable = selected, font = M_FONT, command = lambda: self.show_desc(selected.get())).grid(row = 8, column = 0, sticky = W, padx = 20)
		Radiobutton(leftframe, text = "Real Map", value = "Real_Map", variable = selected, font = M_FONT, command = lambda: self.show_desc(selected.get())).grid(row = 10, column = 0, sticky = W, padx = 20)


#LABELS
		label = ttk.Label(topframe, text="Render Page", font=L_FONT)
		label.pack(padx = 20, pady = 20)

		descriptionlabel = ttk.Label(rightframe, text = "Description", font = M_FONT)
		descriptionlabel.pack(side = TOP, pady = 10)

		mod06label = ttk.Label(leftframe, text = "Cloud Products", font = M_FONT)
		mod06label.grid(row = 0, column = 0, pady = 10)
		mod35label = ttk.Label(leftframe, text = "Cloud Mask", font = M_FONT)
		mod35label.grid(row = 6, column = 0, pady = 10)
		maplabel = ttk.Label(leftframe, text = "Map", font = M_FONT)
		maplabel.grid(row = 9, column = 0 , pady = 10)


#BUTTONS
		applybutton = ttk.Button(bottomframe, text = "Render", command = lambda: self.render_data(selected.get()))
		applybutton.pack(side = RIGHT, padx = 10, pady = 10)
		attribbutton = ttk.Button(bottomframe, text="Go to Attributes Page", command = lambda: controller.show_frame(AttributesPage))
		attribbutton.pack(side = RIGHT, padx = 10, pady = 10)
		backbutton = ttk.Button(bottomframe, text="Go to Input Page", command = lambda: controller.show_frame(InputPage))
		backbutton.pack(side = RIGHT, padx = 10, pady = 10)

#TEXT BOX

		self.tb = Text(rightframe, height = 16, width = 43, borderwidth = 3, relief = SUNKEN, font = L_FONT)
		self.tb.pack()


#################################################################################################################################
#################################################################################################################################

	def show_desc(self, selected):		#Shows a brief description of selected SDS
		self.tb.delete(1.0, END)
		if(selected == "Cloud_Optical_Thickness"):
			self.tb.insert(END, "Cloud optical thickness is a measure of attenuation of the light passing through the atmosphere due to the scattering and absorption by cloud droplets.")

		elif(selected == "Cloud_Water_Path"):
			self.tb.insert(END, "It is the amount of liquid water in the cloud. Cloud Liquid Water is usually expressed either in g/m^2 or mg/cm^2. It varies greatly from cloud to cloud and also depends on its components.")

		elif(selected == "Cloud_Top_Pressure"):
			self.tb.insert(END, "Cloud top pressure is atmospheric pressure at the level of the cloud top. Accurate information on cloud top pressure and height are needed in order to retrieve properly many atmospheric and surface properties. It also plays an important role in the net earth radiation budget studies")

		elif(selected == "Cloud_Top_Temperature"):
			self.tb.insert(END, "It is the atmospheric temperature at the level of the cloud top. Accurate information on cloud top temperature are needed in order to retrieve properly many atmospheric and surface properties. It also plays an important role in the net earth radiation budget studies.")

		elif(selected == "Cloud_Effective_Radius"):
			self.tb.insert(END, "Cloud drop effective radius (alternatively cloud effective radius or effective radius) is a weighted mean of the size distribution of cloud droplets.")

		elif(selected == "Surface_Type"): # Surface Type
			self.tb.insert(END, "Surface Type is the type of surface being projected whether it is land, water or if it is blocked by clouds.")

		elif(selected == "FOV_Quality"): # Unobstructed FOV Quality Flag
			self.tb.insert(END, "Unobstructed FOV Quality Flag indicates whether the field of view to Earth's surface is cloudy, probably cloudy, probably clear or confident clear.")

		elif(selected == "Real_Map"): # Unobstructed FOV Quality Flag
			self.tb.insert(END, "A map projection based on coastal flags from surface type that show the outline of land masses.")

	def render_data(self, selected):
		if(selected == "Cloud_Optical_Thickness"):
			_filename = str(self.controller.filenames["mod06"].get())
			_filename_geo = str(self.controller.filenames["mod03"].get())
			if(_filename == ""): #if filename is blank meaning no selected product
				mbox.showerror("Error", "Input MOD06 (Cloud Prducts) file!")
			else:
				if(_filename_geo != ""):
					read_mod06 = SD(_filename, SDC.READ)
					read_mod03 = SD(_filename_geo, SDC.READ)

					mod03_lon = read_mod03.select('Longitude')
					mod03_lat = read_mod03.select('Latitude')
					mod06_sds = read_mod06.select('Cloud_Optical_Thickness')
					mod03_lon_data = mod03_lon.get()
					mod03_lat_data = mod03_lat.get()

					ArrayShape = mod03_lat_data.shape
					as0 = ArrayShape[0] - 1
					as1 = ArrayShape[1] - 1
					latmin = mod03_lat_data[0,0]
					latmax = mod03_lat_data[as0,as1]
					lat_0 = latmin + (latmax - latmin) / 2

					tmp0 = mod03_lon_data[0,0]
					tmp1 = mod03_lon_data[as0,as1]

					lonmin = min(mod03_lon_data[0,0], mod03_lon_data[as0,as1])
					lonmax = max(mod03_lon_data[0,0], mod03_lon_data[as0,as1])
					lon_0 = lonmin + (lonmax - lonmin) / 2

					if lon_0 > 180:
						lon_0 = - (360 - lon_0)

					mod03_lon_data[0,0] = tmp0
					mod03_lon_data[as0,as1] = tmp1


					fig = plt.figure()
					ax = fig.add_subplot(111)
					ax.patch.set_facecolor('black')
					def format_coord(x, y):
						return 'Longitude={:6.3f}\nLatitude={:6.3f}\nPixel value:'.format(x, y)
					ax.format_coord = format_coord
					m1 = Basemap(projection = 'ortho', lon_0 = lon_0, lat_0 = lat_0, resolution = None)
					xpt0, ypt0 = m1(lon_0, lat_0)
					xpt1, ypt1 = m1(mod03_lon_data[0,0], mod03_lat_data[0,0])
					xpt2, ypt2 = m1(mod03_lon_data[0, as1], mod03_lat_data[0,as1])
					xpt3, ypt3 = m1(mod03_lon_data[as0,as1], mod03_lat_data[as0,as1])
					xpt4, ypt4 = m1(mod03_lon_data[as0,0], mod03_lat_data[as0,0])

					llx = min(xpt1, xpt2, xpt3, xpt4) - xpt0
					lly = min(ypt1, ypt2, ypt3, ypt4) - ypt0
					urx = max(xpt1, xpt2, xpt3, xpt4) - xpt0
					ury = max(ypt1, ypt2, ypt3, ypt4) - ypt0

					m = Basemap(projection = 'ortho', lon_0 = lon_0, lat_0 = lat_0, resolution = 'l', llcrnrx = llx, llcrnry = lly, urcrnrx = urx, urcrnry= ury)

					lon = mod03_lon.get()
					lat = mod03_lat.get()

					x_igrid, y_igrid = m(lon,lat)
					x_igrid = x_igrid - xpt0
					y_igrid = y_igrid - ypt0
					z_igrid = mod06_sds.get()
					z_igrid = z_igrid * 0.01
					x1_igrid = x_igrid.ravel()
					y1_igrid = y_igrid.ravel()
					z1_igrid = z_igrid.ravel()
					xy1_igrid = np.vstack((x1_igrid, y1_igrid)).T
					xi, yi = np.mgrid[llx:urx:1000j, lly:ury:1000j]
					z = griddata(xy1_igrid, z1_igrid, (xi, yi), method='cubic')
					cmap = plt.cm.nipy_spectral
					bounds = np.arange(0, 151, 10)
					norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
					img = m.imshow(z.T, vmin = 0.0, vmax = 150.0, cmap = cmap, interpolation = 'nearest', origin = 'lower')
					cbar = plt.colorbar(img, cmap = cmap, norm = norm, boundaries = None, ticks = bounds)
					m.drawcoastlines(color = 'w')
					m.drawparallels(np.arange(-90.,120.,5.), color='w', labels=[True,False,False,False])
					m.drawmeridians(np.arange(115.,360.,5.), color='w', labels=[False,False,False,True])
					plt.title("MODIS L2 CLOUD OPTICAL THICKNESS")
					plt.show()
				else:
					mbox.showinfo("Warning","No selected MOD03 Geolocation file.\n\nLongitude and Latitude data and map projection are not available.")
					read_mod06 = SD(_filename, SDC.READ)
					sds = read_mod06.select('Cloud_Optical_Thickness')
					sds_data = sds.get()

					for x in np.nditer(sds_data, op_flags = ['readwrite']):
						if (x[...] == -9999):
							x[...] = 0

					fig = plt.figure()
					ax = fig.add_subplot(111)
					cmap = plt.cm.nipy_spectral
					bounds = np.arange(0, 151, 10)
					norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
					sds_data = sds_data * 0.01

					img = plt.imshow(np.flipud(sds_data), vmin = 0.0, vmax = 150.0, cmap = cmap, interpolation = 'nearest', origin = 'lower')
					cbar = plt.colorbar(img, cmap=cmap, norm=norm, boundaries=None, ticks=bounds)
					plt.title('MODIS L2 CLOUD OPTICAL THICKNESS')
					plt.show()

		elif(selected == "Cloud_Water_Path"):
			_filename = str(self.controller.filenames["mod06"].get())
			_filename_geo = str(self.controller.filenames["mod03"].get())
			if(_filename == ""):
				mbox.showerror("Error", "Input MOD06 (Cloud Products) file!")
			else:
				if(_filename_geo != ""):
					read_mod06 = SD(_filename, SDC.READ)
					read_mod03 = SD(_filename_geo, SDC.READ)

					mod03_lon = read_mod03.select('Longitude')
					mod03_lat = read_mod03.select('Latitude')
					mod06_sds = read_mod06.select('Cloud_Water_Path')
					mod03_lon_data = mod03_lon.get()
					mod03_lat_data = mod03_lat.get()
					mod06_sds_data = mod06_sds.get()

					ArrayShape = mod03_lat_data.shape
					as0 = ArrayShape[0] - 1
					as1 = ArrayShape[1] - 1
					latmin = mod03_lat_data[0,0]
					latmax = mod03_lat_data[as0,as1]
					lat_0 = latmin + (latmax - latmin) / 2

					tmp0 = mod03_lon_data[0,0]
					tmp1 = mod03_lon_data[as0,as1]

					lonmin = min(mod03_lon_data[0,0], mod03_lon_data[as0,as1])
					lonmax = max(mod03_lon_data[0,0], mod03_lon_data[as0,as1])
					lon_0 = lonmin + (lonmax - lonmin) / 2

					if lon_0 > 180:
						lon_0 = - (360 - lon_0)

					mod03_lon_data[0,0] = tmp0
					mod03_lon_data[as0,as1] = tmp1


					fig = plt.figure()
					ax = fig.add_subplot(111)
					ax.patch.set_facecolor('black')
					def format_coord(x, y):
						return 'Longitude={:6.3f}\nLatitude={:6.3f}\nPixel value:'.format(x, y)
					ax.format_coord = format_coord
					m1 = Basemap(projection = 'ortho', lon_0 = lon_0, lat_0 = lat_0, resolution = None)
					xpt0, ypt0 = m1(lon_0, lat_0)
					xpt1, ypt1 = m1(mod03_lon_data[0,0], mod03_lat_data[0,0])
					xpt2, ypt2 = m1(mod03_lon_data[0, as1], mod03_lat_data[0,as1])
					xpt3, ypt3 = m1(mod03_lon_data[as0,as1], mod03_lat_data[as0,as1])
					xpt4, ypt4 = m1(mod03_lon_data[as0,0], mod03_lat_data[as0,0])

					llx = min(xpt1, xpt2, xpt3, xpt4) - xpt0
					lly = min(ypt1, ypt2, ypt3, ypt4) - ypt0
					urx = max(xpt1, xpt2, xpt3, xpt4) - xpt0
					ury = max(ypt1, ypt2, ypt3, ypt4) - ypt0

					m = Basemap(projection = 'ortho', lon_0 = lon_0, lat_0 = lat_0, resolution = 'l', llcrnrx = llx, llcrnry = lly, urcrnrx = urx, urcrnry= ury)

					lon = mod03_lon.get()
					lat = mod03_lat.get()

					x_igrid, y_igrid = m(lon,lat)
					x_igrid = x_igrid - xpt0
					y_igrid = y_igrid - ypt0
					z_igrid = mod06_sds.get()
					z_igrid = z_igrid * 0.01
					x1_igrid = x_igrid.ravel()
					y1_igrid = y_igrid.ravel()
					z1_igrid = z_igrid.ravel()
					xy1_igrid = np.vstack((x1_igrid, y1_igrid)).T
					xi, yi = np.mgrid[llx:urx:1000j, lly:ury:1000j]
					z = griddata(xy1_igrid, z1_igrid, (xi, yi), method='cubic')
					cmap = plt.cm.nipy_spectral
					bounds = np.arange(0, 151, 10)
					norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
					img = m.imshow(z.T, vmin = 0.0, vmax = 150.0, cmap = cmap, interpolation = 'nearest', origin = 'lower')
					cbar = plt.colorbar(img, cmap = cmap, norm = norm, boundaries = None, ticks = bounds)
					cbar.set_label("g/m^2")
					m.drawcoastlines(color = 'w')
					m.drawparallels(np.arange(-90.,120.,5.), color='w', labels=[True,False,False,False])
					m.drawmeridians(np.arange(115.,360.,5.), color='w', labels=[False,False,False,True])
					plt.title("MODIS L2 CLOUD WATER PATH")
					plt.show()

				else:
					mbox.showinfo("Warning","No selected MOD03 Geolocation file.\n\nLongitude and Latitude data and map projection are not available.")
					read_mod06 = SD(_filename, SDC.READ)
					sds_name = 'Cloud_Water_Path'
					sds_index = read_mod06.select(sds_name)
					sds_index_data = sds_index.get()

					for x in np.nditer(sds_index_data, op_flags = ['readwrite']):
						if (x[...] == -9999):
							x[...] = 0

					fig = plt.figure()
					ax = fig.add_subplot(111)
					cmap = plt.cm.nipy_spectral
					bounds = np.arange(0, 61, 10)
					norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
					sds_index_data = sds_index_data * 0.01
					img = plt.imshow(np.flipud(sds_index_data), vmin = 0.0, vmax = 60, cmap = cmap, interpolation = 'nearest', origin = 'lower')
					cbar = plt.colorbar(img, cmap = cmap, norm = norm, boundaries = None, ticks = bounds)
					cbar.set_label("g/m^2")
					plt.title('MODIS L2 CLOUD WATER PATH')
					plt.show()

		elif(selected == "Cloud_Effective_Radius"):
			_filename = str(self.controller.filenames["mod06"].get())
			_filename_geo = str(self.controller.filenames["mod03"].get())
			if(_filename == ""):
				mbox.showerror("Error", "Input MOD06 (Cloud Products) file!")
			else:
				if(_filename_geo != ""):
					read_mod06 = SD(_filename, SDC.READ)
					read_mod03 = SD(_filename_geo, SDC.READ)
					mod03_lon = read_mod03.select('Longitude')
					mod03_lat = read_mod03.select('Latitude')
					mod06_sds = read_mod06.select('Cloud_Effective_Radius')
					mod03_lon_data = mod03_lon.get()
					mod03_lat_data = mod03_lat.get()
					mod06_sds_data = mod06_sds.get()

					ArrayShape = mod03_lat_data.shape
					as0 = ArrayShape[0] - 1
					as1 = ArrayShape[1] - 1
					latmin = mod03_lat_data[0,0]
					latmax = mod03_lat_data[as0,as1]
					lat_0 = latmin + (latmax - latmin) / 2

					tmp0 = mod03_lon_data[0,0]
					tmp1 = mod03_lon_data[as0,as1]

					lonmin = min(mod03_lon_data[0,0], mod03_lon_data[as0,as1])
					lonmax = max(mod03_lon_data[0,0], mod03_lon_data[as0,as1])
					lon_0 = lonmin + (lonmax - lonmin) / 2

					if lon_0 > 180:
						lon_0 = - (360 - lon_0)

					mod03_lon_data[0,0] = tmp0
					mod03_lon_data[as0,as1] = tmp1

					fig = plt.figure()
					ax = fig.add_subplot(111)
					ax.patch.set_facecolor('black')
					def format_coord(x, y):
						return 'Longitude={:6.3f}\nLatitude={:6.3f}\nPixel value:'.format(x, y)
					ax.format_coord = format_coord

					m1 = Basemap(projection = 'ortho', lon_0 = lon_0, lat_0 = lat_0, resolution = None)
					xpt0, ypt0 = m1(lon_0, lat_0)
					xpt1, ypt1 = m1(mod03_lon_data[0,0], mod03_lat_data[0,0])
					xpt2, ypt2 = m1(mod03_lon_data[0, as1], mod03_lat_data[0,as1])
					xpt3, ypt3 = m1(mod03_lon_data[as0,as1], mod03_lat_data[as0,as1])
					xpt4, ypt4 = m1(mod03_lon_data[as0,0], mod03_lat_data[as0,0])

					llx = min(xpt1, xpt2, xpt3, xpt4) - xpt0
					lly = min(ypt1, ypt2, ypt3, ypt4) - ypt0
					urx = max(xpt1, xpt2, xpt3, xpt4) - xpt0
					ury = max(ypt1, ypt2, ypt3, ypt4) - ypt0

					m = Basemap(projection = 'ortho', lon_0 = lon_0, lat_0 = lat_0, resolution = 'l', llcrnrx = llx, llcrnry = lly, urcrnrx = urx, urcrnry= ury)

					lon = mod03_lon.get()
					lat = mod03_lat.get()

					x_igrid, y_igrid = m(lon,lat)
					x_igrid = x_igrid - xpt0
					y_igrid = y_igrid - ypt0
					z_igrid = mod06_sds.get()
					z_igrid = z_igrid * 0.01
					x1_igrid = x_igrid.ravel()
					y1_igrid = y_igrid.ravel()
					z1_igrid = z_igrid.ravel()
					xy1_igrid = np.vstack((x1_igrid, y1_igrid)).T
					xi, yi = np.mgrid[llx:urx:1000j, lly:ury:1000j]
					z = griddata(xy1_igrid, z1_igrid, (xi, yi), method='cubic')
					cmap = plt.cm.nipy_spectral
					bounds = np.arange(0, 151, 10)
					norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
					img = m.imshow(z.T, vmin = 0.0, vmax = 150.0, cmap = cmap, interpolation = 'nearest', origin = 'lower')
					cbar = plt.colorbar(img, cmap = cmap, norm = norm, boundaries = None, ticks = bounds)
					cbar.set_label("Microns")
					m.drawcoastlines(color = 'w')
					m.drawparallels(np.arange(-90.,120.,5.), color='w', labels=[True,False,False,False])
					m.drawmeridians(np.arange(115.,360.,5.), color='w', labels=[False,False,False,True])
					plt.title('MODIS L2 CLOUD EFFECTIVE RADIUS')
					plt.show()
				else:
					mbox.showinfo("Warning","No selected MOD03 Geolocation file.\n\nLongitude and Latitude data and map projection are not available.")
					read_mod06 =SD(_filename, SDC.READ)
					sds = read_mod06.select('Cloud_Effective_Radius')
					sds_data = sds.get()

					for x in np.nditer(sds_data, op_flags = ['readwrite']):
						if (x[...] == -9999):
							x[...] = 0

					fig = plt.figure()
					ax = fig.add_subplot(111)
					cmap = plt.cm.nipy_spectral
					bounds = np.arange(5, 66, 10)
					norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
					sds_data = sds_data * 0.01
					img = plt.imshow(np.flipud(sds_data), vmin = 0, vmax = 60.0, cmap = cmap, interpolation = 'none', origin = 'lower')
					cbar = plt.colorbar(img, cmap = cmap, norm = norm, boundaries = None, ticks = bounds)
					cbar.set_label("microns")
					plt.title('MODIS L2 CLOUD EFFECTIVE RADIUS')
					plt.show()

		elif(selected == "Cloud_Top_Temperature"):
			_filename = str(self.controller.filenames["mod06"].get())
			if(_filename == ""):
				mbox.showerror("Error", "Input MOD06 (Cloud Products) file!")
			else:
				read_mod06 = SD(_filename, SDC.READ)
				mod06_Latitude = read_mod06.select('Latitude')
				mod06_Longitude = read_mod06.select('Longitude')
				mod06_sds = read_mod06.select('Cloud_Top_Temperature')
				mod03_Latitude_data = mod06_Latitude.get()
				mod03_Longitude_data = mod06_Longitude.get()
				mod06_sds_data = mod06_sds.get()

				#print "Read hdf done"

				#Find lat_0 and lon_0

				#print mod03_Latitude_data.shape
				#print mod03_Longitude_data.shape
				ArrayShape = mod03_Latitude_data.shape
				as0 = ArrayShape[0] - 1
				as1 = ArrayShape[1] - 1
				latmin = mod03_Latitude_data[0,0]
				latmax = mod03_Latitude_data[as0,as1]
				lat_0 = latmin + (latmax - latmin) / 2
				#print "lat_0: ", lat_0

				tmp_01 = mod03_Longitude_data[0,0]
				tmp_02 = mod03_Longitude_data[as0,as1]
				lonmin = min(mod03_Longitude_data[0,0],mod03_Longitude_data[as0,as1])
				lonmax = max(mod03_Longitude_data[0,0],mod03_Longitude_data[as0,as1])
				lon_0 = lonmin + (lonmax -lonmin) / 2

				if lon_0 > 180:
					lon_0 = - (360 - lon_0)
				mod03_Longitude_data[0,0] = tmp_01
				mod03_Longitude_data[as0,as1] = tmp_02

				#print latmin, latmax
				#print lonmin, lonmax
				#print "lat_0 and lon_0 done"


				#Orthographic map
				fig = plt.figure()
				ax = fig.add_subplot(111)
				ax.patch.set_facecolor('white')
				def format_coord(x, y):
					return 'Longitude{:6.3f}\nLatitude={:6.3f}\nPixel Value:'.format(x, y)
				ax.format_coord = format_coord
				m1 = Basemap(projection='ortho',lon_0=lon_0,lat_0=lat_0,resolution=None)
				xpt0, ypt0 = m1(lon_0,lat_0)
				xpt1, ypt1 = m1(mod03_Longitude_data[0,0],mod03_Latitude_data[0,0])
				xpt2, ypt2 = m1(mod03_Longitude_data[0,as1],mod03_Latitude_data[0,as1])
				xpt3, ypt3 = m1(mod03_Longitude_data[as0,as1], mod03_Latitude_data[as0,as1])
				xpt4, ypt4 = m1(mod03_Longitude_data[as0,0],mod03_Latitude_data[as0,0])
				llx = min(xpt1,xpt2,xpt3,xpt4) - xpt0
				lly = min(ypt1,ypt2,ypt3,ypt4) - ypt0
				urx = max(xpt1,xpt2,xpt3,xpt4) - xpt0
				ury = max(ypt1,ypt2,ypt3,ypt4) - ypt0

				m = Basemap(projection='ortho',lon_0=lon_0,lat_0=lat_0,resolution='l',\
							llcrnrx=llx,llcrnry=lly,urcrnrx=urx,urcrnry=ury)
				#print "Orthographic map done"

				#Plot MODIS data
				lon = mod06_Longitude.get()
				lat = mod06_Latitude.get()
				x_igrid, y_igrid = m(lon,lat)
				x_igrid = x_igrid - xpt0
				y_igrid = y_igrid - ypt0
				z_igrid = mod06_sds.get()
				z_igrid = z_igrid * 0.01
				x1_igrid = x_igrid.ravel()
				y1_igrid = y_igrid.ravel()
				z1_igrid = z_igrid.ravel()
				xy1_igrid = np.vstack((x1_igrid,y1_igrid)).T
				xi, yi = np.mgrid[llx:urx:1000j, lly:ury:1000j]
				z = griddata(xy1_igrid, z1_igrid, (xi, yi), method='cubic')
				cmap = plt.cm.nipy_spectral
				#mpl.colors.ListedColormap(['k', '0.55', '#0D0575', '#C9CDEC', '#CBC206'])
				bounds = np.arange(0, 301, 20)
				norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
				img = m.imshow(z.T, vmin = 0.0, vmax=300.0, cmap=cmap, interpolation = 'nearest', origin='lower')
				cbar = plt.colorbar(img, cmap = cmap, norm = norm, boundaries = None, ticks = bounds)
				cbar.set_label("Kelvin (K)")
				#cbar.ax.set_yticklabels(bounds, fontsize=10)
				m.drawcoastlines()
				m.drawparallels(np.arange(-90.,120.,5.), color='w', labels=[True,False,False,False])
				m.drawmeridians(np.arange(115.,360.,5.), color='w', labels=[False,False,False,True])
				ax.set_xlabel("", fontsize=10)
				ax.set_ylabel("", fontsize=10)
				plt.title('MODIS L2 CLOUD TOP TEMPERATURE')
				plt.show()

		elif(selected == "Cloud_Top_Pressure"):
			_filename = str(self.controller.filenames["mod06"].get())
			if(_filename == ""):
				mbox.showerror("Error", "Input MOD06 (Cloud Products) file!")
			else:
				read_mod06 = SD(_filename, SDC.READ)
				mod06_Latitude = read_mod06.select('Latitude')
				mod06_Longitude = read_mod06.select('Longitude')
				mod06_sds = read_mod06.select('Cloud_Top_Pressure')
				mod03_Latitude_data = mod06_Latitude.get()
				mod03_Longitude_data = mod06_Longitude.get()
				mod06_sds_data = mod06_sds.get()

				#print "Read hdf done"

				#Find lat_0 and lon_0

				#print mod03_Latitude_data.shape
				#print mod03_Longitude_data.shape
				ArrayShape = mod03_Latitude_data.shape
				as0 = ArrayShape[0] - 1
				as1 = ArrayShape[1] - 1
				latmin = mod03_Latitude_data[0,0]
				latmax = mod03_Latitude_data[as0,as1]
				lat_0 = latmin + (latmax - latmin) / 2
				#print "lat_0: ", lat_0

				tmp_01 = mod03_Longitude_data[0,0]
				tmp_02 = mod03_Longitude_data[as0,as1]
				lonmin = min(mod03_Longitude_data[0,0],mod03_Longitude_data[as0,as1])
				lonmax = max(mod03_Longitude_data[0,0],mod03_Longitude_data[as0,as1])
				lon_0 = lonmin + (lonmax -lonmin) / 2

				if lon_0 > 180:
					lon_0 = - (360 - lon_0)
				mod03_Longitude_data[0,0] = tmp_01
				mod03_Longitude_data[as0,as1] = tmp_02

				#print latmin, latmax
				#print lonmin, lonmax
				#print "lat_0 and lon_0 done"


				#Orthographic map
				fig = plt.figure()
				ax = fig.add_subplot(111)
				ax.patch.set_facecolor('white')
				def format_coord(x, y):
					return 'Longitude={:6.3f}\nLatitude={:6.3f}\nPixel value:'.format(x, y)
				ax.format_coord = format_coord

				m1 = Basemap(projection='ortho',lon_0=lon_0,lat_0=lat_0,resolution=None)
				xpt0, ypt0 = m1(lon_0,lat_0)
				xpt1, ypt1 = m1(mod03_Longitude_data[0,0],mod03_Latitude_data[0,0])
				xpt2, ypt2 = m1(mod03_Longitude_data[0,as1],mod03_Latitude_data[0,as1])
				xpt3, ypt3 = m1(mod03_Longitude_data[as0,as1], mod03_Latitude_data[as0,as1])
				xpt4, ypt4 = m1(mod03_Longitude_data[as0,0],mod03_Latitude_data[as0,0])
				llx = min(xpt1,xpt2,xpt3,xpt4) - xpt0
				lly = min(ypt1,ypt2,ypt3,ypt4) - ypt0
				urx = max(xpt1,xpt2,xpt3,xpt4) - xpt0
				ury = max(ypt1,ypt2,ypt3,ypt4) - ypt0

				m = Basemap(projection='ortho',lon_0=lon_0,lat_0=lat_0,resolution='l',\
							llcrnrx=llx,llcrnry=lly,urcrnrx=urx,urcrnry=ury)
				#print "Orthographic map done"

				#Plot MODIS data
				lon = mod06_Longitude.get()
				lat = mod06_Latitude.get()
				x_igrid, y_igrid = m(lon,lat)
				x_igrid = x_igrid - xpt0
				y_igrid = y_igrid - ypt0
				z_igrid = mod06_sds.get()
				z_igrid = z_igrid * 0.1
				x1_igrid = x_igrid.ravel()
				y1_igrid = y_igrid.ravel()
				z1_igrid = z_igrid.ravel()
				xy1_igrid = np.vstack((x1_igrid,y1_igrid)).T
				xi, yi = np.mgrid[llx:urx:1000j, lly:ury:1000j]
				z = griddata(xy1_igrid, z1_igrid, (xi, yi), method='cubic')
				cmap = plt.cm.nipy_spectral
				#mpl.colors.ListedColormap(['k', '0.55', '#0D0575', '#C9CDEC', '#CBC206'])
				bounds = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]
				norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
				#img = m.imshow(np.flipud(z_igrid), origin='lower', vmin = 0.0, vmax=1100.0, cmap=cmap)
				img = m.imshow(z.T, origin='lower', vmin = 0.0, vmax=1100.0, cmap=cmap)
				cbar = m.colorbar(img, cmap = cmap, norm = norm, boundaries = None, ticks = [0, 100, 200, 300, 400, 500,
																					   600, 700, 800, 900, 1000, 1100])
				cbar.ax.set_yticklabels([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100], fontsize=10)
				cbar.set_label("Hectopascal (hPa)")

				m.drawcoastlines()
				m.drawparallels(np.arange(-90.,120.,5.), color='k', labels=[True,False,False,False])
				m.drawmeridians(np.arange(115.,360.,5.), color='k', labels=[False,False,False,True])
				ax.set_xlabel("", fontsize=10)
				ax.set_ylabel("", fontsize=10)
				plt.title('MODIS L2 CLOUD TOP PRESSURE')
				plt.show()


		elif(selected == "Surface_Type"): #surface type
			_filename = str(self.controller.filenames['mod35'].get())
			if(_filename == ""):
				mbox.showerror("Error", "Input MOD35 (Cloud Mask) file!")
			else:
				read_mod35 = SD(_filename, SDC.READ)

				sds_name = 'Cloud_Mask'
				sds_index = read_mod35.select(sds_name)
				sds_data = sds_index.get()

				sds_data_0 = sds_data[0, :, :]
				sds_data_0_bin = sds_data_0.astype(dtype=np.uint8, order='K', casting='unsafe', subok=False, copy=False)

				for x in np.nditer(sds_data_0_bin, op_flags=['readwrite']):
					x[...] = np.right_shift(x, 6)

				fig = plt.figure()
				ax = fig.add_subplot(111)
				cmap = plt.cm.brg
				bounds = [0, 1, 2, 3]
				norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
				img = plt.imshow(np.flipud(sds_data_0_bin), vmin = 0, vmax = 3, cmap = cmap, interpolation = 'nearest',
					origin = 'lower')
				cbar = plt.colorbar(img, cmap = cmap, norm = norm, boundaries = None, ticks = bounds)
				cbar.ax.set_yticklabels(['Water', 'Coastal', 'Desert', 'Land'], fontsize=10)
				ax.set_xlabel("", fontsize=7)
				ax.set_ylabel("", fontsize=1)
				plt.title('CLOUD MASK - SURFACE TYPE')
				plt.show()

		elif(selected == "FOV_Quality"): # Unobstructed FOV Quality Flag
			_filename = str(self.controller.filenames['mod35'].get())
			if(_filename == ""):
				mbox.showerror("Error", "Input MOD35 (Cloud Mask) file!")
			else:
				read_mod35 = SD(_filename, SDC.READ)
				sds_name='Cloud_Mask'
				sds_index = read_mod35.select(sds_name)
				sds_data = sds_index.get()
				sds_data_0 = sds_data[0, :, :]
				sds_data_0_bin = sds_data_0.astype(dtype=np.uint8, order='K', casting='unsafe', subok=False, copy=False)

				#print sds_data_0_bin[0,0]
				#print np.binary_repr(sds_data_0_bin[0,0], width=8)
				#x = np.right_shift(sds_data_0_bin[0,0], 1)
				#print x
				#print np.binary_repr(x, width=8) #original data


				#x_int8 = np.uint8(x)
				#y = np.left_shift(x_int8, 6)
				#print y
				#print np.binary_repr(y, width=8) #after shifting 6 bits to right (16 bits width)

				#y_int8 = np.uint8(y)
				#print y_int8
				#print np.binary_repr(y_int8, width=8) #after shifting 6 bits to the right (8 bits)

				#z = np.right_shift(y_int8, 6) #expexted data (8 bits)
				#print z

				for x in np.nditer(sds_data_0_bin, op_flags=['readwrite']):
					x[...] = np.right_shift(x, 1)

				for y in np.nditer(sds_data_0_bin, op_flags=['readwrite']):
					y[...] = np.left_shift(y, 6)

				for z in np.nditer(sds_data_0_bin, op_flags=['readwrite']):
					z[...] = np.right_shift(z, 6)

				fig = plt.figure()
				ax = fig.add_subplot(111)
				cmap = plt.cm.YlGn
				bounds = np.arange(0, 4, 1)
				norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
				img = plt.imshow(np.flipud(sds_data_0_bin), vmin = 0, vmax = 3, cmap = cmap, interpolation = 'nearest',
					origin = 'lower')
				cbar = plt.colorbar(img, cmap = cmap, norm = norm, boundaries = None, ticks = bounds)
				cbar.ax.set_yticklabels(['Confident Cloudy', 'Probably Cloudy', 'Probably Clear', 'Confident Clear'], fontsize = 10)
				ax.set_xlabel("", fontsize = 7)
				ax.set_ylabel("", fontsize = 1)
				plt.title('Cloud Mask - Unobstructed FOV Quality')
				plt.show()

		elif(selected == "Real_Map"):
			_filename = str(self.controller.filenames["mod35"].get())
			_filename_geo = str(self.controller.filenames["mod03"].get())

			#print _filename
			#print _filename_geo

			if((_filename != "") and (_filename_geo != "")):
				read_mod35 = SD(_filename, SDC.READ)
				read_mod03 = SD(_filename_geo, SDC.READ)

				mod03_lat = read_mod03.select('Latitude')
				mod03_lon = read_mod03.select('Longitude')
				mod03_lat_data = mod03_lat.get()
				mod03_lon_data = mod03_lon.get()
				mod35_sds = read_mod35.select('Cloud_Mask')

				#print mod03_lat_data.shape
				#print mod03_lon_data.shape

				ArrayShape = mod03_lat_data.shape
				as0 = ArrayShape[0] - 1
				as1 = ArrayShape[1] - 1

				latmin = mod03_lat_data[0,0]
				latmax = mod03_lat_data[as0,as1]

				lat_0 = latmin + (latmax - latmin) / 2

				#print lat_0

				tmp0 = mod03_lon_data[0,0]
				tmp1 = mod03_lon_data[as0, as1]

				lonmin = min(tmp0, tmp1)
				lonmax = max(tmp0, tmp1)

				lon_0 = lonmin + (lonmax - lonmin) / 2

				#print lon_0

				if lon_0 > 180:
					lon_0 = - (360 - lon_0)

				mod03_lon_data[0,0] = tmp0
				mod03_lon_data[as0,as1] = tmp1

				fig = plt.figure()
				ax = fig.add_subplot(111)
				ax.patch.set_facecolor('white')
				def format_coord(x, y):
					return 'Longitude={:6.3f}\nLatitude={:6.3f}\nPixel value:'.format(x, y)
				ax.format_coord = format_coord
				m1 = Basemap(projection = 'ortho', lon_0 = lon_0, lat_0 = lat_0, resolution = None)
				xpt0, ypt0 = m1(lon_0, lat_0)
				xpt1, ypt1 = m1(mod03_lon_data[0,0], mod03_lat_data[0,0])
				xpt2, ypt2 = m1(mod03_lon_data[0,as1], mod03_lat_data[0,as1])
				xpt3, ypt3 = m1(mod03_lon_data[as0, as1], mod03_lat_data[as0,as1])
				xpt4, ypt4 = m1(mod03_lon_data[as0, 0], mod03_lat_data[as0,0])

				llx = min(xpt1, xpt2, xpt3, xpt4) - xpt0
				lly = min(ypt1, ypt2, ypt3, ypt4) - ypt0
				urx = max(xpt1, xpt2, xpt3, xpt4) - xpt0
				ury = max(ypt1, ypt2, ypt3, ypt4) - ypt0

				m = Basemap(projection = 'ortho', lon_0 = lon_0, lat_0 = lat_0, resolution = 'l', llcrnrx = llx, llcrnry = lly, urcrnrx = urx, urcrnry = ury)
				lon = mod03_lon_data
				lat = mod03_lat_data
				x_igrid, y_igrid = m(lon, lat)
				x_igrid = x_igrid - xpt0
				y_igrid = y_igrid - ypt0
				#mod06_sds_data = mod06_sds.get()
				#print mod06_sds_data.dtype
				#print mod06_sds_data.shape
				sds_data = mod35_sds.get()
				sds_data_0 = sds_data[0, :, :]
				sds_data_0_bin = sds_data_0.astype(dtype = np.uint8, order = 'K', casting = 'unsafe', subok = False, copy = False)

				for x in np.nditer(sds_data_0_bin, op_flags = ['readwrite']):
					x[...] = np.right_shift(x, 6)

				for y in np.nditer(sds_data_0_bin, op_flags = ['readwrite']):
					if (y[...] == 3 or y[...] == 2):
						y[...] = 0

				#sds_data_0_bin_int16 =  sds_data_0_bin.astype(dtype = np.int16, order = 'K', casting = 'unsafe', subok = False, copy = False)
				z_igrid = sds_data_0_bin
				#print z_igrid[0,0]

				#for i in np.nditer(sds_data_0_bin_int16, op_flags = ['readwrite']):
				#	for j in np.nditer(mod06_sds_data):
				#		k = j
				#	if (i[...] == 0):
				#		i[...] = k
				#	print i
				x1_igrid = x_igrid.ravel()
				y1_igrid = y_igrid.ravel()
				#z1_igrid = z_igrid.ravel()
				xy1_igrid = np.vstack((x1_igrid, y1_igrid)).T
				cmap = plt.cm.gnuplot2
				bounds = np.arange(0, 2, 1)
				norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
				img = m.imshow(np.flipud(z_igrid), origin = 'lower', vmin = 0.0, vmax = 1.0, cmap = cmap)
				#m.drawcoastlines()
				m.drawparallels(np.arange(-90.,120.,5.), color='w', labels=[True,False,False,False])
				m.drawmeridians(np.arange(115.,360.,5.), color='w', labels=[False,False,False,True])


				plt.title("MAP")
				plt.show()
			elif(_filename == ""):
				mbox.showerror("Error", "Input MOD35 (Cloud Mask) file!")
			elif(_filename_geo == ""):
				mbox.showerror("Error", "Input MOD03 (Geolocation) file!")


#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

app = modisApp()
app.geometry('800x600')
app.mainloop()