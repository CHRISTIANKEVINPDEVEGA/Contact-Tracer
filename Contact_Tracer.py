personaldata={
    "Name":"",
    "Age":"",
    "Address":"",
    "Phone Number":""
}
while True:
    print("Menu:")
    print("1-> add an item")
    print("2-> Search")
    print("3-> Exit(y/n)")
    user_opt=int(input("Select an item: "))
    if user_opt==1:
        print("You have chosen the option to add an item")
        Name_=input("Enter your Name: ")
        personaldata["Name"]=Name_
        Age_=input("Enter your Age: ")
        personaldata["Age"]=Age_
        Address_=input("Enter your Address: ")
        personaldata["Address"]=Address_
        Phone_Number_=(input("Enter your Phone Number: "))
        personaldata["Phone Number"]=Phone_Number_
    elif user_opt==2:
        print("You have chosen the option to search")
        print("Name: "+ personaldata.get("Name"))
        print("Age: "+ personaldata.get("Age"))
        print("Address: "+ personaldata.get("Address"))
        print("Phone Number: "+ personaldata.get("Phone Number"))
        
    elif user_opt==3:
        user_opt3=input("Do you wish to exit? ")
        if user_opt3=="yes":
            break
        if user_opt3=="no":
            continue