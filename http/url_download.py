from urllib import request

try:
    req = request.urlopen('https://stackoverflow.com')
    cont = req.read()
    #just in one line
    request.urlretrieve('https://www.python.org/static/img/python-logo@2x.png','python.png')
    # print(cont)
    req.close()
except Exception as e:
    print(e)


f = open('python_stack.html','wb')
f.write(cont)
f.close()