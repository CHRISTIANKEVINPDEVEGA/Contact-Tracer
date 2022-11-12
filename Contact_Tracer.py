Contact_Tracing_DataBase={}

while True:
    print("Menu:")
    print("1-> Add an item")
    print("2-> Search a person in the database")
    print("3-> Exit(y/n)")
    user_opt=int(input("Select you desire option: "))
    if user_opt==1:
        personalinfo=[]
        user_input=input("Enter your Name: ")
        personalinfo.append(user_input.upper())
        user_input=input("Enter your Age: ")
        personalinfo.append(user_input)
        user_input=input("Enter your Address: ")
        personalinfo.append(user_input.upper())
        user_input=input("Enter your Phone Number: ")
        personalinfo.append(user_input)
        Contact_Tracing_DataBase[personalinfo[0]]={"Name":personalinfo[0],"Age":personalinfo[1],"Address":personalinfo[2],"Phone Number":personalinfo[3]}
        user_opt=input("Enter yes if you want to exit: ")
        if user_opt=="yes":
            break
        elif user_opt=="no":
            continue
        
    elif user_opt==2:
        print("You have chosen the option to search")
        search_id=input("Enter the name: ")
        search_id=search_id.upper()
        if search_id in Contact_Tracing_DataBase:
            print("Name: "+ Contact_Tracing_DataBase[search_id]["Name"])
            print("Age: "+ Contact_Tracing_DataBase[search_id]["Age"])
            print("Address: "+ Contact_Tracing_DataBase[search_id]["Address"])
            print("Phone Number: "+ Contact_Tracing_DataBase[search_id]["Phone Number"])
            user_opt=input("Enter yes if you want to exit: ")
            if user_opt=="yes":
                break
            elif user_opt=="no":
                continue
        else:
            print("Does not exist in Database.")

    elif user_opt==3:
        user_opt3=input("Do you wish to exit? ")
        if user_opt3=="yes":
            break
        if user_opt3=="no":
            continue


