from urllib import request
from urllib import parse
import urllib

try:

    #build parameters
    parmas = {"v":"EuC-yVzHhMI","t":"5m56s"}
    q_string = parse.urlencode(parmas)
    print(q_string)

    req = request.urlopen('https://stackoverflow.com')
    cont = req.read() 
    #just in one line
    request.urlretrieve('https://www.python.org/static/img/python-logo@2x.png','python.png')
    # print(cont)
    req.close()
except Exception as e:
    print(e)


f = open('python_stack.html','wb')
# print(dir(urllib))
# print(dir(request))
# type(cont) # this is a binary 
f.write(cont)
#print(cont.decode('UTF-8')) #to print it as a string
f.close()