import re
pattern1=r"^(?=.*\d)[A-Za-z\d_]{8,12}$"
pattern2=r"^[A-Za-z\d._%+-]+@gmail\.com$"
pattern3=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#&_!$%])[A-Za-z\d@#&_]{8,12}$"
pattern4=r"^(\+91)?\d{10}$" #(+\91)? includes optional +91 coountry code. it can match with num. without it or with it.
while True:
    print("1. Check Username\n2.Check Email\n3.Check Password\n4.Check Phone number\n5.Exit\n")
    choice=int(input("Enter your choice(1-5): "))
    if(choice==1):
        text1=input("Enter Username(Note:-It should have atleast one number):")
        res1=re.fullmatch(pattern1,text1)
        if(res1!=None):
            print("Valid")
        else:
            print("Not valid")
    elif(choice==2):
        text2=input("Enter email:")
        res2=re.fullmatch(pattern2,text2)
        if(res2!=None):
            print("Valid")
        else:
            print("Not valid")
    elif(choice==3):
        text3=input("Enter password(Note:-Atleast one uppercase,special character and digit):")
        res3=re.fullmatch(pattern3,text3)
        if(res3!=None):
            print("Valid")
        else:
            print("Not valid")
    elif(choice==4):
        text4=input("Enter phone number(Note:-No need to enter country code):")
        res4=re.fullmatch(pattern4,text4)
        if(res4!=None):
            print("Valid")
        else:
            print("Not valid")
    else:
        print("Invalid input")
        break