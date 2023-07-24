#!/usr/bin/env python3
# Importing socket library 
import re
import socket
import time
from datetime import date
from datetime import datetime
import pytz

from geopy.geocoders import Nominatim
from termcolor import colored



t1=colored("─────────────────────────────────────────────────────────────────\n",'green')
t2=colored("─██████████████─██████████─██████──────────██████─██████████████─\n",'green')
t3=colored("─██░░░░░░░░░░██─██░░░░░░██─██░░██████████████░░██─██░░░░░░░░░░██─\n",'green')
t4=colored("─██████░░██████─████░░████─██░░░░░░░░░░░░░░░░░░██─██░░██████████─\n",'green')
t5=colored("─────██░░██───────██░░██───██░░██████░░██████░░██─██░░██─────────\n",'green')
t5=colored("─────██░░██───────██░░██───██░░██──██░░██──██░░██─██░░██████████─\n",'green')
t6=colored("─────██░░██───────██░░██───██░░██──██░░██──██░░██─██░░░░░░░░░░██─\n",'green')
t7=colored("─────██░░██───────██░░██───██░░██──██████──██░░██─██░░██████████─\n",'green')
t8=colored("─────██░░██───────██░░██───██░░██──────────██░░██─██░░██─────────\n",'green')
t9=colored("─────██░░██─────████░░████─██░░██──────────██░░██─██░░██████████─\n",'green')
tt1=colored("─────██░░██─────██░░░░░░██─██░░██──────────██░░██─██░░░░░░░░░░██─\n",'green')
tt2=colored("─────██████─────██████████─██████──────────██████─██████████████─\n",'green')
tt3=colored("─────────────────────────────────────────────────────────────────\n",'green')
time_style1=t1+t2+t3+t4
time_style2=t5+t6+t7+t8
time_style3=t9+tt1+tt2+tt3


def my_date() :
    date1=date.today()
    m_date="Date :"+str(date1.day)+":"+str(date1.month)+":"+str(date1.year)
    m_date=colored(m_date,'green')
    return m_date

def my_time():
    curr = time.localtime()
    time_order=colored("Time : "+time.strftime("%H:%M:%S", curr),'green')
    return time_order

def my_addr():
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode("Bangalore")
    # passing the coordinates
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    # Latitude & Longitude input
    Latitude = str(getLoc.latitude)
    Longitude = str(getLoc.longitude)

    location = geolocator.reverse(Latitude+","+Longitude)

    # Display
    address = location.raw['address']#dictionary
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    code = address.get('country_code')
    PostCode = address.get('postcode')
    addr="\nCity :"+str(city)+'\n'+"State : "+str(state)+'\n'+"Country :"+str(country)+'\n'+"Post Code : "+str(PostCode)+'\n'
    addr=colored(addr,'green')
    return addr


# Now we can create socket object
s = socket.socket()

# Lets choose one port and start listening on that port
PORT = 9898
print("\n Server is listing on port :", PORT, "\n")

# Now we need to bind to the above port at server side
s.bind(('localhost', PORT))

# Now we will put server into listenig  mode 

s.listen(10)

# Now we do not know when client will concatct server so server should be listening contineously  
while True:
    # Now we can establish connection with client
    conn, addr = s.accept()
    conn.send(time_style1.encode())
    conn.send(time_style2.encode())
    conn.send(time_style3.encode())
    
    name=conn.recv(1024).decode("utf-8")
    
    hi1=colored("\nHi "+name+"\n[IP address: "+ addr[0] + "]\nֲֳ\n*Welcome to Time Server* ",'green')

    msg = "\n\n|---------------------------------|\n"+hi1+"\n\n|---------------------------------|\n \n\n\n\n"

   
    conn.send(msg.encode())


    while True :
        RecvData = int(conn.recv(1024).decode("utf-8"))
        if RecvData==1:
            today_date=my_date()
            conn.send(today_date.encode())

        elif RecvData==2:
            time_order=my_time()
            conn.send(time_order.encode())

        elif RecvData==3:
            addr=my_addr()
            conn.send(addr.encode())

        elif RecvData==4:
            today_date=my_date()
            time_order=my_time()
            time_order=colored(time_order,'yellow')
            

            conn.send(today_date.encode())
            conn.send(time_order.encode())
           
            

        elif RecvData==5:
            break

        
    
    IST = pytz.timezone('Indian/Cocos')
   
    Recvdata=1
    while True:
        Recvdata = int(conn.recv(1024).decode("utf-8"))
        if Recvdata==1 :
            IST = pytz.timezone('Pacific/Midway')
        
        elif Recvdata==2 :
            IST = pytz.timezone('America/Adak')
        elif Recvdata==3:
            IST = pytz.timezone('Pacific/Marquesas')
        elif Recvdata==4:
            IST = pytz.timezone('America/Sitka')
        elif Recvdata==5:
            IST = pytz.timezone('America/Los_Angeles')
        elif Recvdata==6:
            IST = pytz.timezone('America/Denver')
        elif Recvdata==7:
            IST = pytz.timezone(' America/Chicago')
        elif Recvdata==8:
            IST = pytz.timezone('America/Bogota')
        elif Recvdata==9:
            IST = pytz.timezone('America/Grenada')
        elif Recvdata==10:
            IST = pytz.timezone('America/St_Johns')
        elif Recvdata==11:
            IST = pytz.timezone('America/Argentina/Mendoza')
        elif Recvdata==12:
            IST = pytz.timezone('Atlantic/South_Georgia')
        elif Recvdata==13:
            IST = pytz.timezone('Atlantic/Cape_Verde')
        elif Recvdata==14:
            IST = pytz.timezone('Europe/London')
        elif Recvdata==15:
            IST = pytz.timezone('Europe/Berlin')
        elif Recvdata==16:
            IST = pytz.timezone('Africa/Johannesburg')
        elif Recvdata==17:
            IST = pytz.timezone('Africa/Nairobi')
        elif Recvdata==18:
            IST = pytz.timezone('Asia/Dubai')
        elif Recvdata==19:
            IST = pytz.timezone('Asia/Karachi')
        elif Recvdata==20:
            IST = pytz.timezone('Asia/Kolkata')
        elif Recvdata==21:
            IST = pytz.timezone('Asia/Dhaka')
        elif Recvdata==22:
            IST = pytz.timezone('Asia/Bangkok')
        elif Recvdata==23:
            IST = pytz.timezone('Asia/Singapore')
        elif Recvdata==24:
            IST = pytz.timezone('Asia/Tokyo')
        elif Recvdata==25:
            IST = pytz.timezone('Australia/Sydney')
        elif Recvdata==26:
            IST = pytz.timezone('Pacific/Efate')
        elif Recvdata==27:
            IST = pytz.timezone('Pacific/Auckland')
        elif Recvdata==0:
            break

        datetime_ist = datetime.now(IST)
        m="Date & Time: "+str(datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z GMT%z'))
        m=colored(m,'green')
        conn.send(m.encode())
    # Close connection with client
    conn.close()
    print("\n Server closed the connection \n")
    break
    