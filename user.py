from cProfile import Profile
from concurrent.futures import process
from tkinter import *
import tkinter.messagebox as messagebox
from functools import partial
from tokenize import String
from tkinter import filedialog as fd
from tkinter import filedialog
from tkinter.messagebox import showinfo
from app import sig as digitalsign
import FunctionSQL as s
import db_connect as db
global root
LARGEFONT =("Verdana", 15)

def loginForm():
    global  LoginFrame, lbl_result1
    global email, password
    global email1, password1, name, birthday, phone, address
    global email2, password2, name2, birthday2, phone2, address2
    global from_Name, file_Send
    
    from_Name = StringVar()
    file_Send = StringVar()
    
    email = StringVar()
    name = StringVar()
    birthday = StringVar()
    phone = StringVar()
    address = StringVar()
    password = StringVar()
    
    email1 = StringVar()
    password1 = StringVar()

    email2 = StringVar()
    name2 = StringVar()
    birthday2 = StringVar()
    phone2 = StringVar()
    address2 = StringVar()
    password2 = StringVar()
    
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP,pady= 80)
    
    usernameLabel = Label(LoginFrame, text="Email:",font= 12).grid(row=0, column=0)
    usernameEntry = Entry(LoginFrame, textvariable=email,font= 12).grid(row=0, column=1)  
    
    #password label and password entry box
    passwordLabel = Label(LoginFrame,text="Password:",font= 12).grid(row=2, column=0)  
    passwordEntry = Entry(LoginFrame, textvariable=password,show='*',font= 12).grid(row=2, column=1)
    
    #login button
    lbl_result1 = Label(LoginFrame, text="", font=('arial', 11))
    lbl_result1.grid(row=4, columnspan=3)
    loginButton = Button(LoginFrame, text="Login", command=validateLogin,font= 12).grid(row=5, column=1)
    
    lbl_register = Label(LoginFrame, text="Register", fg="Blue", font=('arial', 12))
    lbl_register.grid(row=6,column=1)
    lbl_register.bind('<Button-1>', toRegister)

def RegisterForm():
    global RegisterFrame, lbl_result3,  lbl_result2
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP, pady=40)
    list_infor = ["Email:","Name:","Brithday:","Phone:","Address:","Password:"]
    for i in range(len(list_infor)):
        tem = Label(RegisterFrame, text=list_infor[i], font=('arial', 12), bd=12)
        tem.grid(row=i+1)
    
    lbl_result2 = Label(RegisterFrame, text="", font=('arial',12))
    lbl_result2.grid(row=7, columnspan=2)
    
    lbl_result3 = Label(RegisterFrame, text="", font=('arial',12))
    lbl_result3.grid(row=7, column=2)
    
    Entryusername = Entry(RegisterFrame, font=('arial', 12),textvariable=email1, width=15)
    Entryusername.grid(row=1, column=1)
    
    Entrypassword = Entry(RegisterFrame, font=('arial', 12), textvariable=name, width=15, show="*")
    Entrypassword.grid(row=2, column=1)
    
    Entryfirstname = Entry(RegisterFrame, font=('arial', 12), textvariable=birthday, width=15)
    Entryfirstname.grid(row=3, column=1)
    
    Entrylastname = Entry(RegisterFrame, font=('arial', 12), textvariable=phone, width=15)
    Entrylastname.grid(row=4, column=1)
    
    Entrylastname = Entry(RegisterFrame, font=('arial', 12), textvariable=address, width=15)
    Entrylastname.grid(row=5, column=1)
    
    Entrylastname = Entry(RegisterFrame, font=('arial', 12), textvariable=password1, width=15)
    Entrylastname.grid(row=6, column=1)
    
    btn_login = Button(RegisterFrame, text="Register", font=('arial', 12), width=35, command=Register)
    btn_login.grid(row=7, columnspan=2, pady=20)
    
    lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', toLogin)
    
def HomeForm():
    global  HomeFrame,list_box,fileNames
    name = "khanh"
    HomeFrame = Frame(root)
    HomeFrame.pack(side=TOP,pady= 80)
    
    filename_lasname = Label(HomeFrame, text=name ,font= 12).grid(row=0, column=0)
    
    lbl_edit = Label(HomeFrame, text="Edit_Information", fg="Blue", font=('arial',10))
    lbl_edit.grid(row=1,column=0)
    lbl_edit.bind('<Button-1>', toEdit)
    
    l2 = Label(HomeFrame, text="SignDigital & VeriFy", fg="Blue", font=('arial',10))
    l2.grid(row=2,column=0)
    l2.bind('<Button-1>', ToSignDigital)
        
    usename_reciver = Label(HomeFrame, text="To email:", font=('arial', 12))
    usename_reciver.grid(row=0,column=2)
    
    
    Entry_reciver = Entry(HomeFrame, font=('arial', 12),textvariable=from_Name, width=15)
    Entry_reciver.grid(row=0, column=3)
    
    open_button = Button(HomeFrame,text='Open Files',command=select_files).grid(row=1,column=2)
    
    my_file = Label(HomeFrame,text="My File",fg="Red",font= 11)
    my_file.grid(row=7,column=2)
    
    list_box = Listbox(HomeFrame)
    list_box.grid(row=8,column=2)
    list_NAME = ["1","2"]
    for i in list_NAME:
        list_box.insert(END,i)
    button_open = Button(HomeFrame,text="open",command=ProcessOpen,font= 8).grid(row=8,column=3)
      
def EditForm():
    global EditFrame
    EditFrame = Frame(root)
    EditFrame.pack(side=TOP, pady=40)
    list_infor = ["Name:","Brithday:","Phone:","Address:","Password:"]
    for i in range(len(list_infor)):
        tem = Label(EditFrame, text=list_infor[i], font=('arial', 12), bd=12)
        tem.grid(row=i+1)
    
    
    Entrypassword = Entry(EditFrame, font=('arial', 12), textvariable=name2, width=15, show="*")
    Entrypassword.grid(row=1, column=1)
    
    Entryfirstname = Entry(EditFrame, font=('arial', 12), textvariable=birthday2, width=15)
    Entryfirstname.grid(row=2, column=1)
    
    Entrylastname = Entry(EditFrame, font=('arial', 12), textvariable=phone2, width=15)
    Entrylastname.grid(row=3, column=1)
    
    Entrylastname = Entry(EditFrame, font=('arial', 12), textvariable=address2, width=15)
    Entrylastname.grid(row=4, column=1)
    
    Entrylastname = Entry(EditFrame, font=('arial', 12), textvariable=password2, width=15)
    Entrylastname.grid(row=5, column=1)
    
    btn_login = Button(EditFrame, text="save", font=('arial', 12), width=35, command=processUpdateInformation)
    btn_login.grid(row=6, columnspan=2, pady=20)
    
    lbl_login = Label(EditFrame, text="Home", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', ToHome)

def SignDigtalForm():
    global SignDigtalFrame,priK
    SignDigtalFrame = Frame(root)
    SignDigtalFrame.pack(side=TOP, pady=40)
    
    l1 = Label(SignDigtalFrame,text='Upload File & sign',width=30,font=LARGEFONT)  
    l1.grid(row=1,column=3)
    b1 = Button(SignDigtalFrame, text='Upload File', 
    width=20,command = lambda:upload_file())
    b1.grid(row=2,column=1) 
    button1 = Button(SignDigtalFrame, text ="VerifyPage",
    command = lambda : ToVerifilePage())
    def ToVerifilePage():
        SignDigtalFrame.destroy()
        VerifyFrom()
    # putting the button in its place
    # by using grid
    button1.grid(row = 1, column = 1, padx = 10, pady = 10)
    def upload_file():
        file = filedialog.askopenfilename()
        # print(file)
        if digitalsign.signSHA256(file,priK):
            messagebox.showinfo("showinfo", "Success")
        else:
            messagebox.showerror("showerror", "Error")

def VerifyFrom():
    global VerifyFrame,pubK
    VerifyFrame = Frame(root)
    VerifyFrame.pack(side=TOP, pady=40)
    l1 = Label(VerifyFrame,text='Upload File & verify',width=30,font=LARGEFONT)  
    l1.grid(row=1,column=3)
    b1 = Button(VerifyFrame, text='Upload File', 
    width=20,command = lambda:upload_file())
    b1.grid(row=2,column=1)

    b2 = Button(VerifyFrame, text='Upload sign file', 
    width=20,command = lambda:upload_signfile())
    b2.grid(row=3,column=1)

    global filepath
    filepath = StringVar()
    global signpath
    signpath = StringVar() 

    def upload_file():
        filename = filedialog.askopenfilename()
        filepath.set(filename)
    def upload_signfile():
        signname = filedialog.askopenfilename()
        signpath.set(signname)

    b3 = Button(VerifyFrame, text='Verify', 
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

    

    l2 = Label(VerifyFrame,textvariable=filepath)  
    l2.grid(row=2,column=2)
    l3 = Label(VerifyFrame,textvariable=signpath)  
    l3.grid(row=3,column=2)
    button1 = Button(VerifyFrame, text ="SignPage",
                        command = lambda : toSignPage())
    def toSignPage():
        VerifyFrame.destroy()
        SignDigtalForm()
    # putting the button in its place
    # by using grid
    button1.grid(row = 1, column = 1, padx = 10, pady = 10)
    
#process
def select_files():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message=filenames
    )
    
def processUpdateInformation():

    n = name2.get()
    pws = password2.get()
    b = birthday2.get()
    ph =  phone2.get()
    add = address2.get()
    

def ProcessOpen():
    filename = list_box.get(ANCHOR)
    print(filename)
    
    
def Register():
    n = name.get()
    b = birthday.get()
    ph = phone.get()
    add = address.get()
    p = password1.get()
    if(len(p) > 16 or len(p) == 0):
        lbl_result3.config(text="false", fg="blue")
        
    else:
        lbl_result3.config(text="true", fg="blue")

def validateLogin():
    u = email.get()
    p = password.get()
    if u == "admin" and p == "admin":
        lbl_result1.config(text="You Successfully Login", fg="blue")
        LoginFrame.destroy()
        HomeForm()
    else:
        lbl_result1.config(text=" Invalid e-mail or password. ", fg="red")
        
#move frame
def ToHome(event =None):
    EditFrame.destroy()
    HomeForm()

def toLogin(event = None):
    RegisterFrame.destroy()
    loginForm()
    

def toRegister(event = None):
    LoginFrame.destroy()
    RegisterForm()

def toEdit(event = None):
    HomeFrame.destroy()
    EditForm()

def ToSignDigital(event = None):
        HomeFrame.destroy()
        SignDigtalForm()

if __name__ == "__main__":
    root = Tk() 
    root.title('Login Form')
    root.geometry('900x500')
    loginForm()
    root.mainloop()
    
    