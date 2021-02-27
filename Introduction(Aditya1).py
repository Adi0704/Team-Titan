def chat(name):
    print("HELLO  ", end="")
    print(name, end="")
    print("  I am glad to be at your service")
    hello = input("Type 'hello' to chat with Dr.Titan")
    if hello == 'Hello' or hello == 'hello':
        intromenu()
    else:
        print("Please type 'hello' to chat with Dr.Titan:")
        chat(name)
def intromenu():
    print("I will be listing down a list of common symptoms.Please type the serial number corresponding to your symptom:")
    symp=1
    while symp==1:
        symptom=int(input(" 1.Toothache \n 2.Dizziness \n 3.Cold/Running nose \n 4.Fever \n 5.Cough/Throatpain \n 6.Headache \n"))
        if symptom==1:
            'toothache(age,no_of_days)'
        elif symptom==2:
            'dizziness(age,no_of_days)'
        elif symptom==3:
            'cold_runningnose(age,no_of_days)'
        elif symptom==4:
            'fever(age,no_of_days)'
        elif symptom==5:
            'cough_throatpain(age,no_of_days)'
        elif symptom==6:
            '#headache(age,no_of_days)'
        else:
            print("You have entered the wrong option")
        symp=int(input("Do you want to continue (Enter the option) \n 1.Yes 2.No"))
    print("Dr.Titan has left the chat")



print("             Welcome to Titan Health App         ")
print("     We hope to help you as much as possible here!    ")
name=input("Enter your name:")
age=int(input("Enter your age:"))
phno=int(input("Enter your phone number:"))
address=int(input("Enter the option to find where you belong \n 1.Bangalore Central \n 2.Bangalore North \n 3.Bangalore South \n 4.Bangalore East \n 5.Bangalore West \n 6.Bangalore Rural"))
cho=input("Do you want to find a Hospital near you ? Y/N")
if cho=='Y' or cho=='y':
    ##hospital(age)
    print("in hospital")
else:
    print("     Dr.Titan is now available   ")
    chat(name)













