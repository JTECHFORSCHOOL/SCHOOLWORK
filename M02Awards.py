#Joshua Breeden
#AwardsAuto
#Check to see if you have made an award
check = True
while check == True:
    Award = "do not qualifiy"
    NameLast = str(input("Your last name"))
    if NameLast == "ZZZ":
        break
    NameFirst = str(input("Your first name"))
    GPA = float(input("Your GPA"))
    if 3.25<=GPA:
        Award = " are in Honor Roll"
    if GPA>=3.5:
        Award = "are in Dean's List"
    print("you "+ str(Award)+" "+str(NameFirst)+" "+ str(NameLast))
