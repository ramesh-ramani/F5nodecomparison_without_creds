import f5
from f5.bigip import ManagementRoot
import certifi
import urllib3
import requests
import urllib
import json
import ssl
import re

context = ssl._create_unverified_context()
serviceurl = 'https://<ip of F5 Bigip device>/mgmt/tm/ltm/node'
x_file = open('nodes2.txt', 'r')

##Below lines will extract the nodes from the F5 and store it in a list##

lst=list()

url = serviceurl

uh=urllib.urlopen(url,context=context)
data=uh.read()
js = json.loads(str(data))

for i in js["items"]:

    y=i["name"]
    if y not in lst:

      lst.append(y)

##Below lines will compare the nodes in the list (above) with the names in the nodes2.txt and print out the mathing ones##

for line in x_file:
       for i in lst:
           if i not in line: continue
           else: print line
