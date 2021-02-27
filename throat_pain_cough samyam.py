def tpc(age):
    y = "yes"
    if age <= 2:
        print("Please consult a doctor")
        hospital(address)
    elif 2 < age <= 13:
        print("If the cough or throat pain has been existent for more than 3 weeks please consult doctor immediately\n")
        print("Usually you can let the child recover on his/her own as it it's building their immunity towards it\n")
        print("The following medications might help:\n"
              "1)Dolo syrup\n"
              "2)Dolopar syrup")
    elif 13 < age < 45:
        cov = input("Have u ever been in contact with a COVID-19 patient? Yes/No\n")
        if cov.casefold() == y.casefold():
            diag = input("Have you ever been diagnosed with a condition before? Yes/No\n")
            if diag.casefold() == y.casefold():
                print("Please consult a doctor immediately")
                hospital(address)
            else:
                print("Please get yourself tested at a nearest COVID-19 test centre and Quarantine yourself for at least 4 days")
        else:
            print("Try some home remedies like:\n"
                  "1)Honey Tea\n"
                  "2)Ginger\n"
                  "3)Salt water Gargling\n"
                  "\nAlso some medications like:\n"
                  "1)Robafen Cough\n"
                  "2)Vicks Dayquil Cough")
    elif age >= 45:
        print("Please consult doctor immediately with preferably a COVID-19 report")
        hospital(address)
