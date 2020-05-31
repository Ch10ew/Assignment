# Just a small warning to whoever is doing the same assignment. If you copy code and lecturers question, be ready to engage in a QnA ssession on code.
#
# COVID-19 Patient Management System
#
# Things I can add:
# make search to have the list interface
# make search be more like actual search (substring search)
# add help page (don't do until approval)

# Test data backup
#1,-,Looz,ATO,A,012-3456789,looz@mail.com,None,O-,170,60,-,QDFR,QDFR,-,-
#2,-,Chew,ATO,B,0123456788,chew@mail.com,None,A-,170,60,-,QDFR,-,-,-
#3,-,Tang,ATO,C,0123456787,tang@mail.com,None,B-,170,60,-,QDFR,-,-,-
#4,-,Afiq,ATO,A,012-3456789,-,None,A-,-,-,-,QDFR,-,-,-
#5,-,Khoo,ACC,B,-,khoo@mail.com,-,AB+,155,50,-,-,-,-,-
#6,-,Liam,SID,C,012-56434323,-,-,-,-,-,-,-,-,-,-
#7,-,Chew,ACC,D,-,chew2@mail.com,-,-,-,-,-,-,-,-,-
#8,-,Jone,AEO,A,017-2345678,jone@gmail.com,Has Asthma,AB+,167,58,-,-,-,-,-
#9,-,Kenny,SID,D,019-3214321,kenny61@gmail.com,-,B-,182,63,-,-,-,-,-
#10,-,Josephine,AHS,B,011-43214321,josephine@hospitalmail.com,-,O+,164,58,-,-,-,-,-
#11,-,Zach,AHS,A,017-1234123,zach@hospitalmail.com,-,A+,176,82,-,-,-,-,-
#12,-,Toh,AEO,D,013-2345234,toh27@gmail.com,-,AB-,188,83,-,-,-,-,-
#13,-,Nancy,SID,C,-,nancy@gmail.com,-,B+,170,62,-,-,-,-,-
#14,-,Farah,AEO,C,011-65436543,farah.43@gmail.com,-,A-,159,49,-,-,-,-,-
#15,-,Roshen Singh,ATO,D,017-6543654,roshen.s@gmail.com,-,O-,174,66,-,-,-,-,-


# imports
import os


# Parses a file "filename", with a separator of "sep"
# Returns a list of lists of each entry
# Format: PID, CID, Name, Group, Zone, Contact No., Email, Medical History, Blood Group, Height, Weight, T1, T2, T3, Admission
def ParseFile( filename, sep = ',' ):
    tempList = []
    with open( filename, 'r' ) as dataFile:
        for line in dataFile:
            line = line.rstrip( '\n' ) # right strip any newline characters
            tempList.append( line.split( sep ) )
    return tempList


# Writes list of lists "toWrite" to file "filename", with a separator of "sep"
# No return value
# Format: PID, CID, Name, Group, Zone, Contact No., Email, Medical History, Blood Group, Height, Weight, T1, T2, T3, Admission
def WriteToFile( filename, toWrite, sep = ',' ):
    with open( filename, 'w' ) as dataFile:
        for lines in toWrite:
            dataFile.write( ''.join( [ ( str( item ) + sep ) for item in lines ] ).rstrip( sep ) + '\n' )


# Prints text centered, for aesthetics only
# No return value
# args - list of args
# sep - character separating the args
# end - should the print include trailing spaces
def PrintCenter( *args, sep = ' ', endChar = '\n', trailingSpaces = True ):
    # because IDLE is not recognised as a terminal
    try:
        width = os.get_terminal_size().columns
    except:
        width = 120
    
    if ( trailingSpaces ):
        print( "".join( [ ( str( item ) + sep ) for item in args ] ).rstrip( sep ).center( width - 1 ), end = endChar )
    else:
        print( "".join( [ ( str( item ) + sep ) for item in args ] ).rstrip( sep ).center( width - 1 ).rstrip(), end = endChar  )


# Clears console
# No return value
def ClearConsole():
    try:
        # the thing t otry for
        os.get_terminal_size()

        # normal code
        if( os.name == "nt" ):
            os.system( "cls" )
        else:
            os.system( "clear" )
    except:
        # do nothing
        pass


# takes a list of lists and searches for 
def Search( givenList, key = None, value = None, invalidInput = False, invalidText = "Invalid Input" ):
    if ( key == None or value == None ):
        PrintCenter( "Search by? (PID/CID/Name/Group/Zone/Contact Number/Email/" )
        PrintCenter( "Medical History/Blood Group/Height/Weight/Status/T1/T2/T3/Admission): ", endChar = ' ' , trailingSpaces = False )
        enteredInput = input().lower()
        key = 0
        dataFields = ["PID", "CID", "Name", "Group", "Zone", "Contact Number", "Email", "Medical History", "Blood Group", "Height", "Weight", "Status", "T1", "T2", "T3", "Admission"]
        options = []
        sep = '/'
        
        if ( enteredInput == "pid" ):
            key = 0
        elif ( enteredInput == "cid" ):
            key = 1
        elif ( enteredInput == "name" ):
            key = 2
        elif ( enteredInput == "group" ):
            key = 3
            options = [ "ATO", "ACC", "AEO", "SID", "AHS" ]
        elif ( enteredInput == "zone" ):
            key = 4
            options = [ "A", "B", "C", "D" ]
        elif ( enteredInput == "contact Number" ):
            key = 5
        elif ( enteredInput == "email" ):
            key = 6
        elif ( enteredInput == "medical history" ):
            key = 7
        elif ( enteredInput == "blood group" ):
            key = 8
            options = [ "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-" ]
        elif ( enteredInput == "height" ):
            key = 9
        elif ( enteredInput == "weight" ):
            key = 10
        elif ( enteredInput == "status" ):
            key = 11
            options = [ "ACTIVE", "RECOVERED", "DECEASED" ]
        elif ( enteredInput == "t1" ):
            key = 12
            options = [ "QHNF", "QDFR", "HQFR", "HQNF", "CWFR" ]
        elif ( enteredInput == "t2" ):
            key = 13
            options = [ "QHNF", "QDFR", "HQFR", "HQNF", "CWFR" ]
        elif ( enteredInput == "t3" ):
            key = 14
            options = [ "QHNF", "QDFR", "HQFR", "HQNF", "CWFR" ]
        elif ( enteredInput == "admission" ):
            key = 15
            options = [ "Home", "NW", "ICU" ]
        else:
            return False # Invalid Input
        
        possibleArgs = ''.join( [ item + sep for item in options ] ).rstrip( sep )
        if ( possibleArgs ):
            possibleArgs = " (" + possibleArgs + ")"
        
        PrintCenter( f"Enter a {dataFields[key]}{possibleArgs}:", endChar = ' ' , trailingSpaces = False )
        value = input().lower()
    
    foundList = []
    count = 0
    for n in range( len( givenList ) ):
        
        # find
        found = False
        if ( value.isdigit() ):
            if ( givenList[n][key].lower() == value ):
                found = True
        else: # .find() for lenient find, .startswith() for stricter find
            if ( givenList[n][key].lower().find( value ) != -1 ):
                found = True
        
        # if found
        if ( found == True ):
            ClearConsole()
    
            if ( invalidInput ):
                PrintCenter( "==================================================================" )
                PrintCenter( invalidText )
                PrintCenter( "==================================================================" )
                print( "" )
            else:
                print( "\n\n\n" )            
            PrintCenter( "COVID-19 PATIENT MANAGEMENT SYSTEM" )
            PrintCenter( "------------------------------" )
            PrintCenter( "Search" )
            print( '' )
            PrintCenter( "1.  PID : ", givenList[n][0] )
            PrintCenter( "2.  CID : ", givenList[n][1] )
            PrintCenter( "3.  Name : ", givenList[n][2] )
            PrintCenter( "4.  Group : ", givenList[n][3] )
            PrintCenter( "5.  Zone : ", givenList[n][4] )
            PrintCenter( "6.  Contact Number : ", givenList[n][5] )
            PrintCenter( "7.  Email : ", givenList[n][6] )
            PrintCenter( "8.  Medical History : ", givenList[n][7] )
            PrintCenter( "9.  Blood Group : ", givenList[n][8] )
            PrintCenter( "10. Height : ", givenList[n][9] )
            PrintCenter( "11. Weight : ", givenList[n][10] )
            PrintCenter( "12. Status : ", givenList[n][11] )
            PrintCenter( "13. Test 1 : ", givenList[n][12] )
            PrintCenter( "14. Test 2 : ", givenList[n][13] )
            PrintCenter( "15. Test 3 : ", givenList[n][14] )
            PrintCenter( "16. Admission : ", givenList[n][15] )
            print( '' )
            PrintCenter( "Is this entry what you were looking for? (\"Y\" to end search / \"N\" to continue search):", endChar = ' ' , trailingSpaces = False )
            
            enteredInput = input().upper()
            
            if ( enteredInput == "Y" ):
                return givenList[n]
            elif ( enteredInput == "N" ):
                if not ( Search( givenList[ ( n + 1 ) : None ], key, value ) ):
                    return None
                else:
                    return givenList[n]
            else:
                if not ( Search( givenList[ n : None ], key, value, invalidInput = True ) ):
                    return None
                else:
                    return givenList[n]
            
    return None


def ModifyDetails( givenList, invalidInput = False, invalidText = "Invalid Input" ):
# PID, CID, Name, Group, Zone, Contact No., Email, Medical History, Blood Group, Height, Weight, T1, T2, T3, Admission
    ClearConsole()
    
    if ( invalidInput ):
        PrintCenter( "==================================================================" )
        PrintCenter( invalidText )
        PrintCenter( "==================================================================" )
        print( "" )
    else:
        print( "\n\n\n" )
        
    PrintCenter( "COVID-19 PATIENT MANAGEMENT SYSTEM" )
    PrintCenter( "------------------------------" )
    PrintCenter( "Patient Details Input" )
    print( '' )
    PrintCenter( "1.  PID : ", givenList[0] )
    PrintCenter( "2.  Name : ", givenList[2] )
    PrintCenter( "3.  Group : ", givenList[3] )
    PrintCenter( "4.  Zone : ", givenList[4] )
    PrintCenter( "5.  Contact Number : ", givenList[5] )
    PrintCenter( "6.  Email : ", givenList[6] )
    PrintCenter( "7.  Medical History : ", givenList[7] )
    PrintCenter( "8.  Blood Group : ", givenList[8] )
    PrintCenter( "9.  Height : ", givenList[9] )
    PrintCenter( "10. Weight : ", givenList[10] )
    PrintCenter( "d.  Done" )
    PrintCenter( "x.  Cancel" )
    print( "\n\n\n\n" )
    PrintCenter( "Enter a number to modify its entry:", endChar = ' ' , trailingSpaces = False )
    
    enteredInput = input()

    # PID
    if ( enteredInput == "1" ):
        if not( ModifyDetails( givenList, invalidInput = True, invalidText = "PID cannot be modified" ) ):
            return False

    # Name
    elif ( enteredInput == "2" ):
        PrintCenter( "Enter a new Name (x to cancel):", endChar = ' ' , trailingSpaces = False )
        enteredInput = input()
        noCommaInput = enteredInput.replace( ',', '' )
        
        # validate, no commas allowed
        if ( enteredInput == 'x' or enteredInput == 'X' ):
            if not( ModifyDetails( givenList ) ):
                return False
        elif not( enteredInput.isprintable() and enteredInput == noCommaInput ):
            if not( ModifyDetails( givenList, invalidInput = True, invalidText = "Invalid Input. No Commas allowed in Input." ) ):
                return False
        else:
            givenList[2] = enteredInput
            if not( ModifyDetails( givenList ) ):
                return False

    # Group
    elif ( enteredInput == "3" ):
        PrintCenter( "Enter a new Group (ATO/ACC/AEO/SID/AHS) (x to cancel):", endChar = ' ' , trailingSpaces = False )
        enteredInput = input().upper()
        
        # validate
        allowedGroups = [ "ATO", "ACC", "AEO", "SID", "AHS" ]
        if enteredInput == 'X':
            if not( ModifyDetails( givenList ) ):
                return False
        elif not( enteredInput in allowedGroups ):
            if not( ModifyDetails( givenList, invalidInput = True, invalidText = "Invalid Input. Groups must be ATO, ACC, AEO, SID, or AHS." ) ):
                return False
        else:
            givenList[3] = enteredInput
            if not( ModifyDetails( givenList ) ):
                return False

    # Zone
    elif ( enteredInput == "4" ):
        PrintCenter( "Enter a new Zone (A/B/C/D) (x to cancel):", endChar = ' ' , trailingSpaces = False )
        enteredInput = input().upper()
        
        # validate
        allowedZones = [ 'A', 'B', 'C', 'D' ]
        if enteredInput == 'X':
            if not( ModifyDetails( givenList ) ):
                return False
        elif not( enteredInput in allowedZones ):
            if not( ModifyDetails( givenList, invalidInput = True, invalidText = "Invalid Input. Zones must be A, B, C, or D." ) ):
                return False
        else:
            givenList[4] = enteredInput
            if not( ModifyDetails( givenList ) ):
                return False

    # Contact Number
    elif ( enteredInput == "5" ):
        PrintCenter( "Enter a new Contact Number (x to cancel):", endChar = ' ' , trailingSpaces = False )
        enteredInput = input()
        digits = enteredInput.replace( '-', '' ).replace( '+', '' )
        
        # validate
        if ( enteredInput == 'x' or enteredInput == 'X' ):
            if not( ModifyDetails( givenList ) ):
                return False
        elif not( digits.isdigit() and ( enteredInput.count( '+' ) <= 1 and enteredInput.count( '-' ) <= 1 ) ):
            if not( ModifyDetails( givenList, invalidInput = True, invalidText = "Invalid Input. Contact Number should only consist of digits, a dash and a plus symbol." ) ):
                return False
        else:
            givenList[5] = enteredInput
            if not( ModifyDetails( givenList ) ):
                return False

    # Email
    elif ( enteredInput == "6" ):
        PrintCenter( "Enter a new Email (x to cancel):", endChar = ' ' , trailingSpaces = False )
        enteredInput = input()
        noCommaInput = enteredInput.replace( ',', '' )
        
        # validate
        if ( enteredInput == 'x' or enteredInput == 'X' ):
            if not( ModifyDetails( givenList ) ):
                return False
        elif not( enteredInput.isprintable() and enteredInput == noCommaInput ):
            if not( ModifyDetails( givenList, invalidInput = True, invalidText = "Invalid Input. No Commas allowed in Input." ) ):
                return False
        else:
            givenList[6] = enteredInput
            if not( ModifyDetails( givenList ) ):
                return False

    # Medical History
    elif ( enteredInput == "7" ):
        PrintCenter( "Enter a new Medical History (x to cancel):", endChar = ' ' , trailingSpaces = False )
        enteredInput = input()
        noCommaInput = enteredInput.replace( ',', '' )
        
        # validate, no commas allowed
        if ( enteredInput == 'x' or enteredInput == 'X' ):
            if not( ModifyDetails( givenList ) ):
                return False
        elif not( enteredInput.isprintable() and enteredInput == noCommaInput ):
            if not( ModifyDetails( givenList, invalidInput = True, invalidText = "Invalid Input. No Commas allowed in Input." ) ):
                return False
        else:
            givenList[7] = enteredInput
            if not( ModifyDetails( givenList ) ):
                return False

    # Blood Group
    elif ( enteredInput == "8" ):
        PrintCenter( "Enter a new Blood Group (A+/A-/B+/B-/AB+/AB-/O+/O-) (x to cancel):", endChar = ' ' , trailingSpaces = False )
        enteredInput = input().upper()
        
        # validate
        allowedBloodGroups = [ "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-" ]
        if enteredInput == 'X':
            if not( ModifyDetails( givenList ) ):
                return False
        elif not( enteredInput in allowedBloodGroups ):
            if not( ModifyDetails( givenList, invalidInput = True, invalidText = "Invalid Input. Blood Groups must be A+, A-, B+, B-, AB+, AB-, O+, or O-." ) ):
                return False
        else:
            givenList[8] = enteredInput
            if not( ModifyDetails( givenList ) ):
                return False

    # Height
    elif ( enteredInput == "9" ):
        PrintCenter( "Enter a new Height (x to cancel):", endChar = ' ' , trailingSpaces = False )
        enteredInput = input()
        
        # validate
        if ( enteredInput == 'x' or enteredInput == 'X' ):
            if not( ModifyDetails( givenList ) ):
                return False
        elif not( enteredInput.isdigit() ):
            if not( ModifyDetails( givenList, invalidInput = True, invalidText = "Invalid Input. Height must be a positive number." ) ):
                return False
        elif ( enteredInput.isdigit() ):
            if ( int( enteredInput ) <= 0 ):
                if not( ModifyDetails( givenList, invalidInput = True, invalidText = "Invalid Input. Height must be a positive number." ) ):
                    return False
            else:
                givenList[9] = enteredInput
                if not( ModifyDetails( givenList ) ):
                    return False

    # Weight
    elif ( enteredInput == "10" ):
        PrintCenter( "Enter a new Weight (x to cancel):", endChar = ' ' , trailingSpaces = False )
        enteredInput = input()
        
        # validate
        if ( enteredInput == 'x' or enteredInput == 'X' ):
            if not( ModifyDetails( givenList ) ):
                return False
        elif not( enteredInput.isdigit() ):
            if not( ModifyDetails( givenList, invalidInput = True, invalidText = "Invalid Input. Weight must be a positive number." ) ):
                return False
        else:
            givenList[10] = enteredInput
            if not( ModifyDetails( givenList ) ):
                return False

    elif ( enteredInput == "d" ):
        if ( givenList[3] == '-' or givenList[4] == '-' or ( givenList[5] == '-' and givenList[6] == '-' ) ):
            if not( ModifyDetails( givenList, invalidInput = True, invalidText = "Missing crucial information. Please check Group, Zone, and Contact Number or Email." ) ):
                return False
        else:
            pass
    elif ( enteredInput == 'x' or enteredInput == 'X' ):
        return False

    else:
        if not( ModifyDetails( givenList, invalidInput = True ) ):
            return False

    return givenList


def ModifyTestResults( givenList, invalidInput = False, invalidText = "Invalid Input" ):
# PID, CID, Name, Group, Zone, Contact No., Email, Medical History, Blood Group, Height, Weight, Status, T1, T2, T3, Admission
    allowPreviousTestModification = False
    
    ClearConsole()
    
    if ( invalidInput ):
        PrintCenter( "==================================================================" )
        PrintCenter( invalidText )
        PrintCenter( "==================================================================" )
        print( "" )
    else:
        print( "\n\n\n" )
    
    PrintCenter( "COVID-19 PATIENT MANAGEMENT SYSTEM" )
    PrintCenter( "------------------------------" )
    PrintCenter( "Test Result Details" )
    print( '' )
    PrintCenter( "1.  PID : ", givenList[0] )
    PrintCenter( "2.  CID : ", givenList[1] )
    PrintCenter( "3.  Name : ", givenList[2] )
    PrintCenter( "4.  Group : ", givenList[3] )
    PrintCenter( "5.  Zone : ", givenList[4] )
    PrintCenter( "6.  Status : ", givenList[11] )
    PrintCenter( "7.  Test 1 : ", givenList[12] )
    PrintCenter( "8.  Test 2 : ", givenList[13] )
    PrintCenter( "9.  Test 3 : ", givenList[14] )
    PrintCenter( "10.  Admission : ", givenList[15] )
    PrintCenter( "d.  Done" )
    PrintCenter( "x.  Cancel" )
    print( "\n\n\n\n" )
    PrintCenter( "Enter a number to modify its entry:", endChar = ' ' , trailingSpaces = False )
    
    enteredInput = input()
    
    if ( enteredInput == "1" ):
        if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "PID cannot be modified" ) ):
            return False

    elif ( enteredInput == "2" ):
        if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "CID cannot be modified" ) ):
            return False

    elif ( enteredInput == "3" ):
        if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "Please use the Patient Details Modification interface to modify this field" ) ):
            return False

    elif ( enteredInput == "4" ):
        if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "Please use the Patient Details Modification interface to modify this field" ) ):
            return False

    elif ( enteredInput == "5" ):
        if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "Please use the Patient Details Modification interface to modify this field" ) ):
            return False

    # Status
    elif ( enteredInput == "6" ):
        if ( givenList[1] == "-" ):
            if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "Status cannot be modified unless patient has been tested positive" ) ):
                return False
        else:
            PrintCenter( "Enter a new Status (RECOVERED / DECEASED) (x to cancel):", endChar = ' ' , trailingSpaces = False )
            enteredInput = input().upper()
            
            if ( enteredInput == "RECOVERED" ):
                givenList[11] = "RECOVERED"
                if not( ModifyTestResults( givenList ) ):
                    return False
            elif ( enteredInput == "DECEASED" ):
                givenList[11] = "DECEASED"
                if not( ModifyTestResults( givenList ) ):
                    return False
            elif ( enteredInput == "X" ):
                if not( ModifyTestResults( givenList ) ):
                    return False
            else:
                if not( ModifyTestResults( givenList, invalidInput = True ) ):
                    return False

    # Test 1 / 12
    elif ( enteredInput == "7" ):
        validTestResults = []
        sep = '/'
        if ( givenList[3] == "ATO" or givenList[3] == "ACC" or givenList[3] == "AEO" ):
            validTestResults = [ "QHNF", "QDFR" ]
        elif ( givenList[3] == "SID" ):
            validTestResults = [ "QHNF", "HQFR" ]
        elif ( givenList[3] == "AHS" ):
            validTestResults = [ "HQNF", "CWFR" ]
        
        if ( allowPreviousTestModification ):
            # if either T2 or T3 is set
            if ( givenList[13] != "-" or givenList[14] != "-" ):
                PrintCenter( "Modifying T1 will clear any preexisting data in T2 and T3. Proceed? (Y/N):", endChar = ' ' , trailingSpaces = False )
                enteredInput = input().upper()
                
                if ( enteredInput == "Y" ):
                    # clear T2 and T3, reset Status
                    givenList[11] = "-"
                    givenList[13] = "-"
                    givenList[14] = "-"
                    
                    PrintCenter( f"Enter a new Test Result( { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } ) (x to cancel):", endChar = ' ' , trailingSpaces = False )
                    enteredInput = input().upper()
                    
                    if ( enteredInput == validTestResults[0] ): # positive
                        givenList[12] = validTestResults[0]
                        givenList[11] = "ACTIVE"
                        
                        #find matching PID
                        tempList = ParseFile( "Data.txt" )
                        for lists in tempList:
                            if ( lists[0] == givenList[0] ):
                                givenList[1] = lists[1]
                                break
                        
                        #if empty CID, assign new CID
                        if ( givenList[1] == "-" ):
                            # get newest CID to be used
                            currentCID = 0
                            for items in ParseFile( "Data.txt" ):
                                if ( items[1] != "-" ):
                                    if ( int( items[1] ) > currentCID ):
                                        currentCID = int( items[1] )
                            currentCID += 1
                            givenList[1] = str( currentCID )
                        if not( ModifyTestResults( givenList ) ):
                            return False
                    elif ( enteredInput == validTestResults[1] ): # not positive
                        givenList[1] = "-" # retract CID
                        givenList[11] = "-" # retract Status
                        givenList[15] = "-" # retract Admission
                        givenList[12] = validTestResults[1]
                        if not( ModifyTestResults( givenList ) ):
                            return False
                    elif ( enteredInput == "X" ): # cancel
                        if not( ModifyTestResults( givenList ) ):
                            return False
                    else: # invalid input
                        if not( ModifyTestResults( givenList, invalidInput = True, invalidText = f"Tests can only be { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } for a patient of this group" ) ):
                            return False
                    
                elif ( enteredInput == "N" ):
                    if not( ModifyTestResults( givenList ) ):
                        return False
                else:
                    if not( ModifyTestResults( givenList, invalidInput = True ) ):
                        return False
            else:
                PrintCenter( f"Enter a new Test Result( { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } ) (x to cancel):", endChar = ' ' , trailingSpaces = False )
                enteredInput = input().upper()
                
                if ( enteredInput == validTestResults[0] ): # positive
                    givenList[12] = validTestResults[0]
                    givenList[11] = "ACTIVE"
                    
                    #find matching PID
                    tempList = ParseFile( "Data.txt" )
                    for lists in tempList:
                        if ( lists[0] == givenList[0] ):
                            givenList[1] = lists[1]
                            break
                    
                    #if empty CID, assign new CID
                    if ( givenList[1] == "-" ):
                        # get newest CID to be used
                        currentCID = 0
                        for items in ParseFile( "Data.txt" ):
                            if ( items[1] != "-" ):
                                if ( int( items[1] ) > currentCID ):
                                    currentCID = int( items[1] )
                        currentCID += 1
                        givenList[1] = str( currentCID )
                    if not( ModifyTestResults( givenList ) ):
                        return False
                elif ( enteredInput == validTestResults[1] ): # not positive
                    givenList[1] = "-" # retract CID
                    givenList[11] = "-" # retract Status
                    givenList[15] = "-" # retract Admission
                    givenList[12] = validTestResults[1]
                    if not( ModifyTestResults( givenList ) ):
                        return False
                elif ( enteredInput == "X" ): # cancel
                    if not( ModifyTestResults( givenList ) ):
                        return False
                else: # invalid input
                    if not( ModifyTestResults( givenList, invalidInput = True, invalidText = f"Tests can only be { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } for a patient of this group" ) ):
                        return False
        else:
            if ( givenList[1] == "-" ):
                PrintCenter( f"Enter a new Test Result( { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } ) (x to cancel):", endChar = ' ' , trailingSpaces = False )
                enteredInput = input().upper()
                
                if ( enteredInput == validTestResults[0] ): # positive
                    givenList[12] = validTestResults[0]
                    givenList[11] = "ACTIVE"
                    #if empty CID, assign new CID
                    if ( givenList[1] == "-" ):
                        # get newest CID to be used
                        currentCID = 0
                        for items in ParseFile( "Data.txt" ):
                            if ( items[1] != "-" ):
                                if ( int( items[1] ) > currentCID ):
                                    currentCID = int( items[1] )
                        currentCID += 1
                        givenList[1] = str( currentCID )
                    if not( ModifyTestResults( givenList ) ):
                        return False
                elif ( enteredInput == validTestResults[1] ): # not positive
                    givenList[12] = validTestResults[1]
                    if not( ModifyTestResults( givenList ) ):
                        return False
                elif ( enteredInput == "X" ): # cancel
                    if not( ModifyTestResults( givenList ) ):
                        return False
                else: # invalid input
                    if not( ModifyTestResults( givenList, invalidInput = True, invalidText = f"Tests can only be { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } for a patient of this group" ) ):
                        return False
            else:
                if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "Cannot modify previously set results" ) ):
                    return False

    # Test 2 / 13
    elif ( enteredInput == "8" ):
        validTestResults = []
        sep = '/'
        if ( givenList[3] == "ATO" or givenList[3] == "ACC" or givenList[3] == "AEO" ):
            validTestResults = [ "QHNF", "QDFR" ]
        elif ( givenList[3] == "SID" ):
            validTestResults = [ "QHNF", "HQFR" ]
        elif ( givenList[3] == "AHS" ):
            validTestResults = [ "HQNF", "CWFR" ]
        
        # if T1 not set
        if ( givenList[12] == "-" ):
            if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "Test 1 has not been performed yet" ) ):
                return False
        # if CID set (positive), T2 not done
        elif ( givenList[1] != "-" and givenList[13] == "-" ):
            if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "This patient has been tested positive. No further tests are needed." ) ):
                return False
        elif ( allowPreviousTestModification ):
            # if T3 is set
            if ( givenList[14] != "-" ):
                PrintCenter( "Modifying T1 will clear any preexisting data in T3. Proceed? (Y/N):", endChar = ' ' , trailingSpaces = False )
                enteredInput = input().upper()
                
                if ( enteredInput == "Y" ):
                    # clear T3, recheck Status
                    givenList[14] = "-"
                    if ( givenList[12] != "QHNF" and givenList[12] != "HQNF" ):
                        givenList[11] = "-"
                    
                    PrintCenter( f"Enter a new Test Result( { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } ) (x to cancel):", endChar = ' ' , trailingSpaces = False )
                    enteredInput = input().upper()
                    
                    if ( enteredInput == validTestResults[0] ): # positive
                        givenList[13] = validTestResults[0]
                        givenList[11] = "ACTIVE"
                        
                        #find matching PID
                        tempList = ParseFile( "Data.txt" )
                        for lists in tempList:
                            if ( lists[0] == givenList[0] ):
                                givenList[1] = lists[1]
                                break
                        
                        #if empty CID, assign new CID
                        if ( givenList[1] == "-" ):
                            # get newest CID to be used
                            currentCID = 0
                            for items in ParseFile( "Data.txt" ):
                                if ( items[1] != "-" ):
                                    if ( int( items[1] ) > currentCID ):
                                        currentCID = int( items[1] )
                            currentCID += 1
                            givenList[1] = str( currentCID )
                        if not( ModifyTestResults( givenList ) ):
                            return False
                    elif ( enteredInput == validTestResults[1] ): # not positive
                        givenList[1] = "-" # retract CID
                        givenList[11] = "-" # retract Status
                        givenList[15] = "-" # retract Admission
                        givenList[13] = validTestResults[1]
                        if not( ModifyTestResults( givenList ) ):
                            return False
                    elif ( enteredInput == "X" ): # cancel
                        if not( ModifyTestResults( givenList ) ):
                            return False
                    else: # invalid input
                        if not( ModifyTestResults( givenList, invalidInput = True, invalidText = f"Tests can only be { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } for a patient of this group" ) ):
                            return False
                    
                elif ( enteredInput == "N" ):
                    if not( ModifyTestResults( givenList ) ):
                        return False
                else:
                    if not( ModifyTestResults( givenList, invalidInput = True ) ):
                        return False
            else:
                PrintCenter( f"Enter a new Test Result( { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } ) (x to cancel):", endChar = ' ' , trailingSpaces = False )
                enteredInput = input().upper()
                
                if ( enteredInput == validTestResults[0] ): # positive
                    givenList[13] = validTestResults[0]
                    givenList[11] = "ACTIVE"
                    
                    #find matching PID
                    tempList = ParseFile( "Data.txt" )
                    for lists in tempList:
                        if ( lists[0] == givenList[0] ):
                            givenList[1] = lists[1]
                            break
                    
                    #if empty CID, assign new CID
                    if ( givenList[1] == "-" ):
                        # get newest CID to be used
                        currentCID = 0
                        for items in ParseFile( "Data.txt" ):
                            if ( items[1] != "-" ):
                                if ( int( items[1] ) > currentCID ):
                                    currentCID = int( items[1] )
                        currentCID += 1
                        givenList[1] = str( currentCID )
                    if not( ModifyTestResults( givenList ) ):
                        return False
                elif ( enteredInput == validTestResults[1] ): # not positive
                    givenList[1] = "-" # retract CID
                    givenList[11] = "-" # retract Status
                    givenList[15] = "-" # retract Admission
                    givenList[13] = validTestResults[1]
                    if not( ModifyTestResults( givenList ) ):
                        return False
                elif ( enteredInput == "X" ): # cancel
                    if not( ModifyTestResults( givenList ) ):
                        return False
                else: # invalid input
                    if not( ModifyTestResults( givenList, invalidInput = True, invalidText = f"Tests can only be { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } for a patient of this group" ) ):
                        return False
        else:
            if ( givenList[1] == "-" ):
                PrintCenter( f"Enter a new Test Result( { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } ) (x to cancel):", endChar = ' ' , trailingSpaces = False )
                enteredInput = input().upper()
                
                if ( enteredInput == validTestResults[0] ): # positive
                    givenList[13] = validTestResults[0]
                    givenList[11] = "ACTIVE"
                    #if empty CID, assign new CID
                    if ( givenList[1] == "-" ):
                        # get newest CID to be used
                        currentCID = 0
                        for items in ParseFile( "Data.txt" ):
                            if ( items[1] != "-" ):
                                if ( int( items[1] ) > currentCID ):
                                    currentCID = int( items[1] )
                        currentCID += 1
                        givenList[1] = str( currentCID )
                    if not( ModifyTestResults( givenList ) ):
                        return False
                elif ( enteredInput == validTestResults[1] ): # not positive
                    givenList[13] = validTestResults[1]
                    if not( ModifyTestResults( givenList ) ):
                        return False
                elif ( enteredInput == "X" ): # cancel
                    if not( ModifyTestResults( givenList ) ):
                        return False
                else: # invalid input
                    if not( ModifyTestResults( givenList, invalidInput = True, invalidText = f"Tests can only be { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } for a patient of this group" ) ):
                        return False
            else:
                if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "Cannot modify previously set results" ) ):
                    return False

    # Test 3 / 14
    elif ( enteredInput == "9" ):
        validTestResults = []
        sep = '/'
        if ( givenList[3] == "ATO" or givenList[3] == "ACC" or givenList[3] == "AEO" ):
            validTestResults = [ "QHNF", "QDFR" ]
        elif ( givenList[3] == "SID" ):
            validTestResults = [ "QHNF", "HQFR" ]
        elif ( givenList[3] == "AHS" ):
            validTestResults = [ "HQNF", "CWFR" ]
        
        # if T1 not set
        if ( givenList[12] == "-" ):
            if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "Test 1 has not been performed yet" ) ):
                return False
        # if T2 not set
        elif ( givenList[13] == "-" ):
            if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "Test 2 has not been performed yet" ) ):
                return False
        # if CID set (positive), T3 not done
        elif ( givenList[1] != "-" and givenList[14] == "-" ):
            if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "This patient has been tested positive. No further tests are needed." ) ):
                return False
        elif ( allowPreviousTestModification or not ( givenList[1] != "-" ) ):
            PrintCenter( f"Enter a new Test Result( { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } ) (x to cancel):", endChar = ' ' , trailingSpaces = False )
            enteredInput = input().upper()
            
            if ( enteredInput == validTestResults[0] ): # positive
                givenList[14] = validTestResults[0]
                givenList[11] = "ACTIVE"
                
                #find matching PID
                tempList = ParseFile( "Data.txt" )
                for lists in tempList:
                    if ( lists[0] == givenList[0] ):
                        givenList[1] = lists[1]
                        break
                
                #if empty CID, assign new CID
                if ( givenList[1] == "-" ):
                    # get newest CID to be used
                    currentCID = 0
                    for items in ParseFile( "Data.txt" ):
                        if ( items[1] != "-" ):
                            if ( int( items[1] ) > currentCID ):
                                currentCID = int( items[1] )
                    currentCID += 1
                    givenList[1] = str( currentCID )
                if not( ModifyTestResults( givenList ) ):
                    return False
            elif ( enteredInput == validTestResults[1] ): # not positive
                givenList[1] = "-" # retract CID
                givenList[11] = "-" # retract Status
                givenList[15] = "-" # retract Admission
                givenList[14] = validTestResults[1]
                if not( ModifyTestResults( givenList ) ):
                    return False
            elif ( enteredInput == "X" ): # cancel
                if not( ModifyTestResults( givenList ) ):
                    return False
            else: # invalid input
                if not( ModifyTestResults( givenList, invalidInput = True, invalidText = f"Tests can only be { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } for a patient of this group" ) ):
                    return False
        else:
            if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "Cannot modify previously set results" ) ):
                return False

    # Admission / 15
    elif ( enteredInput == "10" ):
        if ( givenList[1] != "-" ):
            if ( givenList[12] == "HQNF" or givenList[13] == "HQNF" or givenList[14] == "HQNF" ): # if HQNF, auto set to home
                givenList[15] = "Home"
            else:
                #take input
                PrintCenter( f"Enter a new Admission location ( NW/ICU ) (x to cancel):", endChar = ' ' , trailingSpaces = False )
                enteredInput = input().upper()
                
                if ( enteredInput == "NW" ):
                    givenList[15] = "NW"
                    if not( ModifyTestResults( givenList ) ):
                        return False
                elif ( enteredInput == "ICU" ):
                    givenList[15] = "ICU"
                    if not( ModifyTestResults( givenList ) ):
                        return False
                elif ( enteredInput == "X" ):
                    if not( ModifyTestResults( givenList ) ):
                        return False
                else:
                    if not( ModifyTestResults( givenList, invalidInput = True ) ):
                        return False
        else:
            if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "Patient is not tested positive. Cannot set Admission location" ) ):
                return False

    # make sure Admission is filled IF active
    elif ( enteredInput == "d" ):
        if ( givenList[11] != "-" ):
            if ( givenList[15] == "-" ):
                if not( ModifyTestResults( givenList, invalidInput = True, invalidText = "Missing crucial information. Please enter Admission location." ) ):
                    return False
                else:
                    return givenList

    elif ( enteredInput == "x" ):
        return False

    else:
        if not( ModifyTestResults( givenList, invalidInput = True ) ):
            return False

    return givenList


# Takes a list of lists
# No return value
def CalculateTestsPerformed( givenList ):
    # do math first
    T1 = 0
    T2 = 0
    T3 = 0
    for items in givenList:
        if( items[12] != "-" ):
            T1 += 1
        if( items[13] != "-" ):
            T2 += 1
        if( items[14] != "-" ):
            T3 += 1
    
    #print stuff
    ClearConsole()
    print( "\n\n\n" )
    PrintCenter( "COVID-19 PATIENT MANAGEMENT SYSTEM" )
    PrintCenter( "------------------------------" )
    PrintCenter( "Statistics" )
    print( '' )
    PrintCenter( "1. Total Test 1 Performed : ", T1 )
    PrintCenter( "2. Total Test 2 Performed : ", T2 )
    PrintCenter( "3. Total Test 3 Performed : ", T3 )
    print( "\n\n\n\n\n\n\n\n\n\n\n\n\n" )
    PrintCenter( "Press [RETURN] to return to Statistics menu", endChar = ' ' , trailingSpaces = False )
    
    enteredInput = input()


# Takes a list of lists
# Returns True when done
def ShowLists( givenList, page, invalidInput = False, invalidText = "Invalid Input" ):
    # do math
    maxPage = int( ( len( givenList ) - 1 ) / 15 ) + 1

    #print stuff
    ClearConsole()
    if ( invalidInput ):
        PrintCenter( "==================================================================" )
        PrintCenter( invalidText )
        PrintCenter( "==================================================================" )
        print( "" )
    else:
        print( "\n\n\n" )
    PrintCenter( "COVID-19 PATIENT MANAGEMENT SYSTEM" )
    PrintCenter( "------------------------------" )
    PrintCenter( "Statistics (Data might be truncated for display purposes, please use Search for full data)" )
    print( '' )
    
    #print data
    print( "PID CID Name       Grp. Zne. Contact  Email    Med. Hist.   Bld. Ht.  Wt.  Sta. T1   T2   T3   Admission" )
    
    spacings = [ 3, 3, 10, 4, 4, 8, 8, 12, 4, 4, 4, 4, 4, 4, 4, 8 ]
    
    for n in range( ( page - 1) * 15, page * 15 ):
        if ( n >= len( givenList ) ):
            if ( n == 0 ):
                PrintCenter( "================ NO DATA ================" )
            else:
                print( "" )
        else:
            for o in range( 16 ):
                print( givenList[ n ][ o ][ 0 : spacings[ o ] ].ljust( spacings[ o ] ), end = '' )
                if ( o < 15 ):
                    print( ' ', end = '' )
                else:
                    print( '' )
    
    print( "\n\n" )
    print( f"[Page { page } of { maxPage }] \"<\" Previous Page | \">\" Next Page | \"x\" Done Viewing :", end = ' ' )
    
    enteredInput = input().upper()
    
    if ( enteredInput == "<" ):
        if ( page > 1 ):
            page -= 1
            if ( ShowLists( givenList, page ) ):
                return True
        else :
            if ( ShowLists( givenList, page, invalidInput = True, invalidText = "Cannot move page left" ) ):
                return True
    elif ( enteredInput == ">" ):
        if ( page < maxPage ):
            page += 1
            if ( ShowLists( givenList, page ) ):
                return True
        else :
            if ( ShowLists( givenList, page, invalidInput = True, invalidText = "Cannot move page right" ) ):
                return True
    elif ( enteredInput == "X" ):
        return True
    else:
        if ( ShowLists( givenList, page, invalidInput = True ) ):
            return True
    
    return True


# Takes a list of lists
# Returns True when done
def ShowStatistics( givenList, invalidInput = False, invalidText = "Invalid Input" ):
    ClearConsole()
    
    if ( invalidInput ):
        PrintCenter( "==================================================================" )
        PrintCenter( invalidText )
        PrintCenter( "==================================================================" )
        print( "" )
    else:
        print( "\n\n\n" )
    
    PrintCenter( "COVID-19 PATIENT MANAGEMENT SYSTEM" )
    PrintCenter( "------------------------------" )
    PrintCenter( "Statistics" )
    print( '' )
    PrintCenter( "1.  Tests Performed (for T1, T2, and T3)" )
    PrintCenter( "2.  Patients Tested" )
    PrintCenter( "3.  Recovered Cases" )
    PrintCenter( "4.  Positively Tested Patients (by group)" )
    PrintCenter( "5.  Active Cases (by zone)" )
    PrintCenter( "6.  Deceased Patients' Records" )
    PrintCenter( "x.  Cancel" )
    print( "\n\n\n\n\n\n\n\n\n" )
    PrintCenter( "Enter a number:", endChar = ' ' , trailingSpaces = False )
    
    enteredInput = input()
    
    if ( enteredInput == "1" ):
        CalculateTestsPerformed( givenList )
        if ( ShowStatistics( givenList ) ):
            return True
    elif ( enteredInput == "2" ):
        # do math first
        tempList = []
        for items in givenList:
            if ( items[12] != "-" ):
                tempList.append( items )
        
        ShowLists( tempList, 1 )
        if ( ShowStatistics( givenList ) ):
            return True
    elif ( enteredInput == "3" ):
        # do math first
        tempList = []
        for items in givenList:
            if ( items[11] == "RECOVERED" ):
                tempList.append( items )
        
        ShowLists( tempList, 1 )
        if ( ShowStatistics( givenList ) ):
            return True
    elif ( enteredInput == "4" ):
        # take a group
        PrintCenter( "Enter a Group (ATO/ACC/AEO/SID/AHS) (x to cancel):", endChar = ' ' , trailingSpaces = False )
    
        enteredInput = input().upper()
        
        # validate
        allowedGroups = [ "ATO", "ACC", "AEO", "SID", "AHS" ]
        if enteredInput == 'x':
            if ( ShowStatistics( givenList ) ):
                return True
        elif not( enteredInput in allowedGroups ):
            if ( ShowStatistics( givenList, invalidInput = True, invalidText = "Invalid Input. Groups must be ATO, ACC, AEO, SID, or AHS." ) ):
                return True
        else:
            # do math first
            tempList = []
            for items in givenList:
                if ( items[1] != "-" and items[3] == enteredInput ):
                    tempList.append( items )
            
            ShowLists( tempList, 1 )
        if ( ShowStatistics( givenList ) ):
            return True
    elif ( enteredInput == "5" ):
        # take a group
        PrintCenter( "Enter a Zone (A/B/C/D) (x to cancel):", endChar = ' ' , trailingSpaces = False )
    
        enteredInput = input().upper()
        
        # validate
        allowedZones = [ "A", "B", "C", "D" ]
        if enteredInput == 'x':
            if ( ShowStatistics( givenList ) ):
                return True
        elif not( enteredInput in allowedZones ):
            if ( ShowStatistics( givenList, invalidInput = True, invalidText = "Invalid Input. Zones must be A, B, C, or D." ) ):
                return True
        else:
            # do math first
            tempList = []
            for items in givenList:
                if ( items[11] == "ACTIVE" and items[4] == enteredInput ):
                    tempList.append( items )
            
            ShowLists( tempList, 1 )
        if ( ShowStatistics( givenList ) ):
            return True
    elif ( enteredInput == "6" ):
        # do math first
        tempList = []
        for items in givenList:
            if ( items[11] == "DECEASED" ):
                tempList.append( items )
        
        ShowLists( tempList, 1 )
        if ( ShowStatistics( givenList ) ):
            return True
    elif ( enteredInput == "x" ):
        return True
    else:
        ShowStatistics( givenList, invalidInput = True )
    
    return True


# Main menu interface of the program
def MainMenu( invalidInput = False, invalidText = "Invalid Input" ):
    ClearConsole()
    
    if ( invalidInput ):
        PrintCenter( "==================================================================" )
        PrintCenter( invalidText )
        PrintCenter( "==================================================================" )
        print( "" )
    else:
        print( "\n\n\n" )
    
    PrintCenter( "COVID-19 PATIENT MANAGEMENT SYSTEM" )
    PrintCenter( "------------------------------" )
    print( '' )
    PrintCenter( "1.  Register New Patient" )
    PrintCenter( "2.  Modify Patient Record" )
    PrintCenter( "3.  Record/Update Test Details" )
    PrintCenter( "4.  Obtain Statistics" )
    PrintCenter( "5.  Patient Records Search" )
    PrintCenter( "e.  Exit" )
    print( "\n\n\n\n\n\n\n\n\n\n\n" )
    PrintCenter( "Enter a number:", endChar = ' ' , trailingSpaces = False )
    
    enteredInput = input()
    
    # check entered input and call required functions
    if ( enteredInput == "1" ):
        # get newest PID to be used
        currentPID = 0
        for items in ParseFile( "Data.txt" ):
            if ( int( items[0] ) > currentPID ):
                currentPID = int( items[0] )
        currentPID += 1
        
        # call ModifyDetails with empty list, then write the returned list to file
        tempList = ModifyDetails( [ currentPID, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-" ] )
        if ( tempList ):
            WriteToFile( "Data.txt", ParseFile( "Data.txt" ) + [ tempList ] )
            if not( MainMenu( invalidInput = True, invalidText = "Record successfully modified" ) ):
                return False
    elif ( enteredInput == "2" ):
        # search
        tempList = Search( ParseFile( "Data.txt" ) )
        
        # if search found match
        if ( tempList ):
            # call ModifyDetails with found list
            tempBigList = ParseFile( "Data.txt" )
            tempList = ModifyDetails( tempList )
            
            if ( tempList ):
                # substitute updated list with old list, based on PID
                for n in range( len( tempBigList ) ):
                    if ( tempList[0] == tempBigList[n][0] ):
                        tempBigList[n] = tempList
                
                WriteToFile( "Data.txt", tempBigList )
                if not( MainMenu( invalidInput = True, invalidText = "Record successfully modified" ) ):
                    return False
        elif ( tempList == None ):
            if not( MainMenu( invalidInput = True, invalidText = "No Entries found for search term" ) ):
                return False
        elif ( tempList == False ):
            if not( MainMenu( invalidInput = True, invalidText = "Invalid search category" ) ):
                return False

    elif ( enteredInput == "3" ):
        # search
        tempList = Search( ParseFile( "Data.txt" ) )
        
        # if search found match
        if ( tempList ):
            # call ModifyDetails with found list
            tempBigList = ParseFile( "Data.txt" )
            
            tempList = ModifyTestResults( tempList )
            
            if( tempList ):
                # substitute updated list with old list, based on PID
                for n in range( len( tempBigList ) ):
                    if ( tempList[0] == tempBigList[n][0] ):
                        tempBigList[n] = tempList
                
                WriteToFile( "Data.txt", tempBigList )
        elif ( tempList == None ):
            if not( MainMenu( invalidInput = True, invalidText = "No Entries found for search term" ) ):
                return False
        elif ( tempList == False ):
            if not( MainMenu( invalidInput = True, invalidText = "Invalid search category" ) ):
                return False
        
    elif ( enteredInput == "4" ):
        ShowStatistics( ParseFile( "Data.txt" ) )
    elif ( enteredInput == "5" ):
        result = Search( ParseFile( "Data.txt" ) )
        
        if ( result == None ):
            if not( MainMenu( invalidInput = True, invalidText = "Reached end of data" ) ):
                return False
        elif ( result == False ):
            if not( MainMenu( invalidInput = True, invalidText = "Invalid search category" ) ):
                return False
    elif ( enteredInput == "e" ):
        return False

    else:
        if not( MainMenu( invalidInput = True ) ):
            return False

    return True


# Main would start here if it were other languages ¯\_(ツ)_/¯
while MainMenu():
    pass
