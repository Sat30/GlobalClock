# Importing libraries
from distutils.command.install_egg_info import safe_name
import socket
import sys

# Lets catch the 1st argument as server ip
# if (len(sys.argv) > 1):
#     ServerIp = sys.argv[1]
# else:
#     print("\n\n Run like \n python3 client.py < serverip address > \n\n")
#     exit(1)


# Now we can create socket object
s = socket.socket()

# Lets choose one port and connect to that port
PORT = 9898

# Lets connect to that port where server may be running
s.connect(("localhost", PORT))



print("\n\n\n",s.recv(1024).decode("utf-8"),s.recv(1024).decode("utf-8"),s.recv(1024).decode("utf-8"),sep='')
name=input("Enter your name : ")
s.send(name.encode())
print(s.recv(1024).decode("utf-8"))

SendData=1
while True:
    print("\n1: Date\n2: Time\n3: Address\n4: All\n\n5: Time Zone")
    SendData=(input("Select one of the option: "))
    s.send(SendData.encode())
    if SendData=='4':
       
        print("\n\n",s.recv(1024).decode("utf-8"),s.recv(1024).decode("utf-8"),s.recv(1024).decode("utf-8"),"\n\n",sep='\n')
    
    elif SendData=='5' :
        break
    
    else :

        print("\n\n",s.recv(1024).decode("utf-8"),"\n\n")



Senddata=1
while Senddata!=0 :

    print("\n\nSelect the one of the time server : ")
    print("01: Pacific/Midway\n02: America/Adak\n03: Pacific/Marquesas\n04: America/Sitka\n05: America/Los_Angeles\n06: America/Denver\n07: America/Chicago\n08: America/Bogota\n09: America/Grenada\n10: America/St_Johns\n11: America/Argentina/Mendoza\n12: Atlantic/South_Georgia\n13: Atlantic/Cape_Verde\n14: Europe/London\n15: Europe/Berlin\n16: Africa/Johannesburg\n17: Africa/Nairobi\n18: Asia/Dubai\n19: Asia/Karachi\n20: Asia/Kolkata\n21: Asia/Dhaka\n22: Asia/Bangkok\n23: Asia/Singapore\n24: Asia/Tokyo\n25: Australia/Sydney\n26: Pacific/Efate\n27: Pacific/Auckland")
    Senddata=(input("Select one of the option: "))
    s.send(Senddata.encode())
    if(Senddata=='0'):
        break

    print("\n\n" ,s.recv(1024).decode("utf-8"))

s.close()