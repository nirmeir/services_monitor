

def make_test(time,date , time2, date2):

    with open("serviceList.txt", "r") as myfile:
        data = myfile.read()


        data2 = data.split("Time : ",)
        data2.remove(data2[0])

        for index,dat in enumerate (data2):
            dat = dat.split("\n",maxsplit=2)
            dat[1]=dat[1][7:]
            data2[index]=dat



        j=0
        timedict = {}

        for index ,i in enumerate (data2):
            timedict[index]=[int(data2[j][1].replace("/","")),int(data2[j][0].replace(":",""))]
            j+=1

        # print(time_1dict.items())
        # date_1 = input("please enter a date_1")
        date = date.replace("/","")
        date = int(date)

        # time_1 = input("please enter a time_1")
        time = time.replace(":","")
        time =int(time)



        final_index=0

        for t,h in timedict.values():

            if t == int(date) and h == int(time):
                print("yes")
                print(final_index)
                break
            final_index += 1

            if t == int(date) and h != int(time):

                takeClosest = lambda num, collection: min(collection, key=lambda xy: abs(xy[1] - num))
                time = (takeClosest(int(time), timedict.values()))
                time=time[1]

            if t != int(date) :
                takeClosest = lambda date, collection: min(collection, key=lambda xy: abs(xy[0] - date))
                date = (takeClosest(int(date), timedict.values()))
                date = date[0]


    my_dict={}
    for i in data2[final_index][2:]:
        # my_dict[index]=i.replace("\n","")
        my_dict [index] = i

    my_dict[0]=final_index
    # print(my_dict.items())
    print(my_dict.values())
    # test = open("test.txt", "a+")
    # for k, v in my_dict.items():
    #     test.write(f"service_index : {k} , serviceName : {v} \n")
    # test.close()

    # print(my_dict.values())

    with open("serviceList.txt", "r") as myfile:
        data = myfile.read()

        data2 = data.split("Time : ",)
        data2.remove(data2[0])

        for index,dat in enumerate (data2):
            dat = dat.split("\n",maxsplit=2)
            dat[1]=dat[1][7:]
            data2[index]=dat



        j=0
        timedict = {}

        for index ,i in enumerate (data2):
            timedict[index]=[int(data2[j][1].replace("/","")),int(data2[j][0].replace(":",""))]
            j+=1

        # print(time_1dict.items())
        # date_1 = input("please enter a date_1")
        date2 = date2.replace("/","")
        date2 = int(date2)

        # time_1 = input("please enter a time_1")
        time2 = time2.replace(":","")
        time2 =int(time2)



        final_index=0


        for t,h in timedict.values():

            if t == int(date2) and h == int(time2):
                print("yes")
                print(final_index)
                break
            final_index += 1

            if t == int(date2) and h != int(time2):

                takeClosest = lambda num, collection: min(collection, key=lambda xy: abs(xy[1] - num))
                time2 = (takeClosest(int(time2), timedict.values()))
                time2=time2[1]

            if t != int(date2) :
                takeClosest = lambda date2, collection: min(collection, key=lambda xy: abs(xy[0] - date2))
                date2 = (takeClosest(int(date2), timedict.values()))
                date2 = date2[0]

    my_dict2={}

    for i in data2[final_index][2:]:
        my_dict2 [index] = i

    my_dict2[0] = final_index
    print(my_dict2.values())

    # print(data2[final_index])
    # print(data2[final_index][2:])


    if my_dict[0]>my_dict2[0]:
        print("my_dict > my_dict2")

        for value in my_dict2.values():
            print(value)
            if value not in my_dict.values():
                test = open("test.txt", "a+")
                test.write(f"the service {value} is Stop\n\n")
                # print(f"the service {value} is Stop\n\n")

        for value in my_dict.values():
            if value not in my_dict2.values():
                test = open("test.txt", "a+")
                print(f"new service {value} is Running\n\n")
                # status_Log.write(f"new service {value} is Running\n\n")

    if my_dict[0] < my_dict2[0]:
        print("my_dict < my_dict2")

        for value in my_dict.values():
            if value not in my_dict2.values():

                test = open("test.txt", "a+")
                test.write(f"the service {value} is Stop\n\n")
                # print(f"the service {value} is Stop\n\n")

        for value in my_dict2.values():
            if value not in my_dict.values():
                test = open("test.txt", "a+")
                # print(f"new service {value[1]} is Running\n\n")
                test.write(f"new service {value} is Running\n\n")

    test.close()

if __name__ == '__main__':


        time_1=input("enter a time_1")
        date_1=input("enter a date_1")
        time_2 = input("enter a time_2")
        date_2 = input("enter a date_2")

        make_test(time_1,date_1,time_2,date_2)











