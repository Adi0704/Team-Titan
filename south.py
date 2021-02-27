def south():
    n=int(input("Enter 1 for Oncology(Cancer Related) Hospitals \n"
                "Enter 2 for Cardiac(Heart Related) Hospitals\n"
                "Enter 3 for Orthopadeic(Bones and Muscles Related) Hospitals\n"
                "Enter 4 for ENT(Hearing and Speech Related) Hospitals\n"
                "Enter 5 for Dental(Tooth Related) Hospitals \n"
                "Enter 6 for General or any other disease related Hospitals\n"
                "Enter your input : "))
    if n==1:
        print("Oncology(Cancer Related) Hospitals in South Bangalore : \n"
              "1. Apollo Hospitals, Jayanagar, Contact Number : 8046124444\n"
              "2. Fortis Hospitals, Bannerghatta Road, Contact Number : 9663367253\n")
    elif n==2:
        print("Cardiac(Heart Related) Hospitals in South Bangalore : \n"
              "1.Sri Jayadeva Institute of Cardiovascular Sciences and Research, Bannerghatta Road, Contact Number : 08022977260\n"
              "2.Apollo Hospitals, Jayanagar, Contact Number : 8046124444\n")
    elif n==3:
        print("Orthopadeic(Bones and Muscles Related) Hospitals in South Bangalore : \n"
              "1. Fortis Hospitals, Bannerghatta Road, Contact Number : 9663367253\n"
              "2. People Tree Hospitals,SriNagar, Contact number : 9900091881 / 08049599900\n")
    elif n==4:
        print("ENT(Hearing and Speech Related) Hospitals in South Bangalore : \n"
              "1. Fortis Hospitals, Bannerghatta Road, Contact Number : 9663367253\n"
              "2. Medikeri's Super Speciality ENT Center, Lalbagh Road, Contact Number : 08026578324\n")
    elif n==5:
        print("Dental(Tooth Related) Hospitals in South Bangalore : \n"
              "1. Partha Dental Clinic, Basavangudi, Contact Number : 08050765000\n"
              "2. Apollo Dental Clinic, Basvangudi, Contact Number : 8046124444\n")
    elif n==6:
        print("General or any other disease related Hospitals in South Bangalore : \n"
              "1. Apollo Hospitals, Jayanagar, Contact Number : 8046124444\n"
              "2. KR Hospital, Srinagar, Contact Number : 8183675439\n")
    else:
        print("Wrong Input\n")
south()




