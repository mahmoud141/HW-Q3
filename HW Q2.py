UserInput = input("Enter your first Value: ")
UserInputOP = input("Enter the OP you want to process : ")
UserVerify = UserInput.isdecimal() or UserInput.isdigit() or float
UserInput2 = input("Enter your Second Value: ")
UserVerify2 = UserInput2.isdigit()
UserVerify2 = UserInput2.isdecimal() or UserInput2.isdigit() or float

if UserVerify is not False and UserVerify2 is not False:
    if UserInputOP == "1" or UserInputOP == "+" :
        print("You Results is " , float(UserInput) + float(UserInput2) )
        Resultin = float(UserInput) + float(UserInput2)
        UserResult = input("Do you prefer you result to be rounded up to high value press 1 , to low Value press 2 , to be rounded normal 3 or to be shown without decimel as in Integer press 4")
        if UserResult == "1" :
            print("the result rounded to the high value is " , Resultin.__ceil__())
        elif UserResult == "2":
            print("the result rounded to the high value is ", Resultin.__floor__())
        elif UserResult == "3":
            print("the result rounded to the normal value is ", Resultin.__round__())
        elif UserResult == "4":
           print("the result rounded to the normal value is ", Resultin.__int__())
        elif UserResult == "0":
           print("Well, you chose to exit the program, Thank you for your time. all the BEST ")
        else:
            print("Ooops!, you have enterd a wrong Decision for your result to be shown, exsiting program")
    elif UserInputOP == "2" or UserInputOP == "-" :
        print("You Results is " ,float(UserInput) - float(UserInput2) )
        Resultin = float(UserInput) - float(UserInput2)
        UserResult = input("Do you prefer you result to be rounded up to high value press 1 , to low Value press 2 , to be rounded normal 3 or to be shown without decimel as in Integer press 4 or press 0 to exsit >  ")
        if UserResult == "1":
            print("the result rounded to the high value is ", Resultin.__ceil__())
        elif UserResult == "2":
            print("the result rounded to the high value is ", Resultin.__floor__())
        elif UserResult == "3":
            print("the result rounded to the normal value is ", Resultin.__round__())
        elif UserResult == "4":
            print("the result rounded to the normal value is ", Resultin.__int__())
        elif UserResult == "0":
            print("Well, you chose to exit the program, Thank you for your time. all the BEST ")
        else:
            print("Ooops!, you have enterd a wrong Decision for your result to be shown, exsiting program")
    elif UserInputOP == "3" or UserInputOP == "*" :
        print("You Results is " , float(UserInput) * float(UserInput2) )
        Resultin = float(UserInput) * float(UserInput2)
        UserResult = input(
            "Do you prefer you result to be rounded up to high value press 1 , to low Value press 2 , to be rounded normal 3 or to be shown without decimel as in Integer press 4  press 0 to exsit > ")
        if UserResult == "1":
            print("the result rounded to the high value is ", Resultin.__ceil__())
        elif UserResult == "2":
            print("the result rounded to the high value is ", Resultin.__floor__())
        elif UserResult == "3":
            print("the result rounded to the normal value is ", Resultin.__round__())
        elif UserResult == "4":
            print("the result rounded to the normal value is ", Resultin.__int__())
        elif UserResult == "0":
            print("Well, you chose to exit the program, Thank you for your time. all the BEST ")
        else:
            print("Ooops!, you have enterd a wrong Decision for your result to be shown, exsiting program")
    elif UserInputOP == "4" or UserInputOP == "/" :
        print("You Results is " , float(UserInput) / float(UserInput2) )
        Resultin = float(UserInput) / float(UserInput2)
        UserResult = input("Do you prefer you result to be rounded up to high value press 1 , to low Value press 2 , to be rounded normal 3 or to be shown without decimel as in Integer press 4  press 0 to exsit > ")
        if UserResult == "1":
            print("the result rounded to the high value is ", Resultin.__ceil__())
        elif UserResult == "2":
            print("the result rounded to the high value is ", Resultin.__floor__())
        elif UserResult == "3":
            print("the result rounded to the normal value is ", Resultin.__round__())
        elif UserResult == "4":
            print("the result rounded to the normal value is ", Resultin.__int__())
        elif UserResult == "0":
            print("Well, you chose to exit the program, Thank you for your time. all the BEST ")
        else:
            print("Ooops!, you have enterd a wrong Decision for your result to be shown, exsiting program")
    elif UserInputOP == "5" or UserInputOP == "^" :
        print("You Results is " , pow(float(UserInput) , float(UserInput2)) )
        Resultin = float(UserInput) - float(UserInput2)
        UserResult = input(
            "Do you prefer you result to be rounded up to high value press 1 , to low Value press 2 , to be rounded normal 3 or to be shown without decimel as in Integer press 4  press 0 to exsit > ")
        if UserResult == "1":
            print("the result rounded to the high value is ", Resultin.__ceil__())
        elif UserResult == "2":
            print("the result rounded to the high value is ", Resultin.__floor__())
        elif UserResult == "3":
            print("the result rounded to the normal value is ", Resultin.__round__())
        elif UserResult == "4":
            print("the result rounded to the normal value is ", Resultin.__int__())
        elif UserResult == "0":
            print("Well, you chose to exit the program, Thank you for your time. all the BEST ")
        else:
            print("Ooops!, you have enterd a wrong Decision for your result to be shown, exsiting program")
    elif UserInputOP == "6" or UserInputOP == "%" :
        print("Your Results is " , float(UserInput) % float(UserInput2) )
        Resultin = float(UserInput) % float(UserInput2)
        UserResult = input( "Do you prefer you result to be rounded up to high value press 1 , to low Value press 2 , to be rounded normal 3 or to be shown without decimel as in Integer press 4  press 0 to exsit > ")
        if UserResult == "1":
            print("the result rounded to the high value is ", Resultin.__ceil__())
        elif UserResult == "2":
            print("the result rounded to the high value is ", Resultin.__floor__())
        elif UserResult == "3":
            print("the result rounded to the normal value is ", Resultin.__round__())
        elif UserResult == "4":
            print("the result rounded to the normal value is ", Resultin.__int__())
        elif UserResult == "0":
            print("Well, you chose to exit the program, Thank you for your time. all the BEST ")
        else:
            print("Ooops!, you have enterd a wrong Decision for your result to be shown, exsiting program NOW!!!")

else:
     print("You have enterd a wrong integer number for calculation for either or both values, repeat the process again later...")
