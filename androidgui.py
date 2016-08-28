#import relevant libraries, tkinter is gui
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
#a dictionary containing all info about each version
version = {
		"1.0": ["Alpha", "September 23, 2008", [], "1"],
		"1.1": ["Beta", "February 9, 2009", [], "2"],
		"1.5": ["Cupcake", "April 27, 2009", [], "3"],
		"1.6": ["Donut", "September 15, 2009", [], "4"],
		"2.0": ["Eclair", "October 26, 2009", ["2.0.1", "2.1"], "5"],
		"2.0.1": ["Eclair", "December 3, 2009", [], "6"],
		"2.1": ["Eclair", "January 12, 2010", [], "7"],
		"2.2": ["Froyo", "May 20, 2010", ["2.2.1", "2.2.2", "2.2.3"], "8"],
		"2.2.1": ["Froyo", "January 18, 2011", [], "8"],
		"2.2.2": ["Froyo", "January 22, 2011", [], "8"],
		"2.2.3": ["Froyo", "November 21, 2011", [], "8"],
		"2.3": ["Gingerbread", "December 6, 2010", ["2.3.1", "2.3.2", "2.3.3", "2.3.4", "2.3.5", "2.3.6", "2.3.7"], "9"],
		"2.3.1": ["Gingerbread", "December 2010", [], "9"],
		"2.3.2": ["Gingerbread", "February 9, 2011", [], "10"],
		"2.3.3": ["Gingerbread", "February 9, 2011", [], "10"],
		"2.3.4": ["Gingerbread", "April 28, 2011", [], "10"],
		"2.3.5": ["Gingerbread", "July 25, 2011", [], "10"],
		"2.3.6": ["Gingerbread", "September 2, 2011", [], "10"],
		"2.3.7": ["Gingerbread", "September 21, 2011", [], "10"],
		"3.0": ["Honeycomb", "February 22, 2011", ["3.1", "3.2", "3.2.1", "3.2.2", "3.2.3", "3.2.4", "3.2.5", "3.2.6"], "11"],
		"3.1": ["Honeycomb", "May 10, 2011", [], "12"],
		"3.2": ["Honeycomb", "July 15, 2011", ["3.2.1", "3.2.2", "3.2.3", "3.2.4", "3.2.5", "3.2.6"], "13"],
		"3.2.1": ["Honeycomb", "September 20, 2011", [], "13"],
		"3.2.2": ["Honeycomb", "August 30, 2011", [], "13"],
		"3.2.3": ["Honeycomb", "unknown", [], "13"],
		"3.2.4": ["Honeycomb", "December 2011", [], "13"],
		"3.2.5": ["Honeycomb", "January 2012", [], "13"],
		"3.2.6": ["Honeycomb", "February 2012", [], "13"],
		"4.0": ["Ice Cream Sandwich", "October 18, 2011", ["4.0.1", "4.0.2", "4.0.3", "4.0.4"], "14"],
		"4.0.1": ["Ice Cream Sandwich", "October 21, 2011", [], "14"],
		"4.0.2": ["Ice Cream Sandwich", "November 28, 2011", [], "14"],
		"4.0.3": ["Ice Cream Sandwich", "December 16, 2011", [], "15"],
		"4.0.4": ["Ice Cream Sandwich", "March 29, 2012", [], "15"],
		"4.1": ["Jelly Bean", "July 9, 2012", ["4.1.1", "4.1.2", "4.2", "4.2.1", "4.2.2", "4.3", "4.3.1"], "16"],
		"4.1.1": ["Jelly Bean", "July 11, 2012", [], "16"],
		"4.1.2": ["Jelly Bean", "October 9, 2012", [], "16"],
		"4.2": ["Jelly Bean", "November 13, 2012", [], "17"],
		"4.2.1": ["Jelly Bean", "November 27, 2012", [], "17"],
		"4.2.2": ["Jelly Bean", "February 11, 2013", [], "17"],
		"4.3": ["Jelly Bean", "July 24, 2013", [], "18"],
		"4.3.1": ["Jelly Bean", "October 3, 2013", [], "18"],
		"4.4": ["KitKat", "October 31, 2013", ["4.4.1", "4.4.2", "4.4.3", "4.4.4"], "19"],
		"4.4.1": ["KitKat", "December 5, 2013", [], "19"],
		"4.4.2": ["KitKat", "December 9, 2013", [], "19"],
		"4.4.3": ["KitKat", "June 2, 2014", [], "19"],
		"4.4.4": ["KitKat", "June 19, 2014", [], "19"],
		"5.0": ["Lollipop", "November 12, 2014", ["5.0.1", "5.0.2", "5.1", "5.1.1"], "21-22"],
		"5.0.1": ["Lollipop", "December 2, 2014", [], "21"],
		"5.0.2": ["Lollipop", "December 19, 2014", [], "21"],
		"5.1": ["Lollipop", "March 9, 2015", ["5.1.1"], "22"],
		"5.1.1": ["Lollipop", ],
		"6.0": ["Marshmallow", "October 5, 2015", ["6.0.1"], "23"],
		"6.0.1": ["Marshmallow", "December 7, 2015", [], "23"],
		"7.0": ["Nougat", "Not yet released", [], "24"]
		}
#a class for the statusbar
class StatusBar(tk.Frame):

    def __init__(self, master):
		#the style of the statusbar
        tk.Frame.__init__(self, master)
        self.label = tk.Label(self, bd=1, relief="sunken", anchor="w")
        self.label.pack(fill="x")
		#I don't even know, I copied it from the internet
    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

class Application:


	def __init__(self, master):
		self.master = master

		#styling
		master.title("Android Version Tool")
		master.geometry("444x482")
		master.wm_iconbitmap("android.ico")

		#the tabs for the gui
		self.n = ttk.Notebook(master)
		self.f1 = ttk.Frame(self.n,)
		self.f2 = ttk.Frame(self.n)
		self.f3 = ttk.Frame(self.n)
		self.f4 = ttk.Frame(self.n)

		#naming the tabs
		self.n.add(self.f1, text="Code name")
		self.n.add(self.f2, text="Release date")
		self.n.add(self.f3, text="Minor release")
		self.n.add(self.f4, text="API level")

		#labels to help the user
		self.lbl1 = tk.Label(self.f1, text="Look up the code name of an Android version:")
		self.lbl2 = tk.Label(self.f2, text="Find when an Android version was released:")
		self.lbl3 = tk.Label(self.f3, text="Look up the minor releases of an Android version:")
		self.lbl4 = tk.Label(self.f4, text="Look up the API level for an Android version:")

		#text boxes
		self.ent1 = tk.Entry(self.f1)
		self.ent2 = tk.Entry(self.f2)
		self.ent3 = tk.Entry(self.f3)
		self.ent4 = tk.Entry(self.f4)

		#the output is printed here
		self.ans1 = tk.Label(self.f1)
		self.ans2 = tk.Label(self.f2)
		self.ans3 = tk.Label(self.f3)
		self.ans4 = tk.Label(self.f4)

		#a special section on frame 3: a checkbox to show more info
		self.chkvar = tk.IntVar()
		self.chk = tk.Checkbutton(self.f3, text="Show minor releases", variable=self.chkvar)
		self.chkans = tk.Label(self.f3, text="")

		#adding the items to the gui
		self.n.pack(fill="x")
		self.lbl1.pack()
		self.lbl2.pack()
		self.lbl3.pack()
		self.lbl4.pack()
		self.ent1.pack(pady=10)
		self.ent2.pack(pady=10)
		self.ent3.pack(pady=10)
		self.chk.pack()
		self.ent4.pack(pady=10)
		self.ans1.pack()
		self.ans2.pack()
		self.ans3.pack()
		self.ans4.pack()
		self.chkans.pack()

		#add the statusbar to the gui
		status = StatusBar(master)
		status.pack(side="bottom", fill="x")
		status.set("Ready, type in a number and press enter")

		#TODO: clear out these unused functions
		def not_finished():
			status.set("This button doesn't work at the moment.")
			master.after(1000)
			status.set("Ready")
		def about_window():
			self.newWindow = tk.Toplevel(self.master)
			self.app = About(self.newWindow)
		def help_window():
			self.newWindow = tk.Toplevel(self.master)
			self.app = Help(self.newWindow)

		#copys the text from the anser labels to the clipboard
		def copy_text():
			if self.n.index(self.n.select()) == 0:
				master.clipboard_clear()
				master.clipboard_append(self.ans1.cget("text"))
			elif self.n.index(self.n.select()) == 1:
				master.clipboard_clear()
				master.clipboard_append(self.ans2.cget("text"))
			elif self.n.index(self.n.select()) == 2:
				master.clipboard_clear()
				master.clipboard_append(self.ans3.cget("text"))
				master.clipboard_append("\n" + self.chkans.cget("text"))
			elif self.n.index(self.n.select()) == 3:
				master.clipboard_clear()
				master.clipboard_append(self.ans4.cget("text"))

		#creating the menu:
		menubar = tk.Menu(master)
		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Exit", command=master.quit)
		menubar.add_cascade(label="Window", menu=filemenu)
		editmenu = tk.Menu(menubar, tearoff=0)

		editmenu.add_command(label="Copy result to clipboard", command=copy_text)

		menubar.add_cascade(label="Edit", menu=editmenu)
		helpmenu = tk.Menu(menubar, tearoff=0)
		helpmenu.add_command(label="Help...", command=help_window)
		helpmenu.add_command(label="About...", command=about_window)
		menubar.add_cascade(label="Help", menu=helpmenu)

		master.config(menu=menubar)


		#get the code name by looking it up in the version dictionary
		def get_codename(input):
			if not self.ent1.get() in version:
				#throw an error if version number not in the dictionary
				messagebox.showerror("Error", "Not a valid version number.")
			else:
				#put the result onto the answer label
				self.ans1.config(text="The code name for version number " + str(self.ent1.get()) + " is " + version[self.ent1.get()][0] + ".")

		#get the release date by looking it up in the version dictionary
		def get_releasedate(input):
			if not self.ent2.get() in version:
				#throw an error if version number not in the dictionary
				messagebox.showerror("Error", "Not a valid version number.")
			else:
				#put the result onto the answer label
				self.ans2.config(text="The release date for version number " + str(self.ent2.get()) + " was " + version[self.ent2.get()][1] + ".")

		#get the minor releases of a version by looking it up in the version dictionary
		def get_minorrelease(input):
			if not self.ent3.get() in version:
				#throw an error if version number not in the dictionary
				messagebox.showerror("Error", "Not a valid version number.")
			else:
				#check if the checkbox is ticked
				if self.chkvar.get() == 1:
					#if so, clear the answer label and print out each minor release on a new line
					self.chkans.configure(text="")
					for item in version[self.ent3.get()][2]:
						text = self.chkans.cget("text") + item + "\n"
						self.chkans.configure(text=text)
				else:
					#if not, clear the answer label and print out the result based on whether there are 0 or 1 or more
					self.chkans.configure(text="")
				if len(version[self.ent3.get()][2]) == 0:
					self.ans3.config(text="For version " + str(self.ent3.get()) + " there were no minor releases.")
				elif len(version[self.ent3.get()][2]) == 1:
					self.ans3.config(text="For version " + str(self.ent3.get()) + " there was one minor release.")
				else:
					self.ans3.config(text="For version " + str(self.ent3.get()) + " there were " + str(len(version[self.ent3.get()][2])) + " minor release(s).")

		#get the api level of a version by looking it up in the version dictionary
		def get_apilevel(input):
			if not self.ent4.get() in version:
				#throw an error if version number not in the dictionary
				messagebox.showerror("Error", "Not a valid version number.")
			else:
				#put the result onto the answer label
				self.ans4.config(text="For version " + str(self.ent4.get()) + ", the API level is " + str(version[self.ent4.get()][3]) + ".")

		#work out what to do when enter is pressed. It decides based on the currently opened tab
		def on_return(event):
			if self.n.index(self.n.select()) == 0:
				get_codename(self.ent1.get())
			elif self.n.index(self.n.select()) == 1:
				get_releasedate(self.ent2.get())
			elif self.n.index(self.n.select()) == 2:
				get_minorrelease(self.ent3.get())
			elif self.n.index(self.n.select()) == 3:
				get_apilevel(self.ent4.get())

		#when the enter key is pressed, on_return is run
		master.bind('<Return>', on_return)

#to create an about window
class About:
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.quitButton = tk.Button(self.frame, text = "Close", width = 25, command = self.close_windows)
		self.aboutlbl = tk.Label(self.frame, text = "This was made by Danny", width = 25)
		self.aboutlbl.pack()
		self.quitButton.pack()
		self.frame.pack()
		master.after(10, lambda: master.focus_force())
	def close_windows(self):
		self.master.destroy()

#to create a help window
class Help:
	def __init__(self, master):
		self.master = master
		master.geometry("641x257")
		master.title("Help")
		self.frame = tk.Frame(self.master)
		self.quitButton = tk.Button(self.frame, text = "Close", width = 25, command = self.close_windows)
		self.helplbl = tk.Label(self.frame, text = "Here is a list of Android versions which you can try:\n1.0 , 1.1, 1.5, 1.6,\n2.0, 2.0.1, 2.1 , 2.2, 2.2.1, 2.2.2, 2.2.3, 2.3, 2.3.1, 2.3.2, 2.3.3, 2.3.4, 2.3.5, 2.3.6, 2.3.7, \n3.0, 3.1, 3.2, 3.2.1, 3.2.2, 3.2.3, 3.2.4, 3.2.5, 3.2.6,\n4.0, 4.0.1, 4.0.2, 4.0.3, 4.0.4, 4.1, 4.1.1, 4.1.2, 4.2, 4.2.1, 4.2.2, 4.3, 4.3.1, 4.4, 4.4.1, 4.4.2, 4.4.3, 4.4.4,\n5.0, 5.0.1, 5.0.2, 5.1, 5.1.1,\n6.0, 6.0.1, \n7.0", justify="left")
		self.helplbl.pack()
		self.quitButton.pack()
		self.frame.pack()
		master.after(10, lambda: master.focus_force())
	def close_windows(self):
		self.master.destroy()

#start the application
def main():
	root = tk.Tk()
	app = Application(root)
	root.mainloop()

#start
if __name__ == "__main__":
	main()
