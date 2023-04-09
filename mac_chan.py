import os
import random
from colorama import Fore,Style

values = [1,2,3,4,5,6,7,8,9,0,"A","B","C","D","E","F"]
mac = []
    
for i in range(6):
    a = random.choice(values)
    b = random.choice(values)
    c = str(a) + str(b)
    mac.append(c)

random_mac = mac[0] + ":" + mac[1] + ":" + mac[2] + ":" + mac[3] + ":" + mac[4] + ":" + mac[5]

print(F"""
{Fore.RED}

 ____    ____                   ______  __                       
|_   \  /   _|                .' ___  |[  |                      
  |   \/   |   ,--.   .---.  / .'   \_| | |--.   ,--.   _ .--.   
  | |\  /| |  `'_\ : / /'`\] | |        | .-. | `'_\ : [ `.-. |  
 _| |_\/_| |_ // | |,| \__.  \ `.___.'\ | | | | // | |, | | | |  
|_____||_____|\'-;__/'.___.'  `.____ .'[___]|__]\'-;__/[___||__] 

                            {Style.RESET_ALL} {Fore.GREEN}Coded By Yigoboz | https://github.com/yigoboz {Style.RESET_ALL}             

[1] Manuel Mac
[2] Random Mac
[3] Exit
""")
try:
    option = int(input("Please Type a Choice: "))
    if option == 1:
        interface = input("\nPlease Choose The Interface: ")
        man_mac = input("Please Type a Mac Adress (Such as = 00:11:22:33:44:55): ")
        os.system(F'ifconfig {interface} down')
        os.system(F'ifconfig {interface} hw ether {man_mac}')
        os.system(F'ifconfig {interface} up')
        print(F"{Fore.GREEN} [+] Mac Adress Changed Succesfuly!{Style.RESET_ALL}")
        print(F"{Fore.YELLOW} [?] New Mac Adress: {man_mac}")
    elif option == 2:
        interface = input("\nPlease Choose The Interface: ")
        os.system(F'ifconfig {interface} down')
        os.system(F'ifconfig {interface} hw ether {random_mac}')
        os.system(F'ifconfig {interface} up')
        print(F"{Fore.GREEN} [+] Mac Adress Changed Succesfuly!{Style.RESET_ALL}")
        print(F"{Fore.YELLOW} [?] New Mac Adress: {random_mac}")
    elif option == 3:
        exit()
except KeyboardInterrupt:
    print(F"\n {Fore.RED} [!] CTRL+C Detected! {Style.RESET_ALL}")