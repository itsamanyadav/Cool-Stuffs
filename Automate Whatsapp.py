#Firstly you should install pywhatkit from terminal by using - pip install pywhatkit

import pywhatkit
num = input("Enter the reciever number with +91...")
msg = input("Enter your message")
hour = int(input("Enter the time in hour..."))
min = int(input("Enter the minute......"))
print("Starting.......")

pywhatkit.sendwhatmsg(num,msg,hour,min)
