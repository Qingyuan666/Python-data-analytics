# Simple Log Analysis
# 95-882 Enterprise Web Development
# 2017 Copyright, Bigrigg

from datetime import datetime
import time

#creating a connection to the log file:
inputfile = open("access_log.txt", "r")

#creating two sets; one to hold the unique set of IP addreses and one to hold the unique set of URL targets:
uniqueIPs = set()
uniqueURLs = set()

#creating a dictionary of each page and how many times it was accessed:
accessDict = dict()

#creating a dictionary of each user and the page & date/time information. User is key, information is a tuple:
userDict = dict()

#creating a temporary list to store log information
tempLogInfo = list()

#creating a tuple to store log information
logInfo = tuple()

#Reading one line at a time into the program from the log file and adding the IPs and URLs to their respective sets:
for x in inputfile:
    splitLine = x.split()
    print ("<",x.rstrip("\n"),">")
    print("     IP: ", splitLine[0])
    print("     URL: ", splitLine[6])
    uniqueIPs.add(splitLine[0])
    uniqueURLs.add(splitLine[6])

    url=splitLine[6]
    #print(url)

    if url in accessDict:
        accessDict[url] +=1
    else:
        accessDict[url] = 1

inputfile.close()

#print("These are the unique IPs:", uniqueIPs)
print("This is the total number of unique IPs:", len(uniqueIPs))

#print("These are the unique URLs:", uniqueURLs)
print("This is the total number of unique URLs:", len(uniqueURLs))

