import multiprocessing
import threading
import time
from datetime import datetime
from multiprocessing import Process
import wmi



f = wmi.WMI()

print("The program is running ...")

status_Log = open("status_Log.txt", "a+")
service = open("serviceList.txt", "a+")




my_dict={}
i = 0

for serv in f.Win32_Service(State= "Running"):

    my_dict[i] = serv.Name
    i=i+1
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%d/%m/%y")

service.write(f"Time : {current_time}\nDate : {current_date}\n\n")


for v in my_dict.values():
    service.writelines(f" {v} \n")




waiting = input("set time for searching")

while True:

    time.sleep(int(waiting))

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d/%m/%y")

    service = open("serviceList.txt", "a+")
    service.write(f"Time : {current_time}\nDate : {current_date}\n\n")
    service.closed

    status_Log = open("status_Log.txt", "a+")
    status_Log.write(f"Time : {current_time}\nDate : {current_date}\n\n")
    status_Log.close()

    j=0
    my_dict2 = {}

    for serv in f.Win32_Service(State="Running"):
        my_dict2[j] = serv.Name
        j=j+1
    service = open("serviceList.txt", "a+")

    for v in my_dict2.values():
        service.write(f" {v} \n")

    service.close()

    for value in my_dict.values():
        if value not in my_dict2.values():

            status_Log = open("status_Log.txt", "a+")
            status_Log.write(f"the service {value} is Stop\n\n")
            print(f"the service {value} is Stop\n\n")



    for value in my_dict2.values():
        if value not in my_dict.values():

            status_Log = open("status_Log.txt", "a+")
            print(f"new service {value} is Running\n\n")
            status_Log.write(f"new service {value} is Running\n\n")

    status_Log.close()

    my_dict=my_dict2







