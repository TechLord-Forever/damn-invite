#!/usr/bin/python

#Coded by Sreehari
#https://www.facebook.com/xss.py

import base64
import requests

RED = '\033[1;31m'
BLUE = '\033[94m'
BOLD = '\033[1m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
OTRO = '\033[36m'
ENDC = '\033[0m'


logo = RED+"""                                                                                                                                                                                                     
######                          ###                              
#     #   ##   #    # #    #     #  #    # #    # # ##### ###### 
#     #  #  #  ##  ## ##   #     #  ##   # #    # #   #   #      
#     # #    # # ## # # #  #     #  # #  # #    # #   #   #####  
#     # ###### #    # #  # #     #  #  # # #    # #   #   #      
#     # #    # #    # #   ##     #  #   ##  #  #  #   #   #        
######  #    # #    # #    #    ### #    #   ##   #   #   ######   
                                                                              
         \033[1;34m [+] Hackthebox.gr Invite Code Generator [+]    
                                                                  
\033[1;34mCoded:-Sreehari Haridas                                 
\n\033[1;34mContact me:- https://www.facebook.com/xss.py 
\n\033[1;34mHappy Hacking..!!            
--------------------------------------------------------------------
"""+ENDC
print logo

a =requests.post("https://www.hackthebox.eu/api/invite/generate")
print GREEN+a.text+ENDC 
print "\n"
b = raw_input(BLUE+BOLD+"Type the Base64 code : "+ENDC)
print "\n"
print(BLUE+BOLD+"Decoded Code :  {0}".format(YELLOW+b.decode('base64'))+ENDC)

