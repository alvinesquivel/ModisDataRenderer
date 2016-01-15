#!/usr/bin/python27
import Tkinter as tk


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

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()


class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)

		label = tk.Label(self, text="Input", font=L_FONT)
		label.grid(row=0,column=0)
#LABELS
		label1 = tk.Label(self, text="MOD06 Cloud Properties", font=M_FONT)
		label1.grid(row=2,column=0)

		label2 = tk.Label(self, text="MOD35 Cloud Mask", font=M_FONT)
		label2.grid(row=4,column=0)

		label3 = tk.Label(self, text="MOD03 Geolocation", font=M_FONT)
		label3.grid(row=6,column=0)


							#	.grid() layout manager ignores empty rows and columns
							#	left an empty row between the 3 labels for easier adjusting in the future


#TEXT ENTRY
		entrybox1 = tk.Entry(self, text="choose file")
		entrybox1.grid()

#BUTTONS

		button = tk.Button(self, text="Check (moves to pageone AtTheMoment)",
							command=lambda: controller.show_frame(PageOne)) #lambda overrides run at creation behavior, see examples online
		button.grid()

		button2 = tk.Button(self, text="Next (moves to pagetwo AtTheMoment)",
							command=lambda: controller.show_frame(PageTwo))
		button2.grid()


class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page One!!!", font=L_FONT)
		label.pack(pady=10,padx=10)

		button1 = tk.Button(self, text="Back to Home",
							command=lambda: controller.show_frame(StartPage))
		button1.pack()

		button2 = tk.Button(self, text="Page Two",
							command=lambda: controller.show_frame(PageTwo))
		button2.pack()


class PageTwo(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page Two!!!", font=L_FONT)
		label.pack(pady=10,padx=10)

		button1 = tk.Button(self, text="Back to Home",
							command=lambda: controller.show_frame(StartPage))
		button1.pack()

		button2 = tk.Button(self, text="Page One",
							command=lambda: controller.show_frame(PageOne))
		button2.pack()



app = modisApp()
app.mainloop()