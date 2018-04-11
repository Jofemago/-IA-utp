
import urllib3

def GetData(url):

    http = urllib3.PoolManager()
    r = http.request('GET', url)
    r.status
    return r.data



base = 'elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/'
archivo = 'a280.tsp'
data = str(GetData(base + archivo))
a =data.replace('n', ',')
b =a.replace('\\', '')

j = b.split(',')




f = open (archivo +'.txt','w')
for elem in j:
    f.write(elem + '\n')
f.close()
