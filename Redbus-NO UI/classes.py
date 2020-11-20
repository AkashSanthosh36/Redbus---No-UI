from os import system
from getpass import getpass
from prettytable import PrettyTable
class texts:
	def __init__(self):
		pass

	#Registration Text
	def register_text(self,c,conn):
		system('cls')
		print('\n'*5)
		print("\n\t\t\t\t\t\tRegistration Form")
		a=1
		while(a):
			first=input("\n\tFirst Name: ")
			last=input("\n\tLast Name: ")
			email=input("\n\tEmail Address: ")
			username=input("\n\tUsername: ")
			password=getpass("\n\tPassword: ")
			password1=getpass("\n\tConfirm Password: ")
			if(password==password1):
				a=0
				system('cls')
				print("\n\t\t\t\t\tRegistration Successful +_+ !")
			else:
				system("cls")
				print("The Fields Are Incorrect!")
		emp=register(first,last,email,username,password)	
		emp.insert(c,conn)
		emp1=texts()
		emp1.book(c,conn,username)

	#Login Text
	def login_text(self,c,conn):
		system('cls')
		print('\n'*5)
		print("\n\t\t\t\t\t\tLogin Form")
		d=1
		while(d):
			p=1
			username=input("\n\tUsername: ")
			password=getpass("\n\tPassword: ")
			c.execute("SELECT username,password FROM  users")
			for i,j in c.fetchall():
				if(i==username and j==password):
					print("\n\t\t\t\t\tLogin Successful +_+")
					p,d=0,0
					emp1=texts()
					emp1.book(c,conn,username)
					break
			if(p==1):
				system('cls')
				print("\n\t\t\t\tThe username and password is incorrect!")


	#Bus Details Form
	def bus_details(self,c,conn):
		system('cls')
		print('\n'*5)
		print("\n\t\t\t\t\tBus Details Form")
		bus_number=int(input("\n\t\tBus Number: "))
		type_of_bus=input("\n\t\tType_Of_Bus: ")
		boarding_points=input("\n\t\tBoarding_Points: ")
		dropping_points=input("\n\t\tDropping_Points: ")
		seats_available=int(input("\n\t\tSeats Available: "))
		total_seats=int(input("\n\t\tTotal Seats: "))
		duration=int(input("\n\t\tDuration: "))
		date_of_journey=input("\n\t\tDate: ")
		c.execute("INSERT INTO bus11 VALUES(?,?,?,?,?,?,?,?)",(bus_number,type_of_bus,boarding_points,dropping_points,seats_available,total_seats,duration,date_of_journey))
		conn.commit()
		c.execute("SELECT * FROM bus11")
		print(c.fetchall())
		c.execute("SELECT * FROM bus11 WHERE date_of_journey='2019-04-27 %:%:%'")
		print(c.fetchall())

	#Booking Form
	def book(self,c,conn,username):
		system('cls')
		print('\n'*4)
		b=[]
		print("\n\tWelcome ",username,"!")
		print("\n\t\t\t\t\t\tBooking Aura +_+")
		from1=input("\n\tFrom: ").lower()
		to1=(input("\n\tTo: ").strip()).lower()
		type1=(input("\n\tType Of Bus: ").strip()).lower()
		date=input("\n\tDate: ")
		month=input("\n\tMonth: ")
		year=input("\n\tYear: ")
		passengers=int(input("\n\tPassengers Count: "))
		if(len(date)==1):
			date=str(0)+date
		if(len(month)==1):
			month=str(0)+month
		dt=year+'-'+month+'-'+date	
		c.execute("SELECT bus_number,type_of_bus,boarding_points,dropping_points,date_of_journey,seats_available FROM bus11")
		for p,q,r,s,t,u in c.fetchall():
			r=[x.lower() for x in (r.split(','))]
			s=[x.lower() for x in (s.split(','))]
			if(from1 in r and to1 in s):
				if(type1==q):
					if(dt in t):
						if(u>=passengers):
							b.append(p)
		t=PrettyTable(['Bus_Number','Type_Of_Bus','Seats Available','Duration','Date & Time'])
		for i in b:				
			c.execute("SELECT bus_number,type_of_bus,seats_available,duration,date_of_journey FROM bus11 where bus_number=?",[(i)])
			t.add_row(c.fetchone())
		print(t)
		print("\n\t\t\tWhich bus do you want to book?\n\t")
		n=int(input("Bus Number: "))
		c.execute("SELECT seats_available FROM bus11 WHERE bus_number=?",[(n)])
		x=c.fetchone()[0]-passengers
		c.execute("UPDATE bus11 SET seats_available=? WHERE bus_number=?",[(x),(n)])
		conn.commit()
		print("Booking Successful")

class register:
	def __init__(self,first,last,email,username,password):
		self.first=first
		self.last=last
		self.email=email
		self.username=username
		self.password=password

	def insert(self,c,conn):
		c.execute("INSERT INTO users VALUES(?,?,?,?,?)",(self.first,self.last,self.email,self.username,self.password))
		conn.commit()
			

class tables:
	
	def __init__(self):
		pass

	#users table
	def users(self,c):
		c.execute("""CREATE TABLE IF NOT EXISTS users(
		first_name text NOT NULL,
		last_name text NOT NULL,
		email text NOT NULL UNIQUE,
		username text NOT NULL UNIQUE,
		password text NOT NULL
		)""")

	#bus table
	def buses(self,c):
		c.execute("""CREATE TABLE IF NOT EXISTS bus11(
			bus_number numeric NOT NULL UNIQUE,
			type_of_bus text,
			boarding_points text NOT NULL,
			dropping_points text NOT NULL,
			seats_available numeric,
			duration numeric,
			date_of_journey TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
			)""")				

	#Seats Table
	def seats(self,c):
		c.execute("""CREATE TABLE IF NOT EXISTS seat1(
				bus_number numeric NOT NULL UNIQUE,
				type_of_bus text,
				seats_filled text
				)""")	