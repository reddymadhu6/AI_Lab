
def age_criteria(age):
    if (age<=2):
        print("Infants")
    elif (age<=12):
        print("Kids")
    elif (age<=20):
        print("Teen")
    elif (age<=59):
        print("senior citizens")

age=int(input("Enter the age\n"))
age_criteria(age)
    