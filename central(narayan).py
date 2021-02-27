def central():
    n=int(input("Enter 1 for Oncology(Cancer Related) Hospitals \n"
                "Enter 2 for Cardiac(Heart Related) Hospitals\n"
                "Enter 3 for Orthopadeic(Bones and Muscles Related) Hospitals\n"
                "Enter 4 for ENT(Hearing and Speech Related) Hospitals\n"
                "Enter 5 for Dental(Tooth Related) Hospitals \n"
                "Enter 6 for General or any other disease related Hospitals\n"
                "Enter your input : "))
    if n==1:
        print("Oncology(Cancer Related) Hospitals in Central Bangalore : \n"
              "1. Apollo Hospital, Seshadripuram, Contact Number : 06366804477\n"
              "2. Manipal Hospitals, Malleshwaram, Contact number : 18001025555\n")
    elif n==2:
        print("Cardiac(Heart Related) Hospitals in Central Bangalore : \n"
              "1. Manipal Heart Institute, Domlur, Contact Number : 9663345653\n"
              "2. Fortis Hospital, Malleshwaram , Contact Number : 08022837260\n")
    elif n==3:
        print("Orthopadeic(Bones and Muscles Related) Hospitals in Central Bangalore : \n"
              "1. Amrutha Orthopadeic and Knee Clinic, Indiranagar, Contact Number : 08022156947\n"
              "2. The Bone & Joint Clinic Dr.Narendra Rangappa MS Ortho, Malleshwaram, Contact number : 08023526333\n")
    elif n==4:
        print("ENT(Hearing and Speech Related) Hospitals in Central Bangalore : \n"
              "1. Dr. Manu Bharath - ENT Specialist, Sadashiva Nagar, Contact Number : 08022985947\n"
              "2. Sanjevini ENT Clinic, Malleshwaram, Contact Number : 08025710586\n")
    elif n==5:
        print("Dental(Tooth Related) Hospitals in Central Bangalore : \n"
              "1. Dr.Nagendra Dental Clinic, Domlur, Contact Number : 08022156947\n"
              "2. Dr.Mallendra Dental Clinic, Contonment Area, Contact number : 08023530333\n")
    elif n==6:
        print("General or any other disease related Hospitals in Central Bangalore : \n"
              "1. Fortis Hospital, Malleshwaram , Contact Number : 08022837260\n"
              "2. Apollo Hospital, Seshadripuram, Contact Number : 06366804477\n")
    else:
        print("Wrong Input\n")
central()




