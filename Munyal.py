from Tkinter import *
import string
from ftplib import FTP

def main():
	ventana=Tk()
	User=StringVar()
	password=StringVar()
	IP=StringVar()
	ventana.geometry("200x300")
	ventana.title("Munyal")
	entryUser=Entry(login,textvar=User)
	entrypassword=Entry(login,textvar=password)
	entryIP=Entry(login,textvar=varIP)
	User.set("")
	password.set("")
	IP.set("")
	ventana.mainloop()
	return 0

if '_name_ '== '_main_':
	main()

