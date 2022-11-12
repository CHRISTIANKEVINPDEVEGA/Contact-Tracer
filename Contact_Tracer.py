print("Menu:")
print("1-> add an item")
print("2-> search an item")
print("3-> Exit(y/n)")

personaldata={
    "Name":"",
    "Age":"",
    "Address":"",
    "Phone Number":""
}

user_opt=int(input("Select an item: "))
if user_opt==1:
    print("You have chosen the option to add an item")
    Name_=input("Enter your Name: ")
    personaldata["Name"]=Name_
    Age_=input("Enter your Age: ")
    personaldata["Age"]=Age_
    Address_=input("Enter your Address: ")
    personaldata["Address"]=Address_
    Phone_Number_=input("Enter your Phone Number: ")
    personaldata["Phone Number"]:Phone_Number_
    print(personaldata)
if user_opt==2:
    print("You have chosen the option to search for an item")

if user_opt==3:
    print("Do you wish to exit?")