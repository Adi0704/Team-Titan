def feedback():
    print("We hope you have got all the required information that you were looking for.\n\n")
    c=int(input("We would love to hear some feedback from you..Please rate our following project from 1-5: "))
    if c<3:
        print("\n\nWe regret the inconvenience caused ..We will look to make the required changes \n\n")
        change=input("Please tell us where we could improve the project :")

    print("We have noted your valuable feedback \n          THANK YOU FOR USING TITAN HEALTH APP        ")
feedback()
