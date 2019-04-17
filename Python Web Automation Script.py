# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:20:04 2019

Script that automates the task of getting the checked out status of tens of laptops.

Logs into inventory website with credentials and then querys a given laptop asset for its status.

Prints status of all laptops

@author: Daniel Alnasir
"""


import time
import base64

import requests
import bs4 as bs



#INPUT INFO INTO THESE
name=""

password64=""




LOGIN_URL="https://fastsolutions.mroadmin.com/APEX-Login/account_login.action"
HOME_LOGIN_URL="https://fastsolutions.mroadmin.com/APEX-Login/login.jsp"
LOCKER_URL="https://fastsolutions.mroadmin.com/Apex-Device/assetStatusManagement_serachByAssetId.action?assetStatusManagementBean.siteId=SIT100355631&assetStatusManagementBean.assetId="


ID_NUMBERS=["70","71","72","73","74","75","80","81","82","83","84","85","90","91",
            "92","93","94","95","100","101","102","103","104","105","110",
            "111","112","113","114","115",]



if name=="":
    name=input("What is your username?")

    print("Next time change variable name to your username")

if password64=="":
    password64=input("What is yout password?")

    password64=base64.b64encode(password64.encode())
    print("Next time change variable password64 to your password in base64")



password=base64.b64decode(password64)
   
def Word_Search(string,ID):
#    print(string)
    if ("CHECKEDOUT" in string)==True:
        print(ID,"OUT")
        return"OUT"

    if ("CHECKEDIN" in string)==True:
        print(ID,"IN")
        return"IN"
            
    if ("RECLAIMED" in string)==True:
        print(ID,"RECLAIMED")
        return "RECLAIMED"    
    if ("OVERDUE" in string)==True:
        print(ID,"OVERDUE")
        return"ASSET OVERDUE"
    
    if ("Fixed" in string)==True:
        print(ID,"LOCKED DOWN")
        return "LOCKED DOWN"
    else:
        print(ID,"ERROR 404")
        print(string)
        return string


print("TRIYING user:", name)
print("PASSWORD")
print()


with requests.Session() as s: # Makes a session object
    
    
 
    r=s.get(HOME_LOGIN_URL)

    
    sauce= r.text

    soup= bs.BeautifulSoup(sauce,'lxml')

    
    head=s.headers
    



    payload = {

    'user.login_id': name,
    'user.password': password
            }
    
    p = s.post(LOGIN_URL, data=payload, headers=head)
    
    
    sauce2= p.text
    soup2= bs.BeautifulSoup(sauce2,'lxml')
    
    for currentID in ID_NUMBERS:
        time.sleep(0.1)

        ACTUAL_URL=LOCKER_URL+currentID
        print(currentID)
        
        r3=s.get(ACTUAL_URL)
        sauce3=r3.text
        soup3=bs.BeautifulSoup(sauce3,'lxml')
  
    
        out1=soup3.body
        out2=out1.string
        outnoqoutes=out2.replace('"','')

        out3=outnoqoutes[1:27]

        result=Word_Search(out3,currentID)
