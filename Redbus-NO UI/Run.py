from classes import texts
from os import system
import os
import sqlite3
conn=sqlite3.connect('redbus.db')
c=conn.cursor()

system('cls')
print('\n'*5)
print("\t\t\t\t\t\tBus Booking App\n\n\t\t1.Register\n\n\t\t2.Login")
choice=int(input("\n\tEnter Your Choice: "))

if(choice==1):
	texts().register_text(c,conn)
else:
	texts().login_text(c,conn)
"""
#c.execute("INSERT INTO seat1 VALUES(?,?,?)",(100,'semi-sleeper',''))
#conn.commit()
c.execute("UPDATE seat1 SET seats_filled=?",[('a-1')])
c.execute("SELECT seats_filled FROM seat1 WHERE bus_number=100")
p=c.fetchone()
try:
	p=p.split(',')
except AttributeError:
	p=p
for i in p:
	i=i.split(',')
	b=i[0].split('-')
	print(b)		
for i in range():
	for j in range():"""
		 


		








