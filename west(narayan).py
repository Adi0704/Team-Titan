def west():
    n=int(input("Enter 1 for Oncology(Cancer Related) Hospitals \n"
                "Enter 2 for Cardiac(Heart Related) Hospitals\n"
                "Enter 3 for Orthopadeic(Bones and Muscles Related) Hospitals\n"
                "Enter 4 for ENT(Hearing and Speech Related) Hospitals\n"
                "Enter 5 for Dental(Tooth Related) Hospitals \n"
                "Enter 6 for General or any other disease related Hospitals\n"
                "Enter your input : "))
    if n==1:
        print("Oncology(Cancer Related) Hospitals in West Bangalore : \n"
              "1. Gurushree Hospital, Vijay Nagar, Contact Number : 08023392641\n"
              "2. BGS Gleneagles Global Hospitals, Kengeri, Contact number : 1800123111\n")
    elif n==2:
        print("Cardiac(Heart Related) Hospitals in West Bangalore : \n"
              "1. Fortis Hospitals, Nagarbhavi, Contact Number : 9663367253\n"
              "2. Jayadeva Hospital ESI, Rajajinagar , Contact Number : 08022977260\n")
    elif n==3:
        print("Orthopadeic(Bones and Muscles Related) Hospitals in West Bangalore : \n"
              "1. Abhilash Orthopadeic Hospital, Mahalakshmi Layout, Contact Number : 08022156947\n"
              "2. Sumeru Orthopadeic and Spine Hospital, Rajarajeshwari Nagar, Contact number : 08023530333\n")
    elif n==4:
        print("ENT(Hearing and Speech Related) Hospitals in West Bangalore : \n"
              "1. Meenakshi ENT Hospital, Nandini Layout, Contact Number : 08022156947\n"
              "2. Vismaya ENT Clinic, Nagarbhavi, Contact Number : 08025478586\n")
    elif n==5:
        print("Dental(Tooth Related) Hospitals in West Bangalore : \n"
              "1. Dr.Suresh Dental Clinic, Basaveshnagar, Contact Number : 08022156947\n"
              "2. Dr.Narendra Dental Clinic, Nayandhalli, Contact number : 08023530333\n")
    elif n==6:
        print("General or any other disease related Hospitals in West Bangalore : \n"
              "1. Fortis Hospitals, Nagarbhavi, Contact Number : 9663367253\n"
              "2. BGS Gleneagles Global Hospitals, Kengeri, Contact number : 1800123111\n")
    else:
        print("Wrong Input\n")
west()




