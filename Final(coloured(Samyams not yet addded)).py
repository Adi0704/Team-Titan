from colorama import Fore, Back, Style      #Importing Colorama files for foreground and background colours
def feedback():
    print("We hope you have got all the required information that you were looking for.\n\n")
    c=int(input("We would love to hear some feedback from you..Please rate our following project from 1-5: "))
    if c<3:
        print("\n\nWe regret the inconvenience caused ..We will look to make the required changes \n\n")
        change=input("Please tell us where we could improve the project :")

    print("We have noted your valuable feedback \n          THANK YOU FOR USING TITAN HEALTH APP        ")

def south():
    n=int(input(Fore.RED+"Enter 1 for Oncology(Cancer Related) Hospitals \n"
                "Enter 2 for Cardiac(Heart Related) Hospitals\n"
                "Enter 3 for Orthopadeic(Bones and Muscles Related) Hospitals\n"
                "Enter 4 for ENT(Hearing and Speech Related) Hospitals\n"
                "Enter 5 for Dental(Tooth Related) Hospitals \n"
                "Enter 6 for General or any other disease related Hospitals\n"
                "Enter your input : "))
    if n==1:
        print(Fore.YELLOW+"Oncology(Cancer Related) Hospitals in South Bangalore : \n"
              "1. Apollo Hospitals, Jayanagar, Contact Number : 8046124444\n"
              "2. Fortis Hospitals, Bannerghatta Road, Contact Number : 9663367253\n")
    elif n==2:
        print(Fore.YELLOW+"Cardiac(Heart Related) Hospitals in South Bangalore : \n"
              "1.Sri Jayadeva Institute of Cardiovascular Sciences and Research, Bannerghatta Road, Contact Number : 08022977260\n"
              "2.Apollo Hospitals, Jayanagar, Contact Number : 8046124444\n")
    elif n==3:
        print(Fore.YELLOW+"Orthopadeic(Bones and Muscles Related) Hospitals in South Bangalore : \n"
              "1. Fortis Hospitals, Bannerghatta Road, Contact Number : 9663367253\n"
              "2. People Tree Hospitals, Srinagar,Contact number : 9900091881 / 08049599900\n")
    elif n==4:
        print(Fore.YELLOW+"ENT(Hearing and Speech Related) Hospitals in South Bangalore : \n"
              "1. Fortis Hospitals, Bannerghatta Road, Contact Number : 9663367253\n"
              "2. Medikeri's Super Speciality ENT Center, Lalbagh Road, Contact Number : 08026578324\n")
    elif n==5:
        print(Fore.YELLOW+"Dental(Tooth Related) Hospitals in South Bangalore : \n"
              "1. Partha Dental Clinic, Basavangudi, Contact Number : 08050765000\n"
              "2. Apollo Dental Clinic, Basavangudi, Contact Number : 8046124444\n")
    elif n==6:
        print(Fore.YELLOW+"General or any other disease related Hospitals in South Bangalore : \n"
              "1. Apollo Hospitals, Jayanagar, Contact Number : 8046124444\n"
              "2. KR Hospital, Srinagar, Contact Number : 8183675439\n")
    else:
        print(Fore.PINK+"Wrong Input\n")


def north():
    n=int(input(Fore.RED+"Enter 1 for Oncology(Cancer Related) Hospitals \n"
                "Enter 2 for Cardiac(Heart Related) Hospitals\n"
                "Enter 3 for Orthopadeic(Bones and Muscles Related) Hospitals\n"
                "Enter 4 for ENT(Hearing and Speech Related) Hospitals\n"
                "Enter 5 for Dental(Tooth Related) Hospitals \n"
                "Enter 6 for General or any other disease related Hospitals\n"
                "Enter your input : "))
    if n==1:
        print(Fore.YELLOW+"Oncology(Cancer Related) Hospitals in North Bangalore : \n"
              "1. Aster CM Hospitals, Hebbal, Contact Number : 0802214147\n"
              "2. People Tree Hospitals, Yeshwantpura, Contact number : 9900091881 / 08049599900\n")
    elif n==2:
        print(Fore.YELLOW+"Cardiac(Heart Related) Hospitals in North Bangalore : \n"
              "1. M S Ramaiah Narayana Heart Centre, New BEL Road, Contact Number : 08067506870\n"
              "2. Columbia Asia Hospital, Hebbal, Contact Number : 08026727274\n")
    elif n==3:
        print(Fore.YELLOW+"Orthopadeic(Bones and Muscles Related) Hospitals in North Bangalore : \n"
              "1. Columbia Asia Hospital, Hebbal, Contact Number : 08026727274\n"
              "2. People Tree Hospitals,Peenya , Contact number : 9900091881 / 08049599900\n")
    elif n==4:
        print(Fore.YELLOW+"ENT(Hearing and Speech Related) Hospitals in North Bangalore : \n"
              "1. People Tree Hospitals,Peenya , Contact number : 9900091881 / 08049599900\n"
              "2. Dr.Anita's Super Speciality ENT Center, Dasarahalli, Contact Number : 08026578324\n")
    elif n==5:
        print(Fore.YELLOW+"Dental(Tooth Related) Hospitals in North Bangalore : \n"
              "1. Dr.Satish's Dental Clinic, Byatranpura, Contact Number : 08050765000\n"
              "2. Dr.Gangotri's Dental Clinic, Mahalakshmi Layout, Contact Number : 8046124444\n")
    elif n==6:
        print(Fore.YELLOW+"General or any other disease related Hospitals in North Bangalore : \n"
              "1. Apollo Hospitals, Jayanagar, Contact Number : 8046124444\n"
              "2. M S Ramaiah Narayana Multi Speaciality Hospital, MS Ramaiah Nagar, Contact Number : 08067506870\n")
    else:
        print(Fore.PINK+"Wrong Input \n")


def east():
    n=int(input(Fore.RED+"Enter 1 for Oncology(Cancer Related) Hospitals \n"
                "Enter 2 for Cardiac(Heart Related) Hospitals\n"
                "Enter 3 for Orthopadeic(Bones and Muscles Related) Hospitals\n"
                "Enter 4 for ENT(Hearing and Speech Related) Hospitals\n"
                "Enter 5 for Dental(Tooth Related) Hospitals \n"
                "Enter 6 for General or any other disease related Hospitals\n"
                "Enter your input : "))
    if n==1:
        print(Fore.YELLOW+"Oncology(Cancer Related) Hospitals in East Bangalore : \n"
              "1. Bowring and Lady Curzon Hospital, Shivaji Nagar, Contact Number : 08022156947\n"
              "2. Sparsh Hospitals, Invantry Road, Contact number : 08061222000\n")
    elif n==2:
        print(Fore.YELLOW+"Cardiac(Heart Related) Hospitals in East Bangalore : \n"
              "1. Bowring and Lady Curzon Hospital, Shivaji Nagar, Contact Number : 08022156947\n"
              "2. Vikram Hospital, Millers Road, Contact Number : 08061914686\n")
    elif n==3:
        print(Fore.YELLOW+"Orthopadeic(Bones and Muscles Related) Hospitals in East Bangalore : \n"
              "1. Bowring and Lady Curzon Hospital, Shivaji Nagar, Contact Number : 08022156947\n"
              "2. Divine Speciality Hospital, Benson Town, Contact number : 08023530333\n")
    elif n==4:
        print(Fore.YELLOW+"ENT(Hearing and Speech Related) Hospitals in East Bangalore : \n"
              "1. Bowring and Lady Curzon Hospital, Shivaji Nagar, Contact Number : 08022156947\n"
              "2. Sundar Hospital, Lingarajapuram, Contact Number : 08025478586\n")
    elif n==5:
        print(Fore.YELLOW+"Dental(Tooth Related) Hospitals in East Bangalore : \n"
              "1. Bowring and Lady Curzon Hospital, Shivaji Nagar, Contact Number : 08022156947\n"
              "2. Divine Speciality Hospital, Benson Town, Contact number : 08023530333\n")
    elif n==6:
        print(Fore.YELLOW+"General or any other disease related Hospitals in East Bangalore : \n"
              "1. Bowring and Lady Curzon Hospital, Shivaji Nagar, Contact Number : 08022156947\n"
              "2. Sparsh Hospitals, Invantry Road, Contact number : 08061222000\n")
    else:
        print(Fore.PINK+"Wrong Input\n")


def west():
    n=int(input(Fore.RED+"Enter 1 for Oncology(Cancer Related) Hospitals \n"
                "Enter 2 for Cardiac(Heart Related) Hospitals\n"
                "Enter 3 for Orthopadeic(Bones and Muscles Related) Hospitals\n"
                "Enter 4 for ENT(Hearing and Speech Related) Hospitals\n"
                "Enter 5 for Dental(Tooth Related) Hospitals \n"
                "Enter 6 for General or any other disease related Hospitals\n"
                "Enter your input : "))
    if n==1:
        print(Fore.YELLOW+"Oncology(Cancer Related) Hospitals in West Bangalore : \n"
              "1. Gurushree Hospital, Vijay Nagar, Contact Number : 08023392641\n"
              "2. BGS Gleneagles Global Hospitals, Kengeri, Contact number : 1800123111\n")
    elif n==2:
        print(Fore.YELLOW+"Cardiac(Heart Related) Hospitals in West Bangalore : \n"
              "1. Fortis Hospitals, Nagarbhavi, Contact Number : 9663367253\n"
              "2. Jayadeva Hospital ESI, Rajajinagar , Contact Number : 08022977260\n")
    elif n==3:
        print(Fore.YELLOW+"Orthopadeic(Bones and Muscles Related) Hospitals in West Bangalore : \n"
              "1. Abhilash Orthopadeic Hospital, Mahalakshmi Layout, Contact Number : 08022156947\n"
              "2. Sumeru Orthopadeic and Spine Hospital, Rajarajeshwari Nagar, Contact number : 08023530333\n")
    elif n==4:
        print(Fore.YELLOW+"ENT(Hearing and Speech Related) Hospitals in West Bangalore : \n"
              "1. Meenakshi ENT Hospital, Nandini Layout, Contact Number : 08022156947\n"
              "2. Vismaya ENT Clinic, Nagarbhavi, Contact Number : 08025478586\n")
    elif n==5:
        print(Fore.YELLOW+"Dental(Tooth Related) Hospitals in West Bangalore : \n"
              "1. Dr.Suresh Dental Clinic, Basaveshnagar, Contact Number : 08022156947\n"
              "2. Dr.Narendra Dental Clinic, Nayandhalli, Contact number : 08023530333\n")
    elif n==6:
        print(Fore.YELLOW+"General or any other disease related Hospitals in West Bangalore : \n"
              "1. Fortis Hospitals, Nagarbhavi, Contact Number : 9663367253\n"
              "2. BGS Gleneagles Global Hospitals, Kengeri, Contact number : 1800123111\n")
    else:
        print(Fore.PINK+"Wrong Input\n")


def rural():
    n=int(input(Fore.RED+"Enter 1 for Oncology(Cancer Related) Hospitals \n"
                "Enter 2 for Cardiac(Heart Related) Hospitals\n"
                "Enter 3 for Orthopadeic(Bones and Muscles Related) Hospitals\n"
                "Enter 4 for ENT(Hearing and Speech Related) Hospitals\n"
                "Enter 5 for Dental(Tooth Related) Hospitals \n"
                "Enter 6 for General or any other disease related Hospitals\n"
                "Enter your input : "))
    if n==1:
        print(Fore.YELLOW+"Oncology(Cancer Related) Hospitals in Rural Bangalore : \n"
              "1. JP Hospital, Nelamangala, Contact Number : 6366887477\n"
              "2. Columbia Asia Hospitals, Doddaballapur, Contact number : 1800102955\n")
    elif n==2:
        print(Fore.YELLOW+"Cardiac(Heart Related) Hospitals in Rural Bangalore : \n"
              "1. Columbia Asia Hospitals, Doddaballapur, Contact number : 1800102955\n"
              "2. Apollo Hospital, Doddaballapur , Contact Number : 08022826260\n")
    elif n==3:
        print(Fore.YELLOW+"Orthopadeic(Bones and Muscles Related) Hospitals in Rural Bangalore : \n"
              "1. Anand Orthopadeic and Knee Clinic, Hoskote, Contact Number : 08022556947\n"
              "2. Mahadevappa Ortho Clinic, Nelamangala, Contact number : 08023526322\n")
    elif n==4:
        print(Fore.YELLOW+"ENT(Hearing and Speech Related) Hospitals in Rural Bangalore : \n"
              "1. Dr. Madukhar - ENT Specialist, Hoskote, Contact Number : 08022985947\n"
              "2. Netra ENT Clinic, Doddaballapur, Contact Number : 08025710586\n")
    elif n==5:
        print(Fore.YELLOW+"Dental(Tooth Related) Hospitals in Rural Bangalore : \n"
              "1. Dr.Mahesh Dental Clinic, Hoskote, Contact Number : 08021856547\n"
              "2. Dr.Chandru Dental Clinic, Nelamangala, Contact number : 08026539543\n")
    elif n==6:
        print(Fore.YELLOW+"General or any other disease related Hospitals in Rural Bangalore : \n"
              "1. Surksha Hospital, Doddaballapur , Contact Number : 08023834960\n"
              "2. Columbia Asia Hospitals, Doddaballapur, Contact number : 1800102955\n")
    else:
        print(Fore.PINK+"Wrong Input\n")


def central():
    n=int(input(Fore.RED+"Enter 1 for Oncology(Cancer Related) Hospitals \n"
                "Enter 2 for Cardiac(Heart Related) Hospitals\n"
                "Enter 3 for Orthopadeic(Bones and Muscles Related) Hospitals\n"
                "Enter 4 for ENT(Hearing and Speech Related) Hospitals\n"
                "Enter 5 for Dental(Tooth Related) Hospitals \n"
                "Enter 6 for General or any other disease related Hospitals\n"
                "Enter your input : "))
    if n==1:
        print(Fore.YELLOW+"Oncology(Cancer Related) Hospitals in Central Bangalore : \n"
              "1. Apollo Hospital, Seshadripuram, Contact Number : 06366804477\n"
              "2. Manipal Hospitals, Malleshwaram, Contact number : 18001025555\n")
    elif n==2:
        print(Fore.YELLOW+"Cardiac(Heart Related) Hospitals in Central Bangalore : \n"
              "1. Manipal Heart Institute, Domlur, Contact Number : 9663345653\n"
              "2. Fortis Hospital, Malleshwaram , Contact Number : 08022837260\n")
    elif n==3:
        print(Fore.YELLOW+"Orthopadeic(Bones and Muscles Related) Hospitals in Central Bangalore : \n"
              "1. Amrutha Orthopadeic and Knee Clinic, Indiranagar, Contact Number : 08022156947\n"
              "2. The Bone & Joint Clinic Dr.Narendra Rangappa MS Ortho, Malleshwaram, Contact number : 08023526333\n")
    elif n==4:
        print(Fore.YELLOW+"ENT(Hearing and Speech Related) Hospitals in Central Bangalore : \n"
              "1. Dr. Manu Bharath - ENT Specialist, Sadashiva Nagar, Contact Number : 08022985947\n"
              "2. Sanjevini ENT Clinic, Malleshwaram, Contact Number : 08025710586\n")
    elif n==5:
        print(Fore.YELLOW+"Dental(Tooth Related) Hospitals in Central Bangalore : \n"
              "1. Dr.Nagendra Dental Clinic, Domlur, Contact Number : 08022156947\n"
              "2. Dr.Mallendra Dental Clinic, Contonment Area, Contact number : 08023530333\n")
    elif n==6:
        print(Fore.YELLOW+"General or any other disease related Hospitals in Central Bangalore : \n"
              "1. Fortis Hospital, Malleshwaram , Contact Number : 08022837260\n"
              "2. Apollo Hospital, Seshadripuram, Contact Number : 06366804477\n")
    else:
        print(Fore.MAGENTA+"Wrong Input\n")



def dizziness(age):
    if age<60:
        n=input(Fore.MAGENTA+"Is this your 1st incident. Enter Y or N")
        if n=='Y'or n=='y':
            print(Fore.MAGENTA+" Symptoms A")
            print(Fore.GREEN+"Get emergency medical care if you experience new, severe dizziness or vertigo along with any of the following:\n"
                "1.Sudden, severe headache\n"
                "2.Chest pain\n"
                "3.Difficulty breathing\n"
                "4.Numbness or paralysis of arms or legs\n"
                "5.Fainting\n"
                "6.Double vision\n"
                "7.Rapid or irregular heartbeat\n"
                "8.Confusion or slurred speech\n"
                "9.Stumbling or difficulty walking\n"
                "10.Ongoing vomiting\n"
                "11.Seizures\n"
                "12.A sudden change in hearing\n"
                "13.Facial numbness or weakness\n")
            print(Fore.MAGENTA+"B")
            k=input(Fore.GREEN+"enter A if you experience conditions of symptoms listed in A or enter B for home remedies")
            if k=='A':
                hospital(address)
            else:
                print(Fore.MAGENTA+"Try the following home remedies")
                print(Fore.GREEN+'''Steps people can take to relieve dizziness include:
                        1.lying down and closing the eyes.
                        2.acupuncture.
                        3.drinking plenty of water and keeping hydrated.
                        4.reducing stress plus alcohol and tobacco intake.
                        5.getting plenty of sleep.''')
        elif n=='N' or n=='n':
            print(Fore.GREEN+"Consult the doctor as soon as possible")
            print(Fore.GREEN+"We are redirecting you the list of Hospitals \n Please type 6 for General Hospital near you")
            hospital(address)
    else:
        print("Visit the doctor")
        print("We will be redirecting you to our list of hospitals.Please enter 6 for nearest General Hospitals near you")
        hospital(address)


def cold(age):
    n = input(Fore.MAGENTA+"Enter is this your first visit for this issue. ENTER Y for yes and N for no : ")
    if n == 'N'or n=='n':
        print("We will be redirecting you to our list of hospitals.Please enter 6 for nearest General Hospitals near you")
        hospital(address)
    else:
        if age > 6:
            d = input(Fore.MAGENTA+"Enter A:If duration of cold less than 3 days,\nB:if duration of cold more thn 3 days and less than 8,\nC:if 8 or more days")
            if d == 'A':

                print(Fore.MAGENTA+'''Home remedies
                    The most effective and common home remedies for a cold include gargling with saltwater, steam,rest, and staying hydrated.
                    ''')
            elif d == 'B':
                print(Fore.GREEN+'''Topical anticholinergics, such as ipratropium bromide 0.03% nasal spray, may help reduce a runny nose 
                        Topical anticholinergics :  atropine (Atropen)
                                                    belladonna alkaloids.
                                                    benztropine mesylate (Cogentin)
                                                    clidinium.

                        Sometimes, a runny nose is a symptom of an allergic reaction. If this symptom is due to an allergy and not a cold, antihistamines may help.
                        Antihistamines : Brompheniramine (Dimetane)
                                         Cetirizine (Zyrtec)
                                         Chlorpheniramine (Chlor-Trimeton)
                                         Clemastine (Tavist)

                        Decongestants can help relieve a stuffy nose.
                        Decongestants : Afrin, Dristan, Vicks Sinex (oxymetazoline)
                                        Sudafed PE, Suphedrin PE (phenylephrine)
                                        Silfedrine, Sudafed, Suphedrin (pseudoephedrine)

                        Topical nasal sprays offer quick relief but may cause rebound congestion with overuse. 
                        People should restrict using decongestants to a maximum of 3 consecutive days.
                        Topical nasal sprays : Afrin
                                               Flonase 
                                               Nasacort''')
            else:
                print(Fore.MAGENTA+"We will be redirecting to our list of hospitals around you.Please enter 6 for nearest General Hospitals near you")
                hospital(address)
        else:
            print(Fore.GREEN+'''Ease a child’s cold symptoms with these home remedies:

                    1.Rest: Children who have a cold may be more lethargic and irritable than normal. Let them stay home from school and rest until the cold has cleared.

                    2.Hydration: It’s very important children with a cold get plenty of fluids. Colds can dehydrate them quickly. Make sure they’re drinking regularly. Water is great. Warm drinks like tea can pull double duty as a sore throat soother.

                    3.Food: Kids with a cold may not feel as hungry as usual, so look for ways to give them calories and fluids. Smoothies and soups are two great options.

                    4.Salt gargles: They aren’t the most pleasant experience, but gargling with warm, salty water can make sore throats feel better. Saline nasal sprays can also help clear nasal congestion.

                    5.Warm baths: A warm bath can sometimes help reduce a fever and ease mild aches and pains that are common with a cold.''')

def toothache(age):
    if age>12:
        print(Fore.MAGENTA+"CATEGORY")
        print(Fore.MAGENTA+"A")
        print(Fore.MAGENTA+'''If you experience trouble breathing and swallowing along with your pain.
                You have a toothache that lasts longer than one or two days.
                Your toothache is severe.
                You have a fever, earache or pain when you open your mouth wide.
                You experience swelling in the mouth or face.''')
        print(Fore.MAGENTA+"B")
        print(Fore.MAGENTA+"None of those mentioned under A")
        n=input(Fore.MAGENTA+"enter A or B based on your symptoms")
        if n=='A'or n=='a':
            print("We will be redirecting you to our list of hospitals.Please enter 6 for nearest Dental Clinics near you : ")
            hospital(address)
        else:
            print(Fore.GREEN+"Try the following remedies from home AND IF AFTER 2 DAYS YOU STILL EXPERIENCE PAIN VISIT YOUR DENTIST")
            print(Fore.GREEN+'''Home Remedies : 
                    1.Rinse with warm saltwater.
                    2.Rinse with hydrogen peroxide. A hydrogen peroxide (3% solution) helps to reduce inflammation and pain. Dilute the hydrogen peroxide with equal parts water and rinse thoroughly. Don’t swallow it.
                    3.Cold compress. For swelling and pain hold a cold compress of ice wrapped in a towel to the painful area for 20-minute periods. Repeat every few hours.
                    4.Pain medications. Over-the-counter pain medications can reduce pain and inflammation. NSAIDs (nonsteroidal anti-inflammatory drugs) such as aspirin, ibuprofen (Motrin®, Advil®) and naproxen (Aleve®) can be used, or take acetaminophen (Tylenol®) if you can’t take NSAIDs. 
                    DON'T GIVE A CHILD UNDER THE AGE OF 16 aspirin; use Tylenol instead.''')
            print(Fore.GREEN+'''Natural or herbal treatments

                    1.Clove oil. A natural antiseptic that numbs pain and reduces inflammation. Dab a small amount of clove oil on a cotton ball and apply to the painful area. Or add a drop of clove oil to a small glass of water and rinse your mouth thoroughly.
                    2.Vanilla extract. The alcohol in vanilla extract numbs pain temporarily and its antioxidants help the area heal. Use your fingertips or cotton ball to apply the extract to the tooth and gum a few times a day.
                    3.Peppermint tea. Peppermint’s soothing properties can be applied to the painful area with a cooled down peppermint tea bag. Hold this warm tea bag against the tooth and gum.
                    4.Garlic. Make a paste of a crushed garlic clove and apply to the affected area. Garlic can kill bacteria (it contains the antimicrobial allicin) and relieve pain.''')
    else:
        print(Fore.MAGENTA+"We will be redirecting you to the hospital list.Please enter 5 for the nearest Dentist Clinics near you")
        hospital(address)

def headache(age):
    global address
    y = "yes"
    if 15 < age <= 30:
        ndays = int(input(Fore.MAGENTA+"Enter number of days symptom has been existent from\n"))
        n = input(Fore.MAGENTA+"Do you experience headache frequently? Yes/No\n")
        if n.casefold() != y.casefold():
            print(Fore.MAGENTA+"Enter severity of the headache on a range of 1-10")
            severity = int(input())
            print(Fore.MAGENTA+"Are you experiencing Nausea or Vomiting as well? Yes/No")
            norv = input()
            if severity <= 5:
                if ndays > 5:
                    print(Fore.MAGENTA+"Please consult a doctor\nWe will be redirecting you to our list of hospitals.Please enter 6 for nearest General Hospitals near you")
                    hospital(address)
                else:
                    if norv.casefold() != y.casefold():
                        print(Fore.GREEN+'''try home remedies like:
                        1)ice pack
                        2)Hydrate yourself with non-caffeinated fluids
                        3)Inhale peppermint or lavender oil
                        4)Exercise regularly\n''')
                        print(Fore.GREEN+'''You can also try taking these prescription medications:
                        1)Tylenol
                        2)Motrin
                        3)Aspirin''')
                    else:
                        print(Fore.GREEN+'''Try home remedies like:
                        1)Meditation
                        2)Yoga
                        3)Hydration\n                        
                        Also try avoiding certain foods/beverages like:
                        1)Red wine
                        2)Chocolate
                        3)Alcoholic Beverages
                        4)Dairy products\n''')
                        print(Fore.GREEN+'''You can also try taking these prescription medications:
                        1)Sumatriptan
                        2)Rizatriptan
                        3)Eletriptan\n''')
                        print("Note: If you are a pregnant woman we suggest you to consult your doctor than\n"
                              "      going for any medications")
            else:
                print(Fore.MAGENTA+"Please consult a doctor")
                print("We will be redirecting you to our list of hospitals.Please enter 6 for nearest General Hospitals near you : ")
                hospital(address)
        else:
            print(Fore.MAGENTA+"Please consult a doctor")
            print("We will be redirecting you to our list of hospitals.Please enter 6 for nearest General Hospitals near you : ")
            hospital(address)
    elif 12 <= age <= 15:
        print("Do not worry it's a regular body change that's leading to a headache")
        print('''Try these:
        1)Meditation
        2)Yoga
        3)Hydration''')
    elif age < 12:
        print(Fore.GREEN+"Please consult a doctor\nWe will be redirecting you to our list of hospitals.Please enter 6 for nearest General Hospitals near you")
        hospital(address)
    else:
        print(Fore.MAGENTA+"Please consult a doctor\nWe will be redirecting you to our list of hospitals.Please enter 6 for nearest General Hospitals near you")
        hospital(address)

def hospital(address):
    if address == 1:
        central()
    elif address == 2:
        north()
    elif address == 3:
        south()
    elif address == 4:
        east()
    elif address == 5:
        west()
    elif address == 6:
        rural()


def chat(name):
    print(Fore.LIGHTRED_EX+"HELLO  ", end="")
    print(name, end="")
    print(Fore.LIGHTRED_EX+"  I am glad to be at your service")
    hello = input(Fore.LIGHTRED_EX+"Type 'hello' to chat with Dr.Titan : ")
    if hello == 'Hello' or hello == 'hello':
        intromenu()
    else:
        print(Fore.LIGHTRED_EX+"Please type 'hello' to chat with Dr.Titan :")
        chat(name)
def intromenu():
    print(Fore.LIGHTRED_EX+"I will be listing down a list of common symptoms.Please type the serial number corresponding to your symptom :")
    symp='Y'
    while symp=='Y' or symp=='y':
        symptom=int(input(Fore.LIGHTRED_EX+" 1.Toothache \n 2.Dizziness \n 3.Cold/Running nose \n 4.Fever \n 5.Cough/Throatpain \n 6.Headache \n"))
        if symptom==1:
            toothache(age)
        elif symptom==2:
            dizziness(age)
        elif symptom==3:
            cold(age)
        elif symptom==4:
            'fever(age)'
        elif symptom==5:
            'cough_throatpain(age)'
        elif symptom==6:
            headache(age)
        else:
            print(Fore.LIGHTRED_EX+"You have entered the wrong option")
        symp=input(Fore.LIGHTRED_EX+"Do you want to continue (Enter the option) \n 1.Y 2.N : ")
    print(Fore.LIGHTRED_EX+"Dr.Titan has left the chat")



print(Back.LIGHTYELLOW_EX+Fore.RED+"             \N{grinning face}Welcome to Titan Health App\N{face with medical mask}      ")
print(Back.LIGHTYELLOW_EX+Fore.RED+"     We hope to help you as much as possible here!    ")
print(Style.RESET_ALL)
name=input(Fore.CYAN+"Enter your name : ")
age=int(input(Fore.CYAN+"Enter your age : "))
phno=int(input(Fore.CYAN+"Enter your phone number : "))
address=int(input(Fore.CYAN+"Enter the option to find where you belong \n 1.Bangalore Central \n 2.Bangalore North \n 3.Bangalore South \n 4.Bangalore East \n 5.Bangalore West \n 6.Bangalore Rural \n Enter your choice : "))
cho=input(Fore.CYAN+"Do you want to find a Hospital near you ? Y/N : ")
print(Style.RESET_ALL)

if cho=='Y' or cho=='y':
    hospital(address)


else:
    print("     Dr.Titan is now available   ")
    chat(name)
feedback()



