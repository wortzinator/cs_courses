import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#user input
url = input('Unter URL: ')
webinfo = urllib.request.urlopen(url).read().decode()

#convert to json
data = json.loads(webinfo)

count = 0
value_list = []
num_list = []

#extract the comments
for a in range(len(data["comments"])): # 'a' is the deliminator, the 'range()' is the range of the comments which is 2
    value = data["comments"][a] # value is the 'data' list "comments" 
    value_list.append(value) # adding the value list to t he value_list dict

#extracting the dictionary in list
for item in value_list: # item is iterating through the value_list divt
    count += 1 # count is adding 1 to every new itme in value_list
    number = int(item["count"]) # this is making the 'count' key in the new 'item' list an integer
    num_list.append(number) # adding all of the integer 'number' to the num_list dict
print('Count', count)
print('Sum', sum(num_list))
