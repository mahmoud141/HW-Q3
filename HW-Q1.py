Name1 = input("enter your name : ")
Age1 = input("Enter your age : ")
address = input("Input your address please : ")
Name = Name1.isdigit()
Age = Age1.isdigit()
if Name == False and Age == True:
    print("Hello Mr/Ms" , Name1 , "age " , Age1 , "located in " , address , "Thanks for being one of our comunity , have agreat Day." )
else:print("You have enterd a wrong name,age value, please make sure you enter a correct Value in the requierd fields , exsiting program")
