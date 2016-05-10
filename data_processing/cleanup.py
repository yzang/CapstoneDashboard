#This python script performs the preprocessing steps needed to provide the data to the crash analysis web application
#Author: Kriti Paliwal
#Date created:4th may 2016
#Date last modified:6th may 2016

import csv

#This function separates all the columns from the csv in separate lists for listwise manipulation of data
def retcol(i,table):
    k=list()
    for j in range(0,len(table)):
        k.append(table[j][i])
    return(k)

#This function performs the metadata mapping for crash table colums 'COLLISION_TYPE','INTERSECT_TYPE' and 'MAX_SEVERITY_LEVEL'
def metaupdate(col,name):
    for i in range(0,len(col[name['COLLISION_TYPE']])):
        if col[name['COLLISION_TYPE']][i] is '0':
            col[name['COLLISION_TYPE']][i] = 'Non collision'
        if col[name['COLLISION_TYPE']][i] is '1':
            col[name['COLLISION_TYPE']][i] = 'Rear-end'
        if col[name['COLLISION_TYPE']][i] is '2':
            col[name['COLLISION_TYPE']][i] = 'Head-on'
        if col[name['COLLISION_TYPE']][i] is '3':
            col[name['COLLISION_TYPE']][i] = 'Rear-to-rear (Backing)'
        if col[name['COLLISION_TYPE']][i] is '4':
            col[name['COLLISION_TYPE']][i] = 'Angle'
        if col[name['COLLISION_TYPE']][i] is '5':
            col[name['COLLISION_TYPE']][i] = 'Sideswipe (same dir.)'
        if col[name['COLLISION_TYPE']][i] is '6':
            col[name['COLLISION_TYPE']][i] = 'Sideswipe (Opposite dir.)'
        if col[name['COLLISION_TYPE']][i] is '7':
            col[name['COLLISION_TYPE']][i] = 'Hit fixed object'
        if col[name['COLLISION_TYPE']][i] is '8':
            col[name['COLLISION_TYPE']][i] = 'Hit pedestrian'
        if col[name['COLLISION_TYPE']][i] is '9':
            col[name['COLLISION_TYPE']][i] = 'Unknown'

    for i in range(0,len(col[name['INTERSECT_TYPE']])):
        if col[name['INTERSECT_TYPE']][i] is '0':
            col[name['INTERSECT_TYPE']][i] = 'Mid-block'
        if col[name['INTERSECT_TYPE']][i] is '1':
            col[name['INTERSECT_TYPE']][i] = 'Four way intersection'
        if col[name['INTERSECT_TYPE']][i] is '2':
            col[name['INTERSECT_TYPE']][i] = 'T intersection'
        if col[name['INTERSECT_TYPE']][i] is '3':
            col[name['INTERSECT_TYPE']][i] = 'Y intersection'
        if col[name['INTERSECT_TYPE']][i] is '4':
            col[name['INTERSECT_TYPE']][i] = 'Traffic circle or Round About'
        if col[name['INTERSECT_TYPE']][i] is '5':
            col[name['INTERSECT_TYPE']][i] = 'Multi-leg intersection'
        if col[name['INTERSECT_TYPE']][i] is '6':
            col[name['INTERSECT_TYPE']][i] = 'On ramp'
        if col[name['INTERSECT_TYPE']][i] is '7':
            col[name['INTERSECT_TYPE']][i] = 'Off ramp'
        if col[name['INTERSECT_TYPE']][i] is '8':
            col[name['INTERSECT_TYPE']][i] = 'Crossover'
        if col[name['INTERSECT_TYPE']][i] is '9':
            col[name['INTERSECT_TYPE']][i] = 'Railroad crossing'
        if col[name['INTERSECT_TYPE']][i] is '10':
            col[name['INTERSECT_TYPE']][i] = 'Other'
        if col[name['INTERSECT_TYPE']][i] is '99':
            col[name['INTERSECT_TYPE']][i] = 'Unknown(expired)'

    for i in range(0,len(col[name['MAX_SEVERITY_LEVEL']])):
        if col[name['MAX_SEVERITY_LEVEL']][i] is '0':
            col[name['MAX_SEVERITY_LEVEL']][i] = 'Not injured'
        if col[name['MAX_SEVERITY_LEVEL']][i] is '1':
            col[name['MAX_SEVERITY_LEVEL']][i] = 'Killed'
        if col[name['MAX_SEVERITY_LEVEL']][i] is '2':
            col[name['MAX_SEVERITY_LEVEL']][i] = 'Major injury'
        if col[name['MAX_SEVERITY_LEVEL']][i] is '3':
            col[name['MAX_SEVERITY_LEVEL']][i] = 'Moderate injury'
        if col[name['MAX_SEVERITY_LEVEL']][i] is '4':
            col[name['MAX_SEVERITY_LEVEL']][i] = 'Minor injury'
        if col[name['MAX_SEVERITY_LEVEL']][i] is '8':
            col[name['MAX_SEVERITY_LEVEL']][i] = 'Injury/ Unknown Severity'
        if col[name['MAX_SEVERITY_LEVEL']][i] is '9':
            col[name['MAX_SEVERITY_LEVEL']][i] = 'Unknown'
    return(col)

#This function calls the function for metadata mapping as well as exporting only the required columns to the output file
def crashclean(crashpath):

    #Reading the csv file
    with open(crashpath, "rU") as f:
        crash = [row for row in csv.reader(f, delimiter=",", dialect=csv.excel_tab)]

    #Creating a dictionary with the name of the variable and its location in the list for later reference
    name = {}
    for i in range(0,len(crash[0])):
        name[crash[0][i]]=i

    #Creating a list for saving the different columns as separate lists
    col=[[]]*(len(crash[0])+5)
    for i in range(0,len(crash[0])):
        col[i]=retcol(i,crash)

    #converitng values to integers for addition
    for i in range(1,len(crash)):
        col[name['MCYCLE_DEATH_COUNT']][i]=int(col[name['MCYCLE_DEATH_COUNT']][i])
        col[name['MCYCLE_MAJ_INJ_COUNT']][i]=int(col[name['MCYCLE_MAJ_INJ_COUNT']][i])
        col[name['BICYCLE_DEATH_COUNT']][i]=int(col[name['BICYCLE_DEATH_COUNT']][i])
        col[name['BICYCLE_MAJ_INJ_COUNT']][i]=int(col[name['BICYCLE_MAJ_INJ_COUNT']][i])
        col[name['PED_DEATH_COUNT']][i]=int(col[name['PED_DEATH_COUNT']][i])
        col[name['PED_MAJ_INJ_COUNT']][i]=int(col[name['PED_MAJ_INJ_COUNT']][i])
        col[name['FATAL_COUNT']][i]=int(col[name['FATAL_COUNT']][i])
        col[name['MAJ_INJ_COUNT']][i]=int(col[name['MAJ_INJ_COUNT']][i])

    #Calculating and Creating severe injuries columns
    col[len(crash[0])]=[x + y for x, y in zip(col[name['MCYCLE_DEATH_COUNT']], col[name['MCYCLE_MAJ_INJ_COUNT']])]
    col[len(crash[0])+1]=[x + y for x, y in zip(col[name['BICYCLE_DEATH_COUNT']], col[name['BICYCLE_MAJ_INJ_COUNT']])]
    col[len(crash[0])+2]=[x + y for x, y in zip(col[name['PED_DEATH_COUNT']], col[name['PED_MAJ_INJ_COUNT']])]
    col[len(crash[0])+3]=[x + y for x, y in zip(col[name['FATAL_COUNT']], col[name['MAJ_INJ_COUNT']])]

    #assigning the labels for newly created severe injury columns
    col[len(crash[0])][0]= 'MCYCLE_SEV_INJ_COUNT'
    col[len(crash[0])+1][0]='BICYCLE_SEV_INJ_COUNT'
    col[len(crash[0])+2][0]='PED_SEV_INJ_COUNT'
    col[len(crash[0])+2][0]='SEV_INJ_COUNT'

    #Updating the dictionary values for the enwly created columns
    name['MCYCLE_SEV_INJ_COUNT']=len(crash[0])
    name['BICYCLE_SEV_INJ_COUNT']=len(crash[0])+1
    name['PED_SEV_INJ_COUNT']=len(crash[0])+2
    name['SEV_INJ_COUNT']=len(crash[0])+3

    #Updating metadata values by calling the function
    col = metaupdate(col,name)

    #zipping the columns together for csv export
    rows = zip(col[name['CRN']],col[name['CRASH_YEAR']],col[name['CRASH_MONTH']],col[name['DAY_OF_WEEK']],col[name['HOUR_OF_DAY']],col[name['INTERSECT_TYPE']],col[name['COLLISION_TYPE']],col[name['FATAL_COUNT']],col[name['INJURY_COUNT']],col[name['SEV_INJ_COUNT']],col[name['MAJ_INJ_COUNT']],col[name['MCYCLE_DEATH_COUNT']],col[name['MCYCLE_SEV_INJ_COUNT']],col[name['BICYCLE_DEATH_COUNT']],col[name['BICYCLE_SEV_INJ_COUNT']],col[name['PED_DEATH_COUNT']],col[name['PED_SEV_INJ_COUNT']],col[name['MAX_SEVERITY_LEVEL']],col[name['LATITUDE']],col[name['LONGITUDE']])

    with open('crash_clean.csv', 'wb') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

#function that performs the metadata update for 'PERSON_TYPE' in person table
def metaupdateperson(col,name):
    for i in range(0,len(col[name['PERSON_TYPE']])):
        if col[name['PERSON_TYPE']][i] is '1':
            col[name['PERSON_TYPE']][i] = 'Driver'
        if col[name['PERSON_TYPE']][i] is '2':
            col[name['PERSON_TYPE']][i] = 'Passenger'
        if col[name['PERSON_TYPE']][i] is '7':
            col[name['PERSON_TYPE']][i] = 'Pedestrian'
        if col[name['PERSON_TYPE']][i] is '8':
            col[name['PERSON_TYPE']][i] = 'Other'
        if col[name['PERSON_TYPE']][i] is '9':
            col[name['PERSON_TYPE']][i] = 'Unknown'
    return(col)

#This function calls the function for metadata mapping as well as exporting only the required columns to the output file
def personclean(personpath):
    with open(personpath, "rU") as f:
        person = [row for row in csv.reader(f, delimiter=",", dialect=csv.excel_tab)]

    name = {}
    for i in range(0,len(person[0])):
        name[person[0][i]]=i

    col=[[]]*(len(person[0]))
    for i in range(0,len(person[0])):
        col[i]=retcol(i,person)

    col = metaupdateperson(col,name)

    rows = zip(col[name['CRN']],col[name['CRASH_YEAR']],col[name['SEX']],col[name['AGE']],col[name['PERSON_TYPE']],col[name['RESTRAINT_HELMET']])
    with open('person_clean.csv', 'wb') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

#function that performs the metadata update for 'VEH_TYPE' in person table
def metaupdatevehicle(col,name):
    for i in range(0,len(col[name['VEH_TYPE']])):
        if col[name['VEH_TYPE']][i] == '1':
            col[name['VEH_TYPE']][i] = 'Automobile'
        if col[name['VEH_TYPE']][i] == '2':
            col[name['VEH_TYPE']][i] = 'Motorcycle'
        if col[name['VEH_TYPE']][i] == '3':
            col[name['VEH_TYPE']][i] = 'Bus'
        if col[name['VEH_TYPE']][i] == '4':
            col[name['VEH_TYPE']][i] = 'Small truck'
        if col[name['VEH_TYPE']][i] == '5':
            col[name['VEH_TYPE']][i] = 'Large truck'
        if col[name['VEH_TYPE']][i] == '6':
            col[name['VEH_TYPE']][i] = 'SUV'
        if col[name['VEH_TYPE']][i] == '7':
            col[name['VEH_TYPE']][i] = 'Van'
        if col[name['VEH_TYPE']][i] == '10':
            col[name['VEH_TYPE']][i] = 'Snowmobile'
        if col[name['VEH_TYPE']][i] == '11':
            col[name['VEH_TYPE']][i] = 'Farm Equipment'
        if col[name['VEH_TYPE']][i] == '12':
            col[name['VEH_TYPE']][i] = 'Construction Equipment'
        if col[name['VEH_TYPE']][i] == '13':
            col[name['VEH_TYPE']][i] = 'ATV'
        if col[name['VEH_TYPE']][i] == '18':
            col[name['VEH_TYPE']][i] = 'Other type special veh'
        if col[name['VEH_TYPE']][i] == '19':
            col[name['VEH_TYPE']][i] = 'Unknown type special veh'
        if col[name['VEH_TYPE']][i] == '20':
            col[name['VEH_TYPE']][i] = 'Unicycle bicycle or tricycle'
        if col[name['VEH_TYPE']][i] == '21':
            col[name['VEH_TYPE']][i] = 'Other pedalcycle'
        if col[name['VEH_TYPE']][i] == '22':
            col[name['VEH_TYPE']][i] = 'Horse and buggy'
        if col[name['VEH_TYPE']][i] == '23':
            col[name['VEH_TYPE']][i] = 'Horse and rider'
        if col[name['VEH_TYPE']][i] == '24':
            col[name['VEH_TYPE']][i] = 'Train'
        if col[name['VEH_TYPE']][i] == '25':
            col[name['VEH_TYPE']][i] = 'unknown'
        if col[name['VEH_TYPE']][i]=='98':
            col[name['VEH_TYPE']][i] = 'unknown'
        if col[name['VEH_TYPE']][i]== '99':
            col[name['VEH_TYPE']][i] = 'unknown'
    return(col)

#This function calls the function for metadata mapping as well as exporting only the required columns to the output file
def vehicleclean(vehiclepath):
    with open(vehiclepath, "rU") as f:
        vehicle = [row for row in csv.reader(f, delimiter=",", dialect=csv.excel_tab)]

    name = {}
    for i in range(0,len(vehicle[0])):
        name[vehicle[0][i]]=i

    col=[[]]*(len(vehicle[0]))
    for i in range(0,len(vehicle[0])):
        col[i]=retcol(i,vehicle)

    for i in range(1,len(vehicle)):
        col[name['VEH_TYPE']][i]=(col[name['VEH_TYPE']][i]).strip()


    col = metaupdatevehicle(col,name)

    rows = zip(col[name['CRN']],col[name['CRASH_YEAR']],col[name['VEH_TYPE']])
    with open('vehicle_clean.csv', 'wb') as f:
        writer = csv.writer(f)
        #Only writing the values with a valid vehicle type, that is ignoring the blank cell values
        for row in rows:
            if row[2]!='':
                writer.writerow(row)

#Calling the crash clean function which updates the metadata for crash file
crashclean("crash.csv")
#Calling the person clean function which updates the metadata for person file
personclean("person.csv")
#Calling the vehicle clean function which updates the metadata for vehicle file
vehicleclean("vehicle.csv")
