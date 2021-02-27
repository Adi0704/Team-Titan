def fever(age):
    y = "yes"
    ndays = int(input("How many days have you been facing this symptom\n"))
    temp = float(input("Enter the current temperature of your body in degree Fahrenheit\n"))
    if age < 12:
        if temp > 102.2:
            print("Please consult a doctor immediately")
            hospital(address)
        else:
            if ndays < 4:
                print("No need to worry.Some of the home remedies you can try are:\n"
                      "1)Sit in a bath of lukewarm water\n"
                      "2)Wear light clothing\n"
                      "3)Drink cool or room temperature water")
            else:
                print("Suggested medications are:\n"
                      "1)Tylenol\n"
                      "2)Advil\n"
                      "3)Motrin\n")
                doc = input("Do you want to consult the doctor instead? Yes/No\n")
                if doc.casefold() == y.casefold():
                    hospital(address)
    elif 12 < age < 45:
        if temp > 102.2:
            print("Please consult a doctor immediately")
            hospital(address)
        else:
            cov = input("Have u ever been in contact with a COVID-19 patient? Yes/No\n")
            if cov.casefold() == y.casefold():
                diag = input("Have you ever been diagnosed with a condition before? Yes/No\n")
                if diag.casefold() == y.casefold():
                    print("Please consult a doctor immediately")
                    hospital(address)
                else:
                    print("Please get yourself tested at a nearest COVID-19 test centre and Quarantine yourself for at least 4 days")
            else:
                if ndays < 4:
                    print("Some of the home remedies you can try are:\n"
                          "1)Sit in a bath of lukewarm water\n"
                          "2)Wear light clothing\n"
                          "3)Drink cool or room temperature water")
                else:
                    print("Suggested medications are:\n"
                          "1)Ibuprofen\n"
                          "2)Acetaminophen\n"
                          "3)Naproxen\n")
                    doc1 = input("Do you want to consult the doctor instead? Yes/No\n")
                    if doc1.casefold() == y.casefold():
                        hospital(address)
    else:
        print("Please consult a doctor immediately")
        hospital(address)