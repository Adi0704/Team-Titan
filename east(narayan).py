def east():
    n=int(input("Enter 1 for Oncology(Cancer Related) Hospitals \n"
                "Enter 2 for Cardiac(Heart Related) Hospitals\n"
                "Enter 3 for Orthopadeic(Bones and Muscles Related) Hospitals\n"
                "Enter 4 for ENT(Hearing and Speech Related) Hospitals\n"
                "Enter 5 for Dental(Tooth Related) Hospitals \n"
                "Enter 6 for General or any other disease related Hospitals\n"
                "Enter your input : "))
    if n==1:
        print("Oncology(Cancer Related) Hospitals in East Bangalore : \n"
              "1. Bowring and Lady Curzon Hospital, Shivaji Nagar, Contact Number : 08022156947\n"
              "2. Sparsh Hospitals, Invantry Road, Contact number : 08061222000\n")
    elif n==2:
        print("Cardiac(Heart Related) Hospitals in East Bangalore : \n"
              "1. Bowring and Lady Curzon Hospital, Shivaji Nagar, Contact Number : 08022156947\n"
              "2. Vikram Hospital, Millers Road, Contact Number : 08061914686\n")
    elif n==3:
        print("Orthopadeic(Bones and Muscles Related) Hospitals in East Bangalore : \n"
              "1. Bowring and Lady Curzon Hospital, Shivaji Nagar, Contact Number : 08022156947\n"
              "2. Divine Speciality Hospital, Benson Town, Contact number : 08023530333\n")
    elif n==4:
        print("ENT(Hearing and Speech Related) Hospitals in East Bangalore : \n"
              "1. Bowring and Lady Curzon Hospital, Shivaji Nagar, Contact Number : 08022156947\n"
              "2. Sundar Hospital, Lingarajapuram, Contact Number : 08025478586\n")
    elif n==5:
        print("Dental(Tooth Related) Hospitals in East Bangalore : \n"
              "1. Bowring and Lady Curzon Hospital, Shivaji Nagar, Contact Number : 08022156947\n"
              "2. Divine Speciality Hospital, Benson Town, Contact number : 08023530333\n")
    elif n==6:
        print("General or any other disease related Hospitals in East Bangalore : \n"
              "1. Bowring and Lady Curzon Hospital, Shivaji Nagar, Contact Number : 08022156947\n"
              "2. Sparsh Hospitals, Invantry Road, Contact number : 08061222000\n")
    else:
        print("Wrong Input\n")
east()




