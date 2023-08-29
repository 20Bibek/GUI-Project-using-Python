from tkinter import*
import pymysql

#win is the obj of Tk class
win = Tk()
win.configure (bg = "black")

def login():
	#win2=Tk()
	user = uid.get()
	password = pwd.get()
	#print("user id = ",user," ","password = ",password)

	conobj=pymysql.connect(host="localhost", user="root",password="",port=3306)
	curobj=conobj.cursor()
	curobj.execute('use studentpro;')
	test = f'select * from user where nuid= "{user}" and npwd= "{password}";'

	curobj.execute(test)
	record = curobj.fetchall()
	#print(record)

	if len(record):
			print("Welcome to Home Page")
			win3 = Tk()
			win3.configure (bg = "light green")
				



			def Del():
				win5 = Tk()
				def Delete():
					D = duid.get()
					conobj = pymysql.connect(host = "localhost",user = "root",password = "",port = 3306)
					curobj = conobj.cursor()
					curobj.execute('use studentpro;')
					r = f'delete from user where nuid = "{D}";'
					print("Record deleted from Database")
					curobj.execute(r)
					conobj.commit()
					curobj.close()
					conobj.close()
					win5.destroy()


				win5.title("Delete Student")
				win5.maxsize(height = 700,width = 700)
				win5.minsize(height = 700,width = 700)
				Label(win5,text="Enter User Id",font=("Comic Sans MS",15),fg="white",bg = "black").place(x=60,y=100)

				duid= Entry(win5,font=("arial bold",15),bg="white",fg="black")
				duid.place(x=250,y = 101)
				Button(win5,text=" Delete Student  ",font=("Poor Richard",15),bg="purple",fg="white",command= Delete).place(x=500,y=90)
			def Search():
				
				win4 = Tk()
				def Find():
					F = suid.get()
					conobj=pymysql.connect(host="localhost", user="root",password="",port=3306)
					curobj=conobj.cursor()
					curobj.execute('use studentpro;')
					r=f'select * from user where nuid="{F}";'
					curobj.execute(r)
					record1= curobj.fetchall()
					print(record1)
					curobj.close()
					conobj.close()
					win4.destroy()

				win4.title("Search Student")
				win4.maxsize(height = 700,width = 700)
				win4.minsize(height = 700,width = 700)
				Label(win4,text="Enter User Id",font=("Comic Sans MS",15),fg="white",bg = "black").place(x=60,y=100)

				suid= Entry(win4,font=("arial bold",15),bg="white",fg="black")
				suid.place(x=250,y = 101)
				Button(win4,text="  Search  ",font=("Poor Richard",15),bg="purple",fg="white",command= Find).place(x=500,y=90)
				win4.mainloop()

			def details():
				conobj=pymysql.connect(host="localhost", user="root",password="",port=3306)
				curobj=conobj.cursor()
				curobj.execute('use studentpro;')
				curobj.execute('select * from  user;')
				record= curobj.fetchall()
				for A,B,C,D,E,F in record:
					print(A," ",B," ",C," ",D," ",E," ",F)

			def exit():
				win3.destroy()

			win3.title("Home Page")
			win3.maxsize(height = 700,width = 700)
			win3.minsize(height = 700,width = 700)

			Button(win3, text="Add new Student", bg="purple",fg="white",font=("Comic Sans MS",15),command = NewUser).place(x=70, y=60)
			Button(win3, text="Delete Student", bg="purple",fg="white",font=("Comic Sans MS",15),command = Del).place(x=70, y=120)
			Button(win3, text="Search Student Details", bg="purple",fg="white",font=("Comic Sans MS",15),command=Search).place(x=70, y=180)
			Button(win3, text="All Student Details", bg="purple",fg="white",font=("Comic Sans MS",15),command=details).place(x=70, y=240)
			Button(win3, text="EXIT", bg="black",fg="red",font=("Comic Sans MS",15),command=exit).place(x=300, y=400)

			win3.mainloop()
	else:
			print("try again")
			#win2.destroy()
		
			
	curobj.close()
	conobj.close()
	
	#win2.mainloop()

def reset():
	uid.delete(0,END)
	pwd.delete(0,END)

def exit():
	win.destroy()
def NewUser():
	def save():

		a=fname.get()
		b=lname.get()
		c=nuid.get()
		d=dname.get()
		#e=str(var.get())
		e = ""
		if radVar.get() == 1:
			e = "male"
		else:
			e = "female"

		f=npwd.get()
		#print(a," ",b," ",c," ",d," ",f," ")

		conobj=pymysql.connect(host="localhost", user="root",password="",port=3306)
		curobj=conobj.cursor()
		curobj.execute('use studentpro;')

		r= 'insert into user values("{fname}","{lname}","{nuid}","{dname}","{var}","{npwd}");'
		r1= r.format(fname=a, lname=b, nuid=c, dname=d, var=e, npwd=f)

		curobj.execute(r1)
		conobj.commit()
		curobj.close()
		conobj.close()
		
		win1.destroy()


		

	def reset():
		fanme.delete(0,END)
		lname.delete(0,END)
		nuid.delete(0,END)
		dname.delete(0,END)
		npwd.delete(0,END)

	win1=Tk()
	win1.title("Registration Page")
	win1.maxsize(height = 800,width = 750)
	win1.minsize(height = 800,width = 750)
	win1.configure(bg = "black")

	Label(win1,text = "Registration Here",font = ("Showcard Gothic",20),bg="black",fg = "purple").place(x = 280,y = 30)

	Label(win1,text = "Enter First Name",font = ("Comic Sans MS",15),bg="black",fg = "white").place(x = 170,y = 100)
	fname=Entry(win1,font=("Comic Sans MS", 15), bg="orange",fg = "black")
	fname.place(x = 400, y = 100)
	
	Label(win1,text = "Enter Last Name",font = ("Comic Sans MS",15),bg="black",fg = "white").place(x = 170,y = 170)
	lname=Entry(win1,font=("Comic Sans MS", 15), bg="orange",fg = "black")
	lname.place(x = 400, y = 170)

	Label(win1,text = "Enter User ID",font = ("Comic Sans MS",15),bg="black",fg = "white").place(x = 170,y = 240)
	nuid=Entry(win1,font=("Comic Sans MS", 15), bg="orange",fg = "black")
	nuid.place(x = 400, y = 240)

	Label(win1,text = "Enter Dept Name",font = ("Comic Sans MS",15),bg="black",fg = "white").place(x = 170,y = 310)
	#menu = StringVar()
	#menu.set("Select any dept.")
	#drop = OptionMenu(win1,menu,"cse","cst","etc","mech","civil",command = menu)
	#drop.place(x = 400,y = 310)
	dname=Entry(win1,font=("Comic Sans MS", 15), bg="orange",fg = "black")
	dname.place(x = 400, y = 310)

	Label(win1,text = "Select Gender",font = ("Comic Sans MS",15),bg="black",fg = "white").place(x = 170,y = 380)
	radVar = IntVar()
	r1=Radiobutton(win1, text= "Male", font=("Comic Sans MS",15),bg="orange",fg="white",variable=radVar,value = 1)
	r1.place(x=400, y=380)
	r2=Radiobutton(win1, text= "Female", font=("Comic Sans MS",15),bg="orange",fg="white",variable=radVar,value = 2)
	r2.place(x=500, y=380)	

	Label(win1,text = "Enter New Password",font = ("Comic Sans MS",15),bg="black",fg = "white").place(x = 170,y = 450)
	npwd=Entry(win1,font=("Comic Sans MS", 15), bg="orange",fg = "white",show="*")
	npwd.place(x = 400, y = 450)

	Button(win1, text="Submit",font=("Showcard Gothic",15),bg="red",fg="white",command = save).place(x=300, y =530)
	Button(win1, text="Reset",font=("Showcard Gothic",15),bg="red",fg="white",command = reset).place(x=450, y =530)

	win1.mainloop()
	





win.title("Student Database System") #to change or rename the title

win.maxsize(height = 500,width = 750)
win.minsize(height = 500,width = 750)

Label(win,text = "Please Login Here",font = ("Showcard Gothic",20),fg = "white",bg = "purple",relief = SUNKEN).place(x = 250,y = 50)
#place() used to visualise in better way

Label(win,text = "Enter User ID",font = ("Lucida Handwriting",10),fg = "white",bg ="dark green",relief = SUNKEN).place(x = 200,y = 120)

uid = Entry(win,font = (10),fg = "black")
uid.place(x = 350,y = 123)

Label(win,text = "Enter Password", font = ("Lucida Handwriting",10),fg = "white",bg = "dark green",relief = SUNKEN).place(x = 200,y = 200)

pwd = Entry(win,font = (10),fg = "black",show = "*")
pwd.place(x = 350,y = 200)


Button(win,text = "LOGIN",bg = "black",fg = "white",font = ("Showcard Gothic",10),command = login,activebackground = "light green",activeforeground = "yellow",relief = SUNKEN).place(x = 250,y = 250)

Button(win,text = "RESET",bg = "black",fg = "white",font = ("Showcard Gothic",10),command = reset,relief = SUNKEN).place(x = 350,y = 250)

Button(win,text = "EXIT",bg = "black",fg = "white",font = ("Showcard Gothic",10),command = exit,relief = SUNKEN).place(x = 450,y = 250)

Button(win,text = "New User",bg = "orange",fg = "white",font = ("Showcard Gothic",10),command=NewUser,relief = SUNKEN).place(x = 333,y = 300)



win.mainloop()