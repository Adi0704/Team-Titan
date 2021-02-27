def rural():
    n=int(input("Enter 1 for Oncology(Cancer Related) Hospitals \n"
                "Enter 2 for Cardiac(Heart Related) Hospitals\n"
                "Enter 3 for Orthopadeic(Bones and Muscles Related) Hospitals\n"
                "Enter 4 for ENT(Hearing and Speech Related) Hospitals\n"
                "Enter 5 for Dental(Tooth Related) Hospitals \n"
                "Enter 6 for General or any other disease related Hospitals\n"
                "Enter your input : "))
    if n==1:
        print("Oncology(Cancer Related) Hospitals in Rural Bangalore : \n"
              "1. JP Hospital, Nelamangala, Contact Number : 6366887477\n"
              "2. Columbia Asia Hospitals, Doddaballapur, Contact number : 1800102955\n")
    elif n==2:
        print("Cardiac(Heart Related) Hospitals in Rural Bangalore : \n"
              "1. Columbia Asia Hospitals, Doddaballapur, Contact number : 1800102955\n"
              "2. Apollo Hospital, Doddaballapur , Contact Number : 08022826260\n")
    elif n==3:
        print("Orthopadeic(Bones and Muscles Related) Hospitals in Rural Bangalore : \n"
              "1. Anand Orthopadeic and Knee Clinic, Hoskote, Contact Number : 08022556947\n"
              "2. Mahadevappa Ortho Clinic, Nelamangala, Contact number : 08023526322\n")
    elif n==4:
        print("ENT(Hearing and Speech Related) Hospitals in Rural Bangalore : \n"
              "1. Dr. Madukhar - ENT Specialist, Hoskote, Contact Number : 08022985947\n"
              "2. Netra ENT Clinic, Doddaballapur, Contact Number : 08025710586\n")
    elif n==5:
        print("Dental(Tooth Related) Hospitals in Rural Bangalore : \n"
              "1. Dr.Mahesh Dental Clinic, Hoskote, Contact Number : 08021856547\n"
              "2. Dr.Chandru Dental Clinic, Nelamangala, Contact number : 08026539543\n")
    elif n==6:
        print("General or any other disease related Hospitals in Rural Bangalore : \n"
              "1. Surksha Hospital, Doddaballapur , Contact Number : 08023834960\n"
              "2. Columbia Asia Hospitals, Doddaballapur, Contact number : 1800102955\n")
    else:
        print("Wrong Input\n")
rural()


