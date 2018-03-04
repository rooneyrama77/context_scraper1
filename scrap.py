import urllib.request

import json

print("enter the query as word")

name=input()

name=name.replace(" ","")

link = "https://en.wikipedia.org/w/api.php?action=opensearch&search="+name+"&limit=100&format=json"

f = urllib.request.urlopen(link)

myfile = f.read()

x=json.loads(myfile)

print(', '.join(x[2]))