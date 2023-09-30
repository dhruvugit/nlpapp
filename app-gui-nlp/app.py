from tkinter import *
from mydb import Database
from tkinter import messagebox #this helps to print that registraion wala succesfull and alreay exist



#se sab kuch aa gya jo bhi tkinter mein hai 

class NLPapp:
  def __init__(self):

    self.dbo = Database() #dbo is object of Ddatabase, added self becoz we may use dbo again somewhere else



    self.root=Tk() #Tk() is an main and impportant objecct of tkinter, GUI banta hai es se, TK is as class uska objedct bannn rha hai #root is variable of NLP class 
    self.root.title("NLPApp")               
    self.root.iconbitmap('resources/favicon2.ico')
    self.root.geometry('350x600')
    self.root.configure(bg='light green')
    self.login_gui()
    self.root.mainloop() #this helps to hold gui until closed by user

  def login_gui(self):
    self.clear()
    heading = Label(self.root, text = "Welcome to NLP App", font=("Arial", 20, 'bold'), bg='light green', fg='white')#ye bs hume define kiya hai we have to explcitly tell ki show it, using heading.pack
    heading.pack(pady=(30,30))#30,30 is gap from up and down side just like padding

    label1 = Label(self.root, text='Enter Email')
    label1.pack(pady=(10,10))

    self.email_input = Entry(self.root, width=50)#Entry class is used to add text box
    self.email_input.pack(pady=(5,5), ipady=4) #eske liye self use kar rhe hain bcoz this will be used by oyher members too but heading label ko sirf login_gui class use karega

    label2 = Label(self.root, text='Enter Password')
    label2.pack(pady=(10,10))

    self.password_input = Entry(self.root, width=50, show='*')#Entry class is used to add text box
    self.password_input.pack(pady=(5,5), ipady=4)

    #Classes used till now : label , entry 
    #Now add button class
    #self agar nhi lga rhe mtlb hum usko class variable nnhi bna re use koi aur use nhi karega
    #we can give heaight to button but not in input waala jagh

    login_btn = Button(self.root, text='Login', width=30, height=2, command=self.perform_login)
    login_btn.pack(pady=(10,10))


    label3 = Label(self.root, text='Not a Member?')
    label3.pack(pady=(20,10))

    redirect_btn = Button(self.root, text='Register Now', width=30, height=2, command=self.register_gui)
    #command paramter kehta hai jab bhi koi es button pr click kare ye fucn chala do...here we have register_gui
    redirect_btn.pack(pady=(10,10))#command se es button ko click karne pr control register_gui ko chala jaega

  def register_gui(self):
    self.clear()

    heading = Label(self.root, text = "Welcome to NLP App", font=("Arial", 20, 'bold'), bg='light green', fg='white')
    heading.pack(pady=(30,30))

    label0 = Label(self.root, text='Enter Name')
    label0.pack(pady=(10,10))

    self.name_input = Entry(self.root, width=50)
    self.name_input.pack(pady=(5,5), ipady=4) 

    label1 = Label(self.root, text='Enter Email')
    label1.pack(pady=(10,10))

    self.email_input = Entry(self.root, width=50)
    self.email_input.pack(pady=(5,5), ipady=4) 

    label2 = Label(self.root, text='Enter Password')
    label2.pack(pady=(10,10))

    self.password_input = Entry(self.root, width=50, show='*')
    self.password_input.pack(pady=(5,5), ipady=4)

    register_btn = Button(self.root, text='Register', width=30, height=2, command=self.perform_registration)
    register_btn.pack(pady=(10,10))


    label3 = Label(self.root, text='Already a Member?')
    label3.pack(pady=(20,10))

    redirect_btn = Button(self.root, text='Login Now', width=30, height=2, command=self.login_gui)
    redirect_btn.pack(pady=(10,10))
  

  def perform_registration(self):
    name = self.name_input.get()#here get func will fetch what user will give and store in var "name"
    email = self.email_input.get()
    password = self.password_input.get()
    response = self.dbo.add_data(name, email, password)
    if response:
      messagebox.showinfo('Success', 'Registration Successful You can Login Now')
    else:
      messagebox.showerror('Error', 'Email already exist')



  def perform_login(self):
    email = self.email_input.get()
    password = self.password_input.get()

    response = self.dbo.search(email, password)
    if response:
      messagebox.showinfo('Success','Login Successful')
      self.home_gui()
    else:
      messagebox.showerror('Error', 'Incorrect Email/Password!')


  def home_gui(self):
    self.clear()

    heading = Label(self.root, text = "Welcome to NLP App", font=("Arial", 20, 'bold'), bg='light green', fg='white')
    heading.pack(pady=(30,30))

    sentiment_btn = Button(self.root, text='Sentiment Analysis', width=35, height=5, command=self.sentiment_gui)
    sentiment_btn.pack(pady=(10,10))

    ner_btn = Button(self.root, text='Named Entity Recognition', width=35, height=5, command=self.perform_registration)
    ner_btn.pack(pady=(10,10)) 
    
    emotion_btn = Button(self.root, text='Emotion Analysis', width=35, height=5, command=self.perform_registration)
    emotion_btn.pack(pady=(10,10))

    logout_btn = Button(self.root, text='Log Out', width=30, height=2, command=self.login_gui)
    logout_btn.pack(pady=(10,10))
    


  def sentiment_gui(self):

    self.clear()

    heading = Label(self.root, text = "Welcome to NLP App", font=("Arial", 20, 'bold'), bg='light green', fg='white')
    heading.pack(pady=(30,30))

    heading2 = Label(self.root, text = "Sentiment Analysis", font=("Arial", 13), bg='light green', fg='white')
    heading2.pack(pady=(30,30))

    label1 = Label(self.root, text='Enter Text')
    label1.pack(pady=(10,10))
    
    self.sentiment_input = Entry(self.root, width=50)
    self.sentiment_input.pack(pady=(5,5), ipady=4) 

    sentiment_btn = Button(self.root, text='Analyse Sentiment', width=30, height=2, command=self.login_gui)
    sentiment_btn.pack(pady=(10,10))
   
    goback_btn = Button(self.root, text='Go Back', width=30, height=2, command=self.home_gui)
    goback_btn.pack(pady=(10,10))
    #at this point we need to clear escisting gui i.e of login gui
  def clear(self):
    for i in self.root.pack_slaves():
      i.destroy()
    

#pack_slaves : this helps to list all the pack of slaves, you can explore more by printing it, but it conains all the things we did earlier and on loop we will distroy each one to clean the screen 
#clear baar baar kaam ayega usko ftn bna diya
    
    
    


nlp=NLPapp()    
