def headache(age):
    global address
    y = "yes"
    if 15 < age <= 30:
        ndays = int(input("Enter number of days symptom has been existent from\n"))
        n = input("Do you experience headache frequently? Yes/No\n")
        if n.casefold() != y.casefold():
            print("Enter severity of the headache on a range of 1-10")
            severity = int(input())
            print("Are you experiencing Nausea or Vomiting as well? Yes/No")
            norv = input()
            if severity <= 5:
                if ndays > 5:
                    print("Please consult a doctor")
                    #hospital(address)
                else:
                    if norv.casefold() != y.casefold():
                        print('''try home remedies like:
                        1)ice pack
                        2)Hydrate yourself with non-caffeinated fluids
                        3)Inhale peppermint or lavender oil
                        4)Exercise regularly\n''')
                        print('''You can also try taking these prescription medications:
                        1)Tylenol
                        2)Motrin
                        3)Aspirin''')
                    else:
                        print('''Try home remedies like:
                        1)Meditation
                        2)Yoga
                        3)Hydration
                        
Also try avoiding certain foods/beverages like:
                        1)Red wine
                        2)Chocolate
                        3)Alcoholic Beverages
                        4)Dairy products\n''')
                        print('''You can also try taking these prescription medications:
                        1)Sumatriptan
                        2)Rizatriptan
                        3)Eletriptan\n''')
                        print("Note: If you are a pregnant woman we suggest you to consult your doctor than\n"
                              "      going for any medications")
            else:
                print("Please consult a doctor")
                #hospital(address)
        else:
            print("Please consult a doctor")
            #hospital(address)
    elif 12 <= age <= 15:
        print("Do not worry it's a regular body change that's leading to a headache")
        print('''Try these:
        1)Meditation
        2)Yoga
        3)Hydration''')
    elif age < 12:
        print("Please consult a doctor")
        #hospital(address)
    else:
        print("Please consult a doctor")
        #hospital(address)
headache(30)
