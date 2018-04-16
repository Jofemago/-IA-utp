
import urllib3



def getNameNodes():

    i = 0
    res = {}
    archivo = open('links.csv', 'rt')

    for linea in archivo:

        k = linea.replace(' ', '')
        k = k.replace('\n', '')
        if i > 0:

            j = k.split('.')

            if j[0] in res:
                res[j[0]].append(k)
            else:
                res[j[0]] = [k]

        i+=1
    archivo.close()
    return res


def getDataWeb(url):

    http = urllib3.PoolManager()
    r = http.request('GET', url)
    r.status
    return r.data

def makeArchivos(archivos):

    base = 'elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/'

    for k,v in archivos.items():
        for e in v:
            data = str(getDataWeb(base + e))
            a =data.replace('\\n', ',')
            #b =a.replace('\\', '')
            j = a.split(',')


            if len(e.split('.')) > 2:

                #captura el optimo
                f = open ('archivos/'+ k + '.opt'+'.txt','w')
                for elem in j:
                    f.write(elem + '\n')
                f.close()

            else:

                f = open ('archivos/'+ k +'.txt','w')
                for elem in j:
                    f.write(elem + '\n')
                f.close()

if __name__ == "__main__":

    archivos = getNameNodes()
    #print(archivos)
    makeArchivos(archivos)
