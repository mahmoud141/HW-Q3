num1 = input("Enter your 1st int Value >: ")
num2 = input("Enter your 2nd int Value >: ")
num3 = input("Enter your 3rd int Value >: ")
num4 = input("Enter your 4th int Value >: ")
num5 = input("Enter your 5th int  Value >: ")

number1 = num1.isdecimal() or num1.isdigit() or float
number2 = num2.isdecimal() or num2.isdigit() or float
number3 = num3.isdecimal() or num3.isdigit() or float
number4 = num4.isdecimal() or num4.isdigit() or float
number5 = num5.isdecimal() or num5.isdigit() or float

print("You have entered these Values to Matrix", num1 , num2 , num3 , num4 ,num5)

Operate = input("what is the process you want to pefrom, for getting the higest Value press 1 , Lowest Value 2 , Both Value Lowest and highest press 3 to Valdiate your entries... >: ")

if number1 and number2 and number3 and number4 and number5 ==True:
      # Check if the entires are all numbers then proceed to next if all is True
 if Operate == "1" or Operate == "3" :
        if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
         print("The 1st int you entered in the list which is number  ", num1, " is the Highest Value among all")
        elif num2 > num1 and num2 > num4 and num2 > num5 and num2 > num3:
         print("The 2nd int you entered in the list which is number  ", num2, " is the Highest Value among all")
        elif num3 > num2 and num3 > num5 and num3 > num4 and num3 > num1:
         print("The 3rd int you entered in the list which is number  ", num3, " is the Highest Value among all")
        elif num4 > num2 and num4 > num3 and num4 > num5 and num4 > num1:
         print("The 4th int you entered in the list which is number  ", num4, " is the Highest Value among all")
        elif num5 > num1 and num5 > num4 and num5 > num2 and num5 > num3:
         print("The 5th int you entered in the list which is number  ", num5, " is the Highest Value among all")
        else:
            print("You have enterd identical Values for all entries")

 if Operate == "2" or Operate == "3" :
        if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
            print("The 1st int you entered in the list Which is number  ", num1, " is the Lowest Value among all entries.")
        elif num2 < num1 and num2 < num4 and num2 < num5 and num2 < num3:
         print("The 2nd int you entered in the list Which is number  ", num2, " is the Lowest Value among all entries.")
        elif num3 < num2 and num3 < num5 and num3 < num4 and num3 < num1:
         print("The 3rd int you entered in the list Which is number  ", num3, " is the Lowest Value among all entries.")
        elif num4 < num2 and num4 < num3 and num4 < num5 and num4 < num1:
         print("The 4th int you entered in the list Which is number  ", num4, " is the Lowest Value among all entries.")
        elif num5 < num1 and num5 < num4 and num5 < num3 and num5 < num2:
         print("The 5th int you entered in the list Which is number  ", num5, " is the Lowest Value among all entries.")
        else:
            print("You have enterd identical Values for all entries")

else:
    # if one of the entries is wrong, str END
     print("You have entered a incorrect VaLue re-run the program again ,,,,")

# print(min(num1,num2,num3,num4,num5))
# print(max(num1,num2,num3,num4,num5))