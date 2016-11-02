#Part One

import requests

new_dict = {'token':"3cafef0ef5e44f522dbd2eeb360c9cab",'github': "https://github.com/Horalia/APIRegistration.git"}
response = requests.post("http://challenge.code2040.org/api/register",json = new_dict)
if(response.status_code == 400):
    print("Data did not send")
print("Data sent status code: " + format(response.status_code))


#Part Two

import requests

new_dict = {'token':"3cafef0ef5e44f522dbd2eeb360c9cab"}
response = requests.post("http://challenge.code2040.org/api/reverse",json = new_dict)
if(response.status_code == 400):
    print("Data did not send") 
print("Data sent status code: " + format(response.status_code))
reverseString = (response.text)[::-1]
new_dict['string'] = reverseString
print(new_dict)
response = requests.post("http://challenge.code2040.org/api/reverse/validate", json = new_dict)
if(response.status_code == 400):
    print("Data did not send.")
print("Data sent status code: " + format(response.status_code))

#Part Three

import requests

data = {'token':"3cafef0ef5e44f522dbd2eeb360c9cab"}
response = requests.post("http://challenge.code2040.org/api/haystack",json = data)
if(response.status_code == 400):
    print("Data did not send")
else:
    print("Data sent status code: "+ format(response.status_code))
apiHaystack = response.json()
needle = apiHaystack["needle"]
for index, word in enumerate(apiHaystack["haystack"]):
    if needle == word:
        data['needle'] = index

response = requests.post ("http://challenge.code2040.org/api/haystack/validate", json = data)
print("Data sent status code: " + format(response.status_code))

#Part Four
import requests

new_dict = {'token':"3cafef0ef5e44f522dbd2eeb360c9cab"}
response = requests.post("http://challenge.code2040.org/api/prefix",json = new_dict)
if(response.status_code == 400):
    print("Data did not send")
else:
    print("Data sent status code: "+ format(response.status_code))
Apiprefix = response.json()
print(Apiprefix)
prefix = Apiprefix["prefix"]

new = []
for  word in Apiprefix["array"]:
    if prefix != word[0:len(prefix)]:
        new.append(word)
new_dict['array'] = new
          
      

response = requests.post ("http://challenge.code2040.org/api/prefix/validate", json = new_dict)
print("Data sent status code: " + format(response.status_code))

#Part Five
import requests
import dateutil.parser
import datetime
from datetime import timedelta

data = {'token':"3cafef0ef5e44f522dbd2eeb360c9cab",'github': "https://github.com/Horalia/APIRegistration.git"}
response = requests.post("http://challenge.code2040.org/api/dating",json = data)
if(response.status_code == 400):
    print("Data did not send")
print("Data sent status code: " + format(response.status_code))
datestamp = dateutil.parser.parse((response.json())["datestamp"])
print((response.json())["datestamp"])
interval = (response.json())["interval"]
new_datestamp = (datestamp + datetime.timedelta(0,interval))
print(datestamp.date())
IsoFormat = str(new_datestamp.date()) + 'T' + str(new_datestamp.time()) + 'Z'
data['datestamp'] = IsoFormat

response = requests.post ("http://challenge.code2040.org/api/dating/validate", json = data)
print("Data sent status code: " + format(response.status_code))



