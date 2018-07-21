import tkinter as tk
from tkinter import messagebox
import engine as engine
import os

class App(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		
		self.title("Teknomo's Chatbot")
		wdir=os.path.dirname(os.path.realpath(__file__))
		os.chdir(wdir)
		
		self.iconbitmap(r''+wdir+"\\"+'chatbot.ico')
		w = 400 # width for the Tk root
		h = 350 # height for the Tk root

		# get screen width and height
		ws = self.winfo_screenwidth() # width of the screen
		hs = self.winfo_screenheight() # height of the screen

		# calculate x and y coordinates for the Tk root window
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)

		# set the dimensions of the screen and where it is placed
		self.geometry('%dx%d+%d+%d' % (w, h, x, y))
		
		# set private variables
		self.conversation=""
		self.bot = engine.Chatbot()

		# set widgets
		# self.frame=tk.Frame(self)
		# self.frame.pack()
		self.textconversation=tk.Text(self, height=15, width=30,
                                     borderwidth=0, highlightthickness=0, wrap=tk.WORD)
		self.textconversation['font'] = ('consolas', '12')
		# self.textconversation['rmargin']='1'
		self.textconversation.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=(0, 18))
		self.scrollbar = tk.Scrollbar(self,
		                              orient='vertical',
		                              command=self.textconversation.yview)		
		self.scrollbar.grid(row=0, column=3,columnspan=1, sticky='nse')
		self.textconversation['yscrollcommand']=self.scrollbar.set
		
		self.content = tk.StringVar()
		self.textentry=tk.Entry(self,textvariable=self.content)
		self.textentry.bind("<Return>", self.Clicked)
		self.textentry.grid(row=1, column=0, columnspan=3, sticky='nsew')
		self.textentry.focus_set()

		self.button = tk.Button(self, text='Enter')
		self.button.bind("<Button-1>", self.Clicked)
		self.button.grid(row=1, column=3, columnspan=1, sticky='nsew')
		
		# make the widgets resizeable with windows
		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)
		self.grid_columnconfigure(3,weight=1)
		self.grid_rowconfigure(0,weight=1)
		self.grid_rowconfigure(1,weight=1)
	
	def Clicked(self, event):
	    text=self.content.get()
	    respond=self.bot.respond(text)
	    self.conversation=\
	    	"you: " + text + "\n" + \
	    	"bot: " + respond + "\n"
	    self.content.set(text)
	    self.textconversation.insert(tk.END,self.conversation)
	    self.textconversation.see(tk.END)
	    self.textentry.delete(0,tk.END)
	    
	def on_closing(self):
		if messagebox.askokcancel("Quit", "Do you want to quit?"):
			text=self.textconversation.get("1.0","end-1c")
			self.bot.saveConversation(text)
			self.destroy()


if __name__ == "__main__":
    app=App()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()