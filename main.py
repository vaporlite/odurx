## ** Made by redacted#3351 without any knowledge of requests :) ** ##

import requests
from colorama import Fore
import os
import time
import sys

os.system("cls")

tokens = {
    "MTAzMzA1MDY1MDg0Nzc1NjI4OA.GrXxt_.vTh2Tt1O_nKMssIt81gZ1yD2-yL-OuPjB7tlH8",
    "MTA2NDI4MjkzNzY3NzMzNjY0Ng.GZryVX.Rb29AHLM8AbS572pHsXaks9Hw_EVZvpcwarAw0",
    "MTA2NDI3NTQ2NDc0ODgwNjI1Ng.GpjTgT.8o7f7tEcHJmKCZnwsO8qmc0GaKfAolRcf0KXi8"
}

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)

def mainScreen():

    os.system("cls")
    os.system("title Odur X v1.0 - Home")

    print(Fore.MAGENTA + """


                                    ██████╗ ██████╗ ██╗   ██╗██████╗     ██╗  ██╗
                                    ██╔═══██╗██╔══██╗██║   ██║██╔══██╗    ╚██╗██╔╝
                                    ██║   ██║██║  ██║██║   ██║██████╔╝     ╚███╔╝ 
                                    ██║   ██║██║  ██║██║   ██║██╔══██╗     ██╔██╗ 
                                    ╚██████╔╝██████╔╝╚██████╔╝██║  ██║    ██╔╝ ██╗
                                    ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝

                                           - made by redacted aka odur -                                                 
""")

    print(Fore.MAGENTA + "==============================================")
    print(Fore.MAGENTA + "= [" + Fore.WHITE + "1" + Fore.MAGENTA + "]" + Fore.WHITE + " Server Joiner    " + Fore.MAGENTA + "[" + Fore.WHITE + "4" + Fore.MAGENTA + "]" + Fore.WHITE + " HypeSquad Joiner")
    print(Fore.MAGENTA + "= [" + Fore.WHITE + "2" + Fore.MAGENTA + "]" + Fore.WHITE + " Server Leaver    " + Fore.MAGENTA + "[" + Fore.WHITE + "5" + Fore.MAGENTA + "]" + Fore.WHITE + " Webhook Spammer")
    print(Fore.MAGENTA + "= [" + Fore.WHITE + "3" + Fore.MAGENTA + "]" + Fore.WHITE + " Channel Spammer  " + Fore.MAGENTA + "[" + Fore.WHITE + "6" + Fore.MAGENTA + "]" + Fore.LIGHTRED_EX + " soon")
    print(Fore.MAGENTA + "==============================================")
    print("")
    choice = input(Fore.MAGENTA + "[" + Fore.WHITE + "CHOICE?" + Fore.MAGENTA + "]" + Fore.WHITE + " > ")
    Spinner()

    if choice == "1":
        os.system("title Odur X v1.0 - Server Joiner")
        exit = mainScreen()
    if choice == "2":
        os.system("title Odur X v1.0 - Server Leaver")
        exit = mainScreen()
    if choice == "3":
        os.system("title Odur X v1.0 - Channel Spammer")
        os.system("cls")
        print(Fore.MAGENTA + """


                                    ██████╗ ██████╗ ██╗   ██╗██████╗     ██╗  ██╗
                                    ██╔═══██╗██╔══██╗██║   ██║██╔══██╗    ╚██╗██╔╝
                                    ██║   ██║██║  ██║██║   ██║██████╔╝     ╚███╔╝ 
                                    ██║   ██║██║  ██║██║   ██║██╔══██╗     ██╔██╗ 
                                    ╚██████╔╝██████╔╝╚██████╔╝██║  ██║    ██╔╝ ██╗
                                    ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝

                                           - made by redacted aka odur -                                                 
""")

        cnt = input(Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " Enter message content\n" + Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " > ")
        chid = input(Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " Enter channel id\n" + Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " > ")
        amt = input(Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " Amount of messages\n" + Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " > ")
        adv = input(Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " Advertise odur x? (y/n)\n" + Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " > ")

        for i in range(int(amt)):

            for token in tokens:

                try:

                    if adv.lower() == "y" or adv.lower() == "yes":

                        payload = {
                            'content': f"{str(cnt)}\n\n**odur x** hehehe"
                        }

                        header = {
                            'Authorization': str(token)
                        }

                        print(Fore.MAGENTA + "[" + Fore.WHITE + "INFO" + Fore.MAGENTA + "]" + Fore.WHITE + f" Sending post request {str(cnt)}.")

                        r = requests.post(f"https://discord.com/api/v9/channels/{chid}/messages", data=payload, headers=header)

                        print(Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + f" Sent message {str(cnt)}.")

                    elif adv.lower() == "n" or adv.lower() == "no":

                        payload = {
                            'content': str(cnt)
                        }

                        header = {
                            'Authorization': str(token)
                        }

                        print(Fore.MAGENTA + "[" + Fore.WHITE + "INFO" + Fore.MAGENTA + "]" + Fore.WHITE + f" Sending post request {str(cnt)}.")

                        r = requests.post(f"https://discord.com/api/v9/channels/{chid}/messages", data=payload, headers=header)

                        print(Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + f" Sent message {str(cnt)}.")

                    else:

                        exit = mainScreen()

                except:

                    print(Fore.MAGENTA + "[" + Fore.WHITE + "INFO" + Fore.MAGENTA + "]" + Fore.WHITE + f" Message cant be sent")

                print(Fore.MAGENTA + "[" + Fore.WHITE + "INFO" + Fore.MAGENTA + "]" + Fore.WHITE + " Successfully sent all messages")

        exit = mainScreen()
    
    if choice == "4":
        
        os.system("title Odur X v1.0 - HypeSquad Joiner")
        os.system("cls")
        print(Fore.MAGENTA + """


                                    ██████╗ ██████╗ ██╗   ██╗██████╗     ██╗  ██╗
                                    ██╔═══██╗██╔══██╗██║   ██║██╔══██╗    ╚██╗██╔╝
                                    ██║   ██║██║  ██║██║   ██║██████╔╝     ╚███╔╝ 
                                    ██║   ██║██║  ██║██║   ██║██╔══██╗     ██╔██╗ 
                                    ╚██████╔╝██████╔╝╚██████╔╝██║  ██║    ██╔╝ ██╗
                                    ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝

                                           - made by redacted aka odur -                                                 
""")
        print(Fore.MAGENTA + "[" + Fore.WHITE + "INFO" + Fore.MAGENTA + "]" + Fore.WHITE + " 1 : Bravery \n" + Fore.MAGENTA + "[" + Fore.WHITE + "INFO" + Fore.MAGENTA + "]" + Fore.WHITE + " 2 : Brilliance \n" + Fore.MAGENTA + "[" + Fore.WHITE + "INFO" + Fore.MAGENTA + "]" + Fore.WHITE + " 3 : Balance")
        print("")
        house = input(Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " House choice\n" + Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " > ")

        for token in tokens:

            if house == "1":
                housefinal = 1

            if house == "2":
                housefinal = 2

            if house == "3":
                housefinal = 3

            sess = requests.session()

            headers = {
                'Authorization': str(token)
            }

            payload = {
                'house_id': str(housefinal)
            }

            rep = sess.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
            if rep.status_code == 204:
                print(Fore.MAGENTA + "[" + Fore.WHITE + "INFO" + Fore.MAGENTA + "]" + Fore.LIGHTGREEN_EX + " Success")
            else:
                print(Fore.MAGENTA + "[" + Fore.WHITE + "INFO" + Fore.MAGENTA + "]" + Fore.LIGHTRED_EX + " Failed")
        time.sleep(2)
        exit = mainScreen()

    if choice == "5":

        os.system("title Odur X v1.0 - Webhook Spammer")
        os.system("cls")
        print(Fore.MAGENTA + """


                                    ██████╗ ██████╗ ██╗   ██╗██████╗     ██╗  ██╗
                                    ██╔═══██╗██╔══██╗██║   ██║██╔══██╗    ╚██╗██╔╝
                                    ██║   ██║██║  ██║██║   ██║██████╔╝     ╚███╔╝ 
                                    ██║   ██║██║  ██║██║   ██║██╔══██╗     ██╔██╗ 
                                    ╚██████╔╝██████╔╝╚██████╔╝██║  ██║    ██╔╝ ██╗
                                    ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝

                                           - made by redacted aka odur -                                                
""")
        webhook_url = input(Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " Webhook Url\n" + Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " > ")
        cnt = input(Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " Enter message content\n" + Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " > ")
        amt = input(Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " Amount of messages\n" + Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " > ")
        adv = input(Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " Advertise odur x? (y/n)\n" + Fore.MAGENTA + "[" + Fore.WHITE + "INPUT" + Fore.MAGENTA + "]" + Fore.WHITE + " > ")

        for i in range(int(amt)):

            if adv.lower() == "y" or adv.lower() == "yes":

                json_sh = {

                    'content': f"{str(cnt)}\n\n**odur x** hehehe"

                }

                try:

                    r = requests.post(webhook_url, json=json_sh)
                    if r.status_code == 204:
                        print(Fore.MAGENTA + "[" + Fore.WHITE + "INFO" + Fore.MAGENTA + "]" + Fore.LIGHTGREEN_EX + " Sent message")
                    elif r.status_code == 429:
                        print(Fore.MAGENTA + "[" + Fore.WHITE + "INFO" + Fore.MAGENTA + "]" + Fore.LIGHTRED_EX + " Ratelimit")

                except:

                    pass

            elif adv.lower() == "n" or adv.lower() == "no":

                json_sh = {

                    'content': str(cnt)

                }

                try:

                    r = requests.post(webhook_url, json=json_sh)
                    if r.status_code == 204:
                        print(Fore.MAGENTA + "[" + Fore.WHITE + "INFO" + Fore.MAGENTA + "]" + Fore.LIGHTGREEN_EX + " Sent message")
                    elif r.status_code == 429:
                        print(Fore.MAGENTA + "[" + Fore.WHITE + "INFO" + Fore.MAGENTA + "]" + Fore.LIGHTRED_EX + " Ratelimit")

                except:

                    pass

            else:

                exit = mainScreen()

        time.sleep(2)
        exit = mainScreen()

mainScreen()