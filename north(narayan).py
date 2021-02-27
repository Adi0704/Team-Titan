def north():
    n=int(input("Enter 1 for Oncology(Cancer Related) Hospitals \n"
                "Enter 2 for Cardiac(Heart Related) Hospitals\n"
                "Enter 3 for Orthopadeic(Bones and Muscles Related) Hospitals\n"
                "Enter 4 for ENT(Hearing and Speech Related) Hospitals\n"
                "Enter 5 for Dental(Tooth Related) Hospitals \n"
                "Enter 6 for General or any other disease related Hospitals\n"
                "Enter your input : "))
    if n==1:
        print("Oncology(Cancer Related) Hospitals in North Bangalore : \n"
              "1. Aster CM Hospitals, Hebbal, Contact Number : 0802214147\n"
              "2. People Tree Hospitals, Yeshwantpura, Contact number : 9900091881 / 08049599900\n")
    elif n==2:
        print("Cardiac(Heart Related) Hospitals in North Bangalore : \n"
              "1. M S Ramaiah Narayana Heart Centre, New BEL Road, Contact Number : 08067506870\n"
              "2. Columbia Asia Hospital, Hebbal, Contact Number : 08026727274\n")
    elif n==3:
        print("Orthopadeic(Bones and Muscles Related) Hospitals in North Bangalore : \n"
              "1. Columbia Asia Hospital, Hebbal, Contact Number : 08026727274\n"
              "2. People Tree Hospitals,Peenya , Contact number : 9900091881 / 08049599900\n")
    elif n==4:
        print("ENT(Hearing and Speech Related) Hospitals in North Bangalore : \n"
              "1. People Tree Hospitals,Peenya , Contact number : 9900091881 / 08049599900\n"
              "2. Dr.Anita's Super Speciality ENT Center, Dasarahalli, Contact Number : 08026578324\n")
    elif n==5:
        print("Dental(Tooth Related) Hospitals in North Bangalore : \n"
              "1. Dr.Satish's Dental Clinic, Byatranpura, Contact Number : 08050765000\n"
              "2. Dr.Gangotri's Dental Clinic, Mahalakshmi Layout, Contact Number : 8046124444\n")
    elif n==6:
        print("General or any other disease related Hospitals in North Bangalore : \n"
              "1. Apollo Hospitals, Jayanagar, Contact Number : 8046124444\n"
              "2. M S Ramaiah Narayana Multi Speaciality Hospital, MS Ramaiah Nagar, Contact Number : 08067506870\n")
    else:
        print("Wrong Input \n")
north()




