#Joshua Breeden
#AwardsAuto
#Check to see if you have made an award

#on/off switch value set
check = True
#body
while check == True:
    #set up
    Award = "do not qualifiy"
    NameLast = str(input("Your last name"))
    #on/off switch code placed here to make it less complicated to exit
    if NameLast == "ZZZ":
        break
    #more set up
    NameFirst = str(input("Your first name"))
    GPA = float(input("Your GPA"))
    #The brains
    if 3.25<=GPA:
        Award = " are in Honor Roll"
    if GPA>=3.5:
        Award = "are in Dean's List"
    print("you "+ str(Award)+" "+str(NameFirst)+" "+ str(NameLast))
