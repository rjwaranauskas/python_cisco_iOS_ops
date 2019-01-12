# -----------------------------------------------
# ----------Cisco iOS Interface Overview---------
# Reads from running/startup config, searches for
# ---the interface, description, and ip address--
# ----and writes the results to console----------
# -----Written by Richard Waranauskas 8/3/18-----
# -----------------------------------------------


filname = "config.txt"

import re, os, sys
from pprint import pprint
with open(filename) as f:
    interface = f.read()


print("Opening ip int file...")
newlist = []
newlist2 = []
newlist2 = re.findall(r"(^interface|^description|^ip address)(.+)", interface, flags= re.M | re.I)

#Operation to strip all the whitespace from each item.
#Since the newlist2 is a list of tuples, a copy of each must be made, stripped, and then put into a separate list of tuples
for item in newlist2:
    tempitem = item[0] #set temp item to first item in current tuple (i.e. interface, description, ip address - is a string)
    tempitem = tempitem.strip() #strip all whitespace from the string
    tempitem2 = item[1] #set temp item to second item in current tuple (i.e. FastEthernet0, GigaBit0, etc) - is a string)
    tempitem2 = tempitem2.strip() #strip whitespace from the string
    newlist.append((tempitem, tempitem2)) #Given newlist is blank, append is used to create a copy of the original results.

for i in range(0,len(newlist)):
    #Below are edge case checks.
    #Check if the iterable i is equal to the last index of the newlist (max length is 13 in testing, but i only goes to 12)
    #So, use len(newlist)-1 to compare properly.
    #Since the last item is interface, it will not have a description or ip by nature. Print it out as such.
    if i == len(newlist)-1 and "interface" in newlist[i]:
        print(f"{newlist[i][0]} - {newlist[i][1]}")
        print("No description")
        print("No ip address")
        break
    #If the end of the list is interface-interface, then print the second-to-last item without a description and name
    #This is done because the original interface check uses i+2 which would be out of range
    #If this is false (end of list is interface - description - interface) then this will not be ran
    if i == len(newlist)-2 and "interface" in newlist[i] and "interface" in newlist[i+1]:
        print(f"{newlist[i][0]} - {newlist[i][1]}")
        print("No description")
        print("No ip address")
        print("-----")
        continue
    #if the second-to-last item is interface and the next one is description, the description item check would be out of range.
    #This section below alleviates that.
    elif i == len(newlist)-2 and "interface" in newlist[i] and "description" in newlist[i+1]:
        print(f"{newlist[i][0]} - {newlist[i][1]}")
        print(f"{newlist[i+1][0]} - {newlist[i+1][1]}")
        print("No ip address")
        print("-----")
        continue 
    #if the second-to-last item is interface and the next one is ip address, the check would be out of range.
    elif i == len(newlist)-2 and "interface" in newlist[i] and "ip address" in newlist[i+1]:
        print(f"{newlist[i][0]} - {newlist[i][1]}")
        print("No description")
        print(f"{newlist[i+1][0]} - {newlist[i+1][1]}")
        print("-----")
        continue 
    #Checks if the current item is "interface" - if not, nothing happens and iterates again.
    elif "interface" in newlist[i]:
        print(f"{newlist[i][0]} - {newlist[i][1]}")
        if "description" in newlist[i+1]:
            print(f"{newlist[i+1][0]} - {newlist[i+1][1]}")
        else:
            print("No description")
        if "ip address" in newlist[i+2]:
            print(f"{newlist[i+2][0]} - {newlist[i+2][1]}")
        else:
            print("No ip address")
        print("-----")