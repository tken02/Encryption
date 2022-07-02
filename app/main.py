import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import sig as digitalsign
from tkinter import messagebox

global pubK, priK
pubK,priK= digitalsign.generate_key()
LARGEFONT =("Verdana", 15)

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (SignPage, VerifyPage):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(SignPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage

class SignPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		# label of frame Layout 2
		l1 = ttk.Label(self,text='Upload File & sign',width=30,font=LARGEFONT)  
		l1.grid(row=1,column=3)
		b1 = tk.Button(self, text='Upload File', 
		width=20,command = lambda:upload_file())
		b1.grid(row=2,column=1) 
		button1 = ttk.Button(self, text ="VerifyPage",
		command = lambda : controller.show_frame(VerifyPage))
	
		# putting the button in its place
		# by using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)
		def upload_file():
			print(pubK)

			file = filedialog.askopenfilename()
			# print(file)
			if digitalsign.signSHA256(file,priK):
				messagebox.showinfo("showinfo", "Success")
			else:
				messagebox.showerror("showerror", "Error")

	
        


		


# second window frame page1
class VerifyPage(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)

		l1 = ttk.Label(self,text='Upload File & verify',width=30,font=LARGEFONT)  
		l1.grid(row=1,column=3)
		b1 = tk.Button(self, text='Upload File', 
		width=20,command = lambda:upload_file())
		b1.grid(row=2,column=1)

		b2 = tk.Button(self, text='Upload sign file', 
		width=20,command = lambda:upload_signfile())
		b2.grid(row=3,column=1)

		global filepath
		filepath = tk.StringVar()
		global signpath
		signpath = tk.StringVar() 

		def upload_file():
			filename = filedialog.askopenfilename()
			filepath.set(filename)
		def upload_signfile():
			signname = filedialog.askopenfilename()
			signpath.set(signname)

		b3 = tk.Button(self, text='Verify', 
		width=20,command = lambda:verify())
		b3.grid(row=4,column=1)
		def verify():
			print(pubK)
			# print(filepath.get(),signpath.get())
			verified, user =digitalsign.verifySign(filepath.get(),signpath.get(),pubK)
			if verified:
				messagebox.showinfo("showinfo", "Success, user veirifed is " + user)
			else:
				messagebox.showerror("Error", "the find not match for any user")

		

		l2 = ttk.Label(self,textvariable=filepath)  
		l2.grid(row=2,column=2)
		l3 = ttk.Label(self,textvariable=signpath)  
		l3.grid(row=3,column=2)
		button1 = ttk.Button(self, text ="SignPage",
							command = lambda : controller.show_frame(SignPage))
	
		# putting the button in its place
		# by using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		



# Driver Code
app = tkinterApp()
app.mainloop()
