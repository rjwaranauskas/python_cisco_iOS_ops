# ----------------------------------------------------------------
# ---------------Cisco iOS Interface Status Checker---------------
# ----------Reads from ip int brief text file, searches for-------
# ----------the interface and ip address (unassigned or not)------
# ---and allows user to check the status of specified interface---
# -------------Written by Richard Waranauskas 8/3/18--------------
# ----------------------------------------------------------------

with open("show_ip_int_brief.txt") as f:
    ipint = f.read()
import re
result_tuple = re.findall(r"(Gigabit.+\s+|FastEthernet.+\s+|Vlan.+\s+)(unassigned | \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", ipint, flags= re.M | re.I)

new_dict = {} #create empty dictionary to update later
for item in result_tuple:
    tempitem = item[0] #set temp item to current tuple "key" (FastEthernet0, 1, etc) - is a string
    tempitem = tempitem.strip() #strip all whitespace from the string
    tempitem2 = item[1] #set temp item to current tuple "value" (unassigned, 10.1.1.1, etc) - is a string
    tempitem2 = tempitem2.strip() #strip whitespace
    new_dict[tempitem] = tempitem2 #create a new key-value pair for the now-stripped interface name (FA1) and its corresponding status

choice = ""
while choice != "Exit":
    print("Useful commands: Type 'Exit' to exit, type 'ints' for a list of interfaces, type 'all' for an overview.")
    choice = input("Please type the name of the interface you want to see the status of.")
    if choice == "Exit":
        print("Exiting program...")
        break
    if choice in new_dict.keys():
        if new_dict[choice] != "unassigned":
            print(f"{choice} has an IP address of {new_dict[choice]}")
        else:
            print(f"{choice} is {new_dict[choice]}")
    elif choice == "ints":
        for item in new_dict.keys():
            print(item)
    elif choice == 'all':
        for key,value in new_dict.items():
            print(f"{key} - {value}")
    else:
        print("You have put an incorrect statement. Please try again.")
    print("-----")