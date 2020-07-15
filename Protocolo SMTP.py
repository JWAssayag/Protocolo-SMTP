# -- coding: cp1252 --
import tkinter
from tkinter import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import tkinter.constants, tkinter.filedialog

class Tela:
    def __init__(self,master):
        self.frm1= Frame(master)
        self.ent= Entry(self.frm1,width=33,font=('Arial',15))
        self.lblUsername= Label(self.frm1,text='Username:',font=('Arial',15,'bold'),fg='black')
        self.lblPassword= Label(self.frm1,text='Password:',font=('Arial',15,'bold'),fg='black')
        self.ent2= Entry(self.frm1,width=33,show='*',font=('Arial',15))
        self.mlblError= Label(self.frm1,text='Password or Username was incorrect. Try again!',font=('Arial',13),fg='red')
        self.btn= Button(self.frm1,command=self.click,text='Enter',font=('Arial',14,'bold'),fg='blue')
        self.lblUsername.pack()
        self.ent.pack()
        self.lblPassword.pack()
        self.ent2.pack()
        self.btn.pack()
        self.frm1.pack()
        self.frm2= Frame(master)
        self.lblTo = Label(self.frm2,text = 'To:',font = ('Arial',13),width=6 ,fg = 'blue')
        self.entTo = Entry(self.frm2,width=45,font = ('Arial',13))
        self.lblSubject = Label(self.frm2,text = 'Subject:',font = ('Arial',13),fg = 'blue')
        self.entSubject = Entry(self.frm2,width=45,font = ('Arial',13))
        self.lblMgs = Label(self.frm2,text='Message:',font = ('Arial',13),fg = 'blue')
        self.myText_Box = Text(self.frm2)
        self.btnSend= Button(self.frm2,command=self.click2,text = 'Send',font = ('Arial',15),fg='blue')
        self.lblArq= Label(self.frm2,text='Put your mail list here:',font = ('Arial',13),fg='blue')
        self.btnArq= Button(self.frm2,command=self.Arq,text='Open list',font = ('Arial',15),fg='blue') 
        self.lblErrorTO= Label(self.frm2,text='Please, enter the email of who you want to send the message!',font = ('Arial',13),fg='red') 
        self.lblTo.pack()
        self.entTo.pack()
        self.lblArq.pack()
        self.btnArq.pack()
        self.lblSubject.pack()
        self.entSubject.pack()
        self.lblMgs.pack()
        self.myText_Box.pack()
        self.btnSend.pack()
       

    def click(self):
        self.frm1.pack_forget()
        user= self.ent.get()
        pasw= self.ent2.get()
        if ('@gmail.com' in user):
            server= smtplib.SMTP('smtp.gmail.com:587')
        else:
            ('@outlook.com'or'@hotmail.com' in user)
            server= smtplib.SMTP('smtp.live.com:587')
        server.starttls()
        try:
            server.login(user,pasw)
            ret = True
        except:
            ret= False
        server.quit()
        if ret is not True:
            self.mlblError.pack(side= BOTTOM)
            self.frm1.pack()
        else:
            self.frm2.pack()
            root.geometry('800x700')
            
    def Arq(self):
        top= Toplevel()
        root.filename = tkinter.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files",".jpg"),("all files","."),("txt files",".txt"))) 
        to= root.filename
        str = to
        aki=open(to)
        emails= aki.read().splitlines()
        aki.close()
        csv_values = ','.join(emails)
        self.entTo.delete(0,END)
        self.entTo.insert(0,csv_values)
        
    def click2(self):
        msg = MIMEMultipart()
        message = self.myText_Box.get('1.0',END)
        password = self.ent2.get()
        msg['From'] = self.ent.get()
        msg['To'] = self.entTo.get()
        if len(self.entTo.get()) == 0:
            self.lblErrorTO.pack(side= TOP)
            self.frm2.pack()
        else:
            msg['Subject'] = self.entSubject.get()
            msg.attach(MIMEText(message, 'plain'))
            if ('@gmail.com' in msg['From']):
                server= smtplib.SMTP('smtp.gmail.com:587') 
            else:
                ('@outlook.com'or'@hotmail.com' in msg['From'])
                server= smtplib.SMTP('smtp.live.com:587') 
            server.starttls()
            server.login(msg['From'], password)
            server.sendmail(msg['From'], msg['To'].split(','), msg.as_string())    
            server.quit()
            top= Toplevel()
            label= Label(top,text='successfully sent email to %s' % (msg['To']),font=('Arial',14,'bold'),fg='blue')
            label.pack() 

        
root= Tk()
root.title("@SMTP.com")
root.geometry('500x190')
app= Tela(root)
root.mainloop()
