Contact_Tracing_DataBase={}

while True:
    print("Menu:")
    print("1-> add an item")
    print("2-> Search")
    print("3-> Exit(y/n)")
    user_opt=int(input("Select an item: "))
    if user_opt==1:
        personalinfo=[]
        user_input=input("Enter your Name: ")
        personalinfo.append(user_input)
        user_input=input("Enter your Age: ")
        personalinfo.append(user_input)
        user_input=input("Enter your Address: ")
        personalinfo.append(user_input)
        user_input=input("Enter your Phone Number: ")
        personalinfo.append(user_input)
        Contact_Tracing_DataBase[personalinfo[0]]={"Name":personalinfo[0],"Age":personalinfo[1],"Address":personalinfo[2],"Phone Number":personalinfo[3]}

    elif user_opt==2:
        print("You have chosen the option to search")
        search_id=input("Enter the name: ")
        print("You have chosen the option to search")
        print("Name: "+ Contact_Tracing_DataBase[search_id]["Name"])
        print("Age: "+ Contact_Tracing_DataBase[search_id]["Age"])
        print("Address: "+ Contact_Tracing_DataBase[search_id]["Address"])
        print("Phone Number: "+ Contact_Tracing_DataBase[search_id]["Phone Number"])

    elif user_opt==3:
        user_opt3=input("Do you wish to exit? ")
        if user_opt3=="yes":
          break
        if user_opt3=="no":
           continue


