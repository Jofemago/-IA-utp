
import urllib3

def GetData(url):

    http = urllib3.PoolManager()
    r = http.request('GET', url)
    r.status
    return r.data



base = 'elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/'
archivo = 'a280.tsp'
data = str(GetData(base + archivo))
f = open (archivo +'.txt','w')
f.write(data)
f.close()
