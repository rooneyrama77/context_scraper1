import urllib.request

import json

print("enter the query as single word eg:rogerfederer and not roger federer")

print("Please mind your spaces")

name=input()

link = "https://en.wikipedia.org/w/api.php?action=opensearch&search="+name+"&limit=10&format=json"

f = urllib.request.urlopen(link)

myfile = f.read()

x=json.loads(myfile)

print(', '.join(x[2]))