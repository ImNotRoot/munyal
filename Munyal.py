from Tkinter import *
import string
from ftplib import FTP

def main():
	ventana=Tk()
	img=PhotoImage(file="os.gif")
	c=Canvas(ventana,width=50, height=50)
	ventana.geometry("300x400")
	ventana.title("MUNYAL")
	user=StringVar()
	password=StringVar()
	ip=StringVar()
	l=Label(ventana,text="MUNYAL")
	logo=c.create_image(image=img) 
	c.pack(side=TOP)
	l.pack(side=TOP)
	label1=Label(ventana,text="Use:")
	label1.pack(side=TOP)
	entryuser=Entry(ventana,textvar=user)
	entryuser.pack(side=TOP)
	label2=Label(ventana,text='password:')
	label2.pack(side=TOP)
	entrypassword=Entry(ventana,textvar=password)
	entrypassword.pack(side=TOP)
	label3=Label(ventana,text='IP')
	label3.pack(side=TOP)
	entryip=Entry(ventana,text="ip")
	entryip.pack(side=TOP)
	boton=Button(ventana,text="iniciar", relief=SOLID)
	boton.pack(side=TOP)
	ventana.mainloop()
	return 0
if __name__ == '__main__':
	main()
