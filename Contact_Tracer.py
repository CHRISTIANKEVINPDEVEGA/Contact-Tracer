Contact_Tracing_DataBase={}

while True:
    print("Menu:")
    print("1-> add an item")
    print("2-> Search")
    print("3-> Exit(y/n)")
    user_opt=int(input("Select an item: "))
    if user_opt==1:
        personalinfo=[]
        user_input=input("put name: ")
        personalinfo.append(user_input)
        user_input=input("Age: ")
        personalinfo.append(user_input)
        user_input=input("Adress: ")
        personalinfo.append(user_input)
        user_input=input("Phone Number: ")
        personalinfo.append(user_input)
        Contact_Tracing_DataBase[personalinfo[0]]={"Name":personalinfo[0],"Age":personalinfo[1],"Address":personalinfo[2],"Phone Number":personalinfo[3]}
    
    elif user_opt==3:
        user_opt3=input("Do you wish to exit? ")
        if user_opt3=="yes":
          break
        if user_opt3=="no":
           continue


