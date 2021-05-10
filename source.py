# This file is required. Use the same name, "source.py".
# All of your *foundational* code goes here, meaning the functions and classes
# that can be used to build larger processes. For example, the class you
# created for the OOP assignment would go here.

#amanda final
#ce 3013

#choosing calculation method
method = input("Is the roadway a 1)freeway 2)multilane highway 3)two-lane highway or 4)arterial segment? Enter the corresponding number: ")
#freeway
if method == "1":
    lanes = float(input("Enter the number of lanes in each direction: "))
    phv = float(input("Enter the peak hour volume in vehicles per hour: "))
    truckpercentage = float(input("Enter the percentage of trucks in decimal form: "))
    recreationalvehiclepercentage = float(input("Enter the percentage of recreational vehicles in decimal form: "))
    phf = float(input("Enter the peak hour factor: "))
    lanewidth = float(input("Enter the lane width in feet: "))
    lateralclearance = float(input("Enter the lateral clearance in feet: "))
    rampdensity = float(input("Enter the ramp density in ramps per mile: "))
    terrain = input("Is the terrain level, rolling, or mountainous? ")
    if terrain != ("level"or "rolling" or "mountainous"):
            terrain = input("Is the terrain level, rolling, or mountainous? ")


    #find free-flow speed
    #adjustments to ffs for average lane width
    if lanewidth>=12:
        f_LW = 0
    elif 12>lanewidth>=11:
        f_LW = 1.9
    elif 11>lanewidth>=10:
        f_LW = 6.6
    else:
        print("Unrealistic lane width.")

    #adjustments to ffs to right-side lateral clearance
    if lateralclearance>=6:
        f_LC = 0
    elif lateralclearance == 5:
        if lanes == 2:
            f_LC = 0.6
        elif lanes == 3:
            f_Lc = 0.4
        elif lanes == 4:
            f_LC = 0.2
        elif lanes >= 5:
            f_LC = 0.1
    elif lateralclearance == 4:
        if lanes == 2:
            f_LC = 1.2
        elif lanes == 3:
            f_LC = 0.8
        elif lanes == 4:
            f_LC = 0.4
        elif lanes >= 5:
            f_LC = 0.2
    elif lateralclearance == 3:
        if lanes == 2:
            f_LC = 1.8
        elif lanes == 3:
            f_Lc = 1.2
        elif lanes == 4:
            f_LC = 0.6
        elif lanes >= 5:
            f_LC = 0.3
    elif lateralclearance == 2:
        if lanes == 2:
            f_LC = 2.4
        elif lanes == 3:
            f_LC = 1.6
        elif lanes == 4:
            f_LC = 0.8
        elif lanes >= 5:
            f_LC = 0.4
    elif lateralclearance == 1:
        if lanes == 2:
            f_LC = 3
        elif lanes == 3:
            f_Lc = 2
        elif lanes == 4:
            f_LC = 1
        elif lanes >= 5:
            f_LC = 0.5
    elif lateralclearance == 0:
        if lanes == 2:
            f_LC = 3.6
        elif lanes == 3:
            f_LC = 2.4
        elif lanes == 4:
            f_LC = 1.2
        elif lanes >= 5:
            f_LC = 0.6

    ffs = 75.4 - f_LW - f_LC - 3.22*rampdensity**.84

    #finding PCE
    if terrain == "level":
        E_T = 1.5
        E_R = 1.2
    elif terrain == "rolling":
        E_T = 2.5
        E_R = 2
    elif terrain == "mountainous":
        E_T = 4.5
        E_R = 4

    #finding heavy vehicle factor
    f_HV = 1/(1+(truckpercentage*(E_T-1))+(recreationalvehiclepercentage*(E_R-1)))

    #finding flow rate
    flowrate = phv/(phf*lanes*1*f_HV)

    #finding density = flowrate/avg passenger car speed
    density = flowrate/ffs

    #finding level of service
    if density <= 11:
        los = "A"
        print ("The level of service is A.")
    elif 18>=density>11:
        los = "B"
        print ("The level of service is B.")
    elif 26>=density>18:
        los = "C"
        print ("The level of service is C.")
    elif 35>=density>26:
        los = "D"
        print ("The level of service is D.")
    elif 45>=density>35:
        los = "E"
        print ("The level of service is E.")
    else:
        print("The level of service could not be found.")

#multilane highway
if method == "2":
    lanes = float(input("Enter the number of lanes in each direction: "))
    phv = float(input("Enter the peak hour volume in vehicles per hour: "))
    truckpercentage = float(input("Enter the percentage of trucks in decimal form: "))
    busespercentage = float(input("Enter the percentage of trucks in decimal form: ")
    recreationalvehiclepercentage = float(input("Enter the percentage of recreational vehicles in decimal form: "))
    phf = float(input("Enter the peak hour factor: "))
    lanewidth = float(input("Enter the lane width in feet: "))
    highwaylength = float(input("Enter the length of the highway in feet: "))
    highwaysegmentlength = float(input("Enter the length of the highway segment in ramps per mile: "))
    rightside = float(input("Enter the right-side lateral clearance: "))
    mediantype = input("Enter the median type: ")
    accesspoints = float(input("Enter the roadside access points per mile: "))

    terrain = input("Is the terrain level, rolling, or mountainous? ")
    if terrain != ("level"or "rolling" or "mountainous"):
            terrain = input("Is the terrain level, rolling, or mountainous? ")
    #find flow rate
    if terrain == "level":
        E_T = 1.5
        E_R = 1.2
    elif terrain == "rolling":
        E_T = 2.5
        E_R = 2
    elif terrain == "mountainous":
        E_T = 4.5
        E_R = 4
    f_HV = 1/(1+(truckpercentage*(E_T-1))+(recreationalvehiclepercentage*(E_R-1)))        
    flowrate = phv/(phf*lanes*1*f_HV)


    #find ffs
    if lanewidth>=12:
        f_LW = 0
    elif 12>lanewidth>=11:
        f_LW = 1.9
    elif 11>lanewidth>=10:
        f_LW = 6.6
    else:
        print("Unrealistic lane width.")
        
    #adjustments to ffs to right-side lateral clearance
    if rightside>=6:
        f_LC = 0
    elif rightside == 5:
        if lanes == 2:
            f_LC = 0.6
        elif lanes == 3:
            f_Lc = 0.4
        elif lanes == 4:
            f_LC = 0.2
        elif lanes >= 5:
            f_LC = 0.1
    elif rightside == 4:
        if lanes == 2:
            f_LC = 1.2
        elif lanes == 3:
            f_LC = 0.8
        elif lanes == 4:
            f_LC = 0.4
        elif lanes >= 5:
            f_LC = 0.2
    elif rightside == 3:
        if lanes == 2:
            f_LC = 1.8
        elif lanes == 3:
            f_Lc = 1.2
        elif lanes == 4:
            f_LC = 0.6
        elif lanes >= 5:
            f_LC = 0.3
    elif rightside == 2:
        if lanes == 2:
            f_LC = 2.4
        elif lanes == 3:
            f_LC = 1.6
        elif lanes == 4:
            f_LC = 0.8
        elif lanes >= 5:
            f_LC = 0.4
    elif rightside == 1:
        if lanes == 2:
            f_LC = 3
        elif lanes == 3:
            f_Lc = 2
        elif lanes == 4:
            f_LC = 1
        elif lanes >= 5:
            f_LC = 0.5
    elif rightside == 0:
        if lanes == 2:
            f_LC = 3.6
        elif lanes == 3:
            f_LC = 2.4
        elif lanes == 4:
            f_LC = 1.2
        elif lanes >= 5:
            f_LC = 0.6

    #adjustments for median
    if mediantype == "undivided":
        f_M = 1.6
    else:
        f_M = 0

    #adjustments for access-point density
    if accesspoints == 0:
        f_A = 0
    elif accesspoints == 10:
        f_A = 2.5
    elif accesspoints == 20:
        f_A = 5
    elif accesspoints == 30:
        f_A = 7.5
    elif accesspoints >= 40:
        f_A = 10
    
    ffs = 75.4 - f_LW - f_LC - f_M - f_A
    density = flowrate/ffs

    #assign los
    if 11>density>0:
        print("The level of service is A.")
    elif 18>density>11:
        print("The level of service is B.")
    elif 26>density>18:
        print("The level of service is C.")
    elif 35>density>26:
        print("The level of service is D.")
    elif ffs == 60 and 40>density>35:
        print("The level of service is D.")
    elif ffs == 55 and 41>density>35:
        print("The level of service is D.")
    elif ffs == 50 and 43>density>35:
        print("The level of service is E.")
    elif ffs == 45 and 45>density>35:
        print("The level of service is E.")
    elif ffs == 60 and density>40:
        print("The level of service is E.")
    elif ffs == 55 and density>41:
        print("The level of service is E.")
    elif ffs == 50 and density>43:
        print("The level of service is F.")
    elif ffs == 45 and density>45:
        print("The level of service is F.")
    else:
        print("The level of service could not be found.")
    

#two-lane highway ONLY IF PTSF, ATS, AND FFS ARE KNOWN
if method == "3":
    lanes = float(input("Enter the number of lanes in each direction: "))
    phv = float(input("Enter the peak hour volume in vehicles per hour: "))
    truckpercentage = float(input("Enter the percentage of trucks in decimal form: "))
    recreationalvehiclepercentage = float(input("Enter the percentage of recreational vehicles in decimal form: "))
    phf = float(input("Enter the peak hour factor: "))
    lanewidth = float(input("Enter the lane width in feet: "))
    lateralclearance = float(input("Enter the lateral clearance in feet: "))
    rampdensity = float(input("Enter the ramp density in ramps per mile: "))
    terrain = input("Is the terrain level, rolling, or mountainous? ")
    if terrain != ("level"or "rolling" or "mountainous"):
            terrain = input("Is the terrain level, rolling, or mountainous? ")
